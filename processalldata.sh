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

for file in `ls ace/20100308_ace_epam_5m*`; do
    echo processing $file
    ./process.py $file
    #cd - > /dev/null
done
