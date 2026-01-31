#!/bin/bash
# Wrapper for ThermoRawFileParser
# Default path to binary on this system
THERMO_PARSER="/home/matthew/bin/ThermoRawFileParser/ThermoRawFileParser"

if [ ! -f "$THERMO_PARSER" ]; then
    echo "Error: ThermoRawFileParser not found at $THERMO_PARSER"
    exit 1
fi

"$THERMO_PARSER" "$@"
