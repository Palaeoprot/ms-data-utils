import os
import pyopenms
from pathlib import Path
import argparse

def convert_mgf_to_mzml(input_path, output_dir=None):
    """
    Converts MGF files to mzML format using pyopenms.
    Can take a single file or a directory.
    """
    path = Path(input_path)
    
    if path.is_file():
        mgf_files = [path]
        if output_dir is None:
            output_dir = path.parent
    elif path.is_dir():
        mgf_files = list(path.glob("*.mgf"))
        if output_dir is None:
            output_dir = path
    else:
        print(f"Error: {input_path} is not a valid file or directory.")
        return

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not mgf_files:
        print(f"No MGF files found in {input_path}")
        return

    print(f"Processing {len(mgf_files)} files...")

    for mgf_file in mgf_files:
        output_file = output_dir / (mgf_file.stem + ".mzML")
        print(f"Converting {mgf_file.name} -> {output_file.name}...")
        
        try:
            exp = pyopenms.MSExperiment()
            # Use MascotGenericFile for standard MGF
            pyopenms.MascotGenericFile().load(str(mgf_file), exp)
            pyopenms.MzMLFile().store(str(output_file), exp)
            print(f"Successfully converted {mgf_file.name}")
        except Exception as e:
            print(f"Error converting {mgf_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MGF files to mzML using pyopenms.")
    parser.add_argument("input", help="Path to MGF file or directory containing MGF files.")
    parser.add_argument("-o", "--output", help="Output directory (default: same as input).", default=None)
    
    args = parser.parse_args()
    convert_mgf_to_mzml(args.input, args.output)
