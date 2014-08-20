#This test is meant to run after the script is run to generate an html table from the included CSV file. The test will look for the word "Walters" which is the last name of one of the people in the test file.

# The script will be run on the CI server / service using the following arguments for the input & output files
# python csv_to_google_charts_table.py example_csv.csv out.html

import sys

string_to_find = "WaltersXx"

if string_to_find in open("out.html").read():
  print "Found"
else:
  # Raise and error so the build will fail
  raise StandardError
  print "String not found in file"
