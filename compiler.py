import yaml
import json
import argparse

def generate_full_ids(data):
    """
    Traverses the scindex hierarchy and replace simple item IDs
    with full concatenated scindex codes.
    """
    for division in data.get('divisions', []):
        division_id = division.get('id', '')
        for section in division.get('sections', []):
            # zfill(2) ensures two digits (e.g., 1 -> "01")
            section_id = str(section.get('id', '')).zfill(2)
            for item in section.get('items', []):
                item_id = str(item.get('id', '')).zfill(2)
                
                # Construct the full ID, e.g., "DATA" + "01" + "10" -> "DATA0110"
                full_scindex_code = f"{division_id}{section_id}{item_id}"
                
                # Overwrite the item's simple ID with the full one
                item['id'] = full_scindex_code
    return data

# 1. Define command-line arguments
parser = argparse.ArgumentParser(description="Compile scindex.yaml to other formats.")
parser.add_argument('--format', choices=['json', 'toml'], default='json', help='The output format.')
args = parser.parse_args()

# 2. Load and parse the source YAML file
with open('scindex.yaml', 'r') as f:
    scindex_data = yaml.safe_load(f)

# 3. Generate the full IDs from the source data
processed_data = generate_full_ids(scindex_data)

# 4. Export to the chosen format
if args.format == 'json':
    output_filename = 'scindex.json'
    with open(output_filename, 'w') as f:
        # Dump the *processed* data, not the original
        json.dump(processed_data, f, indent=2)
    print(f"Successfully exported to {output_filename}")

# Add other formats as needed...
# elif args.format == 'toml':
#     # ...