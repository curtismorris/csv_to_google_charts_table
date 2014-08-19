#This test is meant to run after the script is run to generate an html table from the included CSV file. The test will look for the word "Walters" which is the last name of one of the people in the test file.

import sys

string_to_search = "The man's name is John Walters and he lives on 123 Fake Street"
string_to_find = "thes"

search_result = string_to_search.find(string_to_find)

if search_result > 0:
  print"Found"
else:
  print"Not Found"
