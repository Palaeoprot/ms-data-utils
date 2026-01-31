# Mass Spectrometry Data Conversion Manual

This manual describes how to use the tools in this repository for converting mass spectrometry data.

## 1. Thermo RAW to mzML
We use **ThermoRawFileParser** for high-performance conversion of Thermo Fisher RAW files.

### Configuration
The default script `scripts/convert_raw.py` applies the following parameters:
- **Format**: Indexed mzML (`-f 2`)
- **Compression**: Gzip (`-g`)
- **Noise**: Included (`-N`)

### Usage
```bash
python3 scripts/convert_raw.py <input_path> -o <output_directory>
```
The `<input_path>` can be a single `.raw` file or a directory containing multiple files.

---

## 2. MGF to mzML
Converting Mascot Generic Format (MGF) files is handled by **pyopenms**.

### Usage
```bash
python3 scripts/convert_mgf.py <input_path> [-o <output_directory>]
```
If no output directory is specified, it will create the `.mzML` files in the same location as the source files.

---

## 3. Requirements & Environment
- **Python 3.8+**
- **pyopenms**: Required for MGF conversion.
- **ThermoRawFileParser**: Required for RAW conversion. The script expects the binary at `/home/matthew/bin/ThermoRawFileParser/ThermoRawFileParser`.

---

## Troubleshooting
- **Permission Errors**: If `run_thermo_parser.sh` fails, ensure it has execute permissions:
  ```bash
  chmod +x scripts/run_thermo_parser.sh
  ```
- **ModuleNotFoundError**: Ensure you have installed the requirements:
  ```bash
  pip install -r requirements.txt
  ```
