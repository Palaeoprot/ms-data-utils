import os
import subprocess
import argparse
from pathlib import Path

def convert_raw_to_mzml(input_path, output_dir, wrapper_script):
    """
    Converts Thermo RAW files to mzML using ThermoRawFileParser.
    """
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if input_path.is_file():
        files = [input_path]
    elif input_path.is_dir():
        files = list(input_path.glob("*.raw"))
    else:
        print(f"Error: {input_path} is not valid.")
        return

    for raw_file in files:
        print(f"Converting {raw_file.name}...")
        
        # Flags:
        # -f 2 : Indexed mzML
        # -g : Gzip output
        # -N : Include Noise
        cmd = [
            str(wrapper_script),
            "-i", str(raw_file),
            "-o", str(output_dir),
            "-f", "2",
            "-g",
            "-N"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Successfully converted {raw_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {raw_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Thermo RAW files to mzML.")
    parser.add_argument("input", help="Path to RAW file or directory.")
    parser.add_argument("-o", "--output", required=True, help="Output directory.")
    parser.add_argument("--wrapper", help="Path to run_thermo_parser.sh", 
                        default=str(Path(__file__).parent / "run_thermo_parser.sh"))
    
    args = parser.parse_args()
    convert_raw_to_mzml(args.input, args.output, args.wrapper)
