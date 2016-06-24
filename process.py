#!/usr/bin/env python

# ==================================================================================================================
# *ace_epam_5m.txt
#                      5-minute averaged Real-time Differential Electron and Proton Flux 
# 
#                Modified Seconds ---------------------------- Differential Flux ---------------------------
# UT Date   Time  Julian  of the  ----- Electron -----   ------------------- Protons keV -------------------   Anis.
# YR MO DA  HHMM    Day    Day    S    38-53   175-315   S    47-68   115-195   310-580   795-1193 1060-1900   Index
#-------------------------------------------------------------------------------------------------------------------
#2016 06 08  0000   57547       0  0  4.31e+02  1.98e+01  0  1.61e+03  6.54e+01  6.00e+00  5.39e-01  1.68e-01  -1.00
#
# ==================================================================================================================
# *ace_mag_1m.txt
#              1-minute averaged Real-time Interplanetary Magnetic Field Values 
# 
#                 Modified Seconds
# UT Date   Time  Julian   of the   ----------------  GSM Coordinates ---------------
# YR MO DA  HHMM    Day      Day    S     Bx      By      Bz      Bt     Lat.   Long.
#2008 11 02  0000   54772       0    0     0.0    -3.8     2.3     4.4    31.8   270.1
#
# ==================================================================================================================
# *_ace_sis_5m.txt
# 5-minute averaged Real-time Integral Flux of High-energy Solar Protons
# 
#                 Modified Seconds
# UT Date   Time   Julian  of the      ---- Integral Proton Flux ----
# YR MO DA  HHMM     Day     Day       S    > 10 MeV    S    > 30 MeV
#--------------------------------------------------------------------
#2008 11 02  0000    54772       0      0    2.00e+00    0    1.38e+00
#2008 11 02  0005    54772     300      0    1.98e+00    0    1.39e+00
#
# ==================================================================================================================
# *_ace_swepam_1m.txt
#   1-minute averaged Real-time Bulk Parameters of the Solar Wind Plasma
# 
#                Modified Seconds   -------------  Solar Wind  -----------
# UT Date   Time  Julian  of the          Proton      Bulk         Ion
# YR MO DA  HHMM    Day     Day     S    Density     Speed     Temperature
#-------------------------------------------------------------------------
#2008 11 02  0000   54772       0    0        0.8      440.3     5.11e+04
#
# ==================================================================================================================
# *_ace_epam_1h.txt
#                      Hourly Averaged Real-time Differential Electron and Proton Flux 
# 
#                Modified Seconds ---------------------------- Differential Flux ---------------------------
# UT Date   Time  Julian  of the  ----- Electron -----   ------------------- Protons keV -------------------  Anis.
# YR MO DA  HHMM    Day    Day    S    38-53   175-315   S    47-68   115-195   310-580   761-1220 1060-1900  Index
#------------------------------------------------------------------------------------------------------------------
#2007 11 01  0000   54405       0  0  6.33e+02  2.65e+01  0  1.19e+03  1.73e+01  2.15e+00  5.42e-01  1.65e-01   0.15
#
# ==================================================================================================================
# *_ace_mag_1h.txt
#              Hourly Averaged Real-time Interplanetary Magnetic Field Values 
# 
#                 Modified Seconds
# UT Date   Time  Julian   of the   ----------------  GSM Coordinates ---------------
# YR MO DA  HHMM    Day      Day    S     Bx      By      Bz      Bt     Lat.   Long.
#------------------------------------------------------------------------------------
#2007 11 01  0000   54405       0    0    -2.3     1.0    -0.5     2.5   -12.3   156.8
#
# ==================================================================================================================
# *_ace_sis_1h.txt
# Hourly Averaged Real-time Integral Flux of High-energy Solar Protons
# 
#                 Modified Seconds
# UT Date   Time   Julian  of the     ---- Integral Proton Flux ----
# YR MO DA  HHMM     Day     Day      S    > 10 MeV    S    > 30 MeV
#-------------------------------------------------------------------
#2007 11 01  0000   54405       0      0    1.97e+00    0    1.38e+00
#
# ==================================================================================================================
# *_ace_swepam_1h.txt
#   Hourly Averaged Real-time Bulk Parameters of the Solar Wind Plasma
# 
#                Modified Seconds   -------------  Solar Wind  -----------
# UT Date   Time  Julian  of the          Proton      Bulk         Ion
# YR MO DA  HHMM    Day     Day     S    Density     Speed     Temperature
#-------------------------------------------------------------------------
#2007 11 01  0000   54405       0    0        1.4      402.7     4.02e+04
#
# ==================================================================================================================

import sys
import os.path
import csv
import time
from calendar import timegm

filetypeinfo = {
    'ace_epam_5m' : {
        'colhdrs' : ['timestamp', 'julian_day', 'electron_flux_status', 'electron_flux_38-53', 'electron_flux_175-315',
                     'proton_flux_status', 'proton_flux_47-68', 'proton_flux_115-195', 'proton_flux_310-580',
                     'proton_flux_795-1193', 'proton_flux_1060-1900', 'anisotropy_index'],
    },
    'ace_epam_1h' : {
        'colhdrs' : ['timestamp', 'julian_day', 'electron_flux_status', 'electron_flux_38-53', 'electron_flux_175-315',
                     'proton_flux_status', 'proton_flux_47-68', 'proton_flux_115-195', 'proton_flux_310-580',
                     'proton_flux_795-1193', 'proton_flux_1060-1900', 'anisotropy_index'],
    },
    'ace_mag_1m' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status', 'bx', 'by', 'bz', 'bt', 'lat', 'lon'],
    },
    'ace_mag_1h' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status', 'bx', 'by', 'bz', 'bt', 'lat', 'lon'],
    },
    'ace_sis_5m' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status_10', 'proton_flux_10', 'status_30', 'proton_flux_30'],
    },
    'ace_sis_1h' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status_10', 'proton_flux_10', 'status_30', 'proton_flux_30'],
    },
    'ace_swepam_1m' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status', 'proton_density', 'bulk_speed', 'ion_temperature'],
    },
    'ace_swepam_1h' : {
        'colhdrs' : ['timestamp', 'julian_day', 'status', 'proton_density', 'bulk_speed', 'ion_temperature'],
    },
}

if len(sys.argv) != 2:
    print 'Usage: %s txtfile' % sys.argv[0]
    sys.exit()

filefront = sys.argv[1].split('.', 1)[0]
filetype = filefront.split('_', 1)[1]

#outfilename = filefront + ".csv"
outfilename = "output/" + filefront.split("/", 1)[1] + ".csv"
#print '  File out name: %s' % outfilename

if filetype == "ace_loc_1h":
    print "    Skipping"
    sys.exit()
elif filetype not in filetypeinfo.keys():
    print "I don't know how to deal with the file type of %s (based on filename)" % filetype
    sys.exit()

with open(sys.argv[1], 'rb') as infile, open(outfilename, "wb") as outfile:
    logdata = infile.readlines()
    # header
    for hf in filetypeinfo[filetype]['colhdrs']:
        outfile.write("%s," % hf)
    outfile.write("\n")
    for row in logdata:
        # first char of [:#] means a comment
        if row.startswith((':', '#')):
            continue

        fields = row.split()

        # parse time fields
        year = fields[0]
        month = fields[1]
        day = fields[2]
        hh = fields[3][0:2]
        mm = fields[3][2:]
        #print row
        #print hh
        #print mm
        #print "-------------------------------------------"
        #sys.exit()
        julian_day = fields[4]
        seconds_of_day = int(fields[5]) # ignored, as we have minute data
        ss = "%02d" % (seconds_of_day - ((3600 * int(hh)) + (60 * int(mm))))
        timestamp = time.strptime(year+month+day+hh+mm+ss,"%Y%m%d%H%M%S")
        text_timestamp = time.strftime("%b %d %Y %H:%M:%S", timestamp)
        outfile.write("%s," % text_timestamp)
        outfile.write("%s," % julian_day)
        for field in fields[5:]:
            outfile.write("%s," % field)
        outfile.write("\n")

#    logdata = csv.reader(csvinfile, delimiter=',', quotechar='"')
