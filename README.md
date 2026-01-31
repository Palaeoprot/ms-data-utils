# Mass Spectrometry Data Utilities (ms-data-utils)

A collection of scripts and tools for converting and pre-processing mass spectrometry data files.

## Features
- **RAW to mzML**: Batch convert Thermo Fisher `.raw` files using `ThermoRawFileParser`.
- **MGF to mzML**: Convert Mascot Generic Format `.mgf` files using `pyopenms`.
- **Standardized Output**: All converters are configured for indexed mzML with optional gzip compression and noise retention.

## Quick Start

### 1. Installation
Ensure you have the required Python libraries:
```bash
pip install -r requirements.txt
```

### 2. Convert MGF files
```bash
python3 scripts/convert_mgf.py /path/to/mgf_folder/ -o /path/to/output/
```

### 3. Convert RAW files
```bash
python3 scripts/convert_raw.py /path/to/raw_folder/ -o /path/to/output/
```

## Documentation
For detailed instructions and troubleshooting, see [docs/MANUAL.md](docs/MANUAL.md).
