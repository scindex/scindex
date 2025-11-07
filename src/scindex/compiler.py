import datetime
import yaml
import json
import toml
import os

def generate_full_ids(data):
    # Traverses the scindex and create full codes
    for division in data.get('divisions', []):
        division_id = division.get('id', '')
        for section in division.get('sections', []):
            section_id = str(section.get('id', '')).zfill(2)
            for item in section.get('items', []):
                item_id = str(item.get('id', '')).zfill(2)
                full_scindex_code = f"{division_id}{section_id}{item_id}"
                item['id'] = full_scindex_code
    return data

def export_json(data, directory):
    #Export JSON file
    output_filename = os.path.join(directory, 'scindex.json')
    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully exported to {output_filename}")

def export_toml(data, directory):
    #Export TOML file
    output_filename = os.path.join(directory, 'scindex.toml')
    with open(output_filename, 'w') as f:
        toml.dump(data, f)
    print(f"Successfully exported to {output_filename}")

def export_txt(data, directory):
    #Export plain text file
    lines = ["Software Component Index (Scindex)"]
    version = data.get('scindex_version')
    lines.append(f"version {version}")
    for division in data.get('divisions', []):
        lines.append(f"\n{division['id']}     {division['name']}")
        lines.append(f"      {division['description']}\n")
        for section in division.get('sections', []):
            lines.append(f"\n{division['id']}{section['id']}   {section['name']}")
            lines.append(f"      {section['description']}")
            for item in section.get('items', []):
                lines.append(f"{item['id']} {item['name']}")
                lines.append(f"      {item['description']}")
    
    output_filename = os.path.join(directory, 'scindex.txt')
    with open(output_filename, 'w') as f:
        f.write("\n".join(lines))
    print(f"Successfully exported to {output_filename}")

def export_markdown(data, directory):
    # Export Markdown file
    version = data.get('scindex_version')
    lines = ["# Software Component Index (Scindex)"]
    lines.append(f"\n version: _{version}_\n date: _{datetime.datetime.now().strftime('%d/%m/%Y')}_ ")
    lines.append(f"\n ---")
    for division in data.get('divisions', []):
        lines.append(f"\n## Division: {division['id']} - {division['name']}")
        if division.get('description'):
            lines.append(f"*{division['description']}*")
        
        for section in division.get('sections', []):
            section_id = str(section['id']).zfill(2)
            lines.append(f"\n### Section: {division['id']}{section_id} - {section['name']}")
            if section.get('description'):
                lines.append(f"_{section['description']}_")
            
            for item in section.get('items', []):
                lines.append(f"\n- **{item['id']}**: {item['name']}")
                if item.get('description'):
                    lines.append(f"  - *Description*: {item['description']}")
                if item.get('examples'):
                    lines.append(f"  - *Examples*: {', '.join(item['examples'])}")

    output_filename = os.path.join(directory, 'scindex.md')
    with open(output_filename, 'w') as f:
        f.write("\n".join(lines))
    print(f"Successfully exported to {output_filename}")

def export_embeddings(data, directory):
    # Only load the library if needed
    from sentence_transformers import SentenceTransformer
    
    # Generates and exports vector embeddings for each scindex item.
    print("Initializing embedding model... (This may take a moment)")
    # Load 'all-MiniLM-L6-v2' for a fast pre-trained starting point
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    embeddings_list = []
    print("Generating embeddings...")

    # Loop through the original data to build rich text blocks
    for division in data.get('divisions', []):
        division_id = division.get('id', '')
        division_name = division.get('name', '')
        for section in division.get('sections', []):
            section_id = str(section.get('id', '')).zfill(2)
            section_name = section.get('name', '')
            for item in section.get('items', []):
                item_id = str(item.get('id', '')).zfill(2)
                full_id = f"{division_id}{section_id}{item_id}"
                item_name = item.get('name', '')
                item_desc = item.get('description', '')
                examples_text = ", ".join(item.get('examples', []))

                # Create a rich text block with context for better embeddings
                text_block = f"{item_name}. Category: {section_name}, {division_name}. Description: {item_desc} Examples: {examples_text}"
                
                # Convert the text to a vector embedding
                vector = model.encode(text_block).tolist() # .tolist() makes it JSON-serializable
                
                embeddings_list.append({
                    "id": full_id,
                    "text": text_block,
                    "vector": vector
                })

    # Save the embeddings to a JSON file
    output_filename = os.path.join(directory, 'scindex.embeddings.json')
    with open(output_filename, 'w') as f:
        json.dump(embeddings_list, f, indent=2)
    print(f"Successfully exported to {output_filename}")


def run_export(source_file, output_dir, formats):
    # Load and parse source file
    with open(source_file, 'r') as f:
        scindex_data = yaml.safe_load(f)

    # The embeddings exporter needs the original data, but others need processed IDs
    processed_data_for_export = generate_full_ids(scindex_data.copy()) 

    # Check output directory
    os.makedirs(output_dir, exist_ok=True)

    # Call exporter(s)
    if 'json' in formats:
        export_json(processed_data_for_export, output_dir)

    if 'toml' in formats:
        export_toml(processed_data_for_export, output_dir)

    if 'txt' in formats:
        export_txt(processed_data_for_export, output_dir)

    if 'md' in formats:
        export_markdown(processed_data_for_export, output_dir)

    if 'embeddings' in formats:
        export_embeddings(scindex_data, output_dir)