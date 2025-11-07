import argparse
from . import compiler
import os

def main():
    # Main parser
    parser = argparse.ArgumentParser(description="A CLI for working with the Software Component Index (Scindex).")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # 'export' command parser
    export_parser = subparsers.add_parser('export', help='Export the Scindex YAML to other formats.')
    export_parser.add_argument(
        '--dict',
        type=str,
        default='scindex.yaml',
        help='Path to the source scindex.yaml file. Defaults to "scindex.yaml" in the current directory.'
    )
    export_parser.add_argument(
        '--output',
        type=str,
        default='dist',
        help='The output directory for the generated files. Defaults to "./dist".'
    )
    export_parser.add_argument(
        '--format',
        choices=['json', 'toml', 'txt', 'md', 'embeddings'],
        default=None,
        help='The specific output format to generate. If not provided, all standard formats (json, toml, txt, md) will be generated.'
    )

    args = parser.parse_args()

    if args.command == 'export':
        # Check if source file exists
        if not os.path.exists(args.dict):
            print(f"Error: Source file not found at '{args.dict}'")
            return

        # Create a list of formats to generate
        formats_to_generate = [args.format] if args.format else ['json', 'toml', 'txt', 'md']
        
        print(f"Exporting '{args.dict}' to formats: {', '.join(formats_to_generate)}...")
        compiler.run_export(
            source_file=args.dict,
            output_dir=args.output,
            formats=formats_to_generate
        )
        print("Export complete.")

if __name__ == '__main__':
    main()
