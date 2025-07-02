import yaml
import json
import toml
import argparse
import os

def generate_full_ids(data):
    # Traverse the scindex data and creates full scindex codes
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
    output_filename = os.path.join(directory, 'scindex.json')
    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully exported to {output_filename}")

def export_toml(data, directory):
    output_filename = os.path.join(directory, 'scindex.toml')
    with open(output_filename, 'w') as f:
        toml.dump(data, f)
    print(f"Successfully exported to {output_filename}")

def export_txt(data, directory):
    output_filename = os.path.join(directory, 'scindex.txt')
    with open(output_filename, 'w') as f:
        for division in data.get('divisions', []):
            for section in division.get('sections', []):
                for item in section.get('items', []):
                    line = f"{item['id']} {item['name']}\n"
                    f.write(line)
    print(f"Successfully exported to {output_filename}")


# Define CLI arguments
parser = argparse.ArgumentParser(description="Compile scindex.yaml to other formats.")
parser.add_argument(
    '--format', 
    choices=['json', 'toml', 'txt'], 
    default=None,  # <-- Set default to None
    help='The output format. If not specified, all formats will be exported.'
)
args = parser.parse_args()

# Load and parse source file
with open('scindex.yaml', 'r') as f:
    scindex_data = yaml.safe_load(f)
processed_data = generate_full_ids(scindex_data)

# Check output directory
dist_dir = 'dist'
os.makedirs(dist_dir, exist_ok=True)

# Call exporter(s)
if args.format is None or args.format == 'json':
    export_json(processed_data, dist_dir)

if args.format is None or args.format == 'toml':
    export_toml(processed_data, dist_dir)

if args.format is None or args.format == 'txt':
    export_txt(processed_data, dist_dir)