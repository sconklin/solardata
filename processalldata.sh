#!/bin/bash

# ace
# *_ace_epam_5m.txt
# *_ace_mag_1m.txt
# *_ace_sis_5m.txt
# *_ace_swepam_1m.txt

# ace2
# *_ace_epam_1h.txt
# *_ace_mag_1h.txt
# *_ace_sis_1h.txt
# *_ace_swepam_1h.txt

OUTPUT_DIR="output"
mkdir -p ./$OUTPUT_DIR

for file in `ls ace/*.txt`; do
    echo processing $file
    ./process.py $file
done
