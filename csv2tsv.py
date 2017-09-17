#/usr/bin/env python

import sys
import csv
from datetime import datetime

''' Assume that argument order is:
	1. Name of csv
	2. (Optional) Name of output - if left blank, file will be named csvName_timestamp

	Outputs the given .csv file into a .tsv using an optional given name.
'''
if(len(sys.argv) < 2):
	print "Not enough arguments (minimum 1). \n\t(1) Name of csv \n\t(Optional)(2) Name of output"
	exit(0)

# Assume that ".csv" only ever occurs at the end of the file
input_csv = open(sys.argv[1], "r")
output_file = open(sys.argv[1].replace(".csv", "") + "_" + datetime.now().strftime('%Y%m%d-%H%M%S') + ".tsv" if len(sys.argv) < 3 else sys.argv[2], "w")

csv.writer(output_file, dialect='excel-tab').writerows(csv.reader(input_csv))
