#!/bin/bash
lftp -c  "mirror -v ftp://ftp.swpc.noaa.gov/pub/lists/ace /src/solardata/" > /path/to/logs/nasa-solar.log 2>&1
lftp -c  "mirror -v ftp://ftp.swpc.noaa.gov/pub/lists/ace2 /src/solardata/" >> /path/to/logs/nasa-solar.log 2>&1
cd /src/solardata; git add *; git commit -m "`date`";git push cronpush >>  /path/to/logs/nasa-solar.log 2>&1

