# Import the newere version of the print fuction so the sep argument will work when formatting my strings
from __future__ import print_function
import csv
import sys
import argparse

# Parse command line argument for the input file
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("out_file")
args = parser.parse_args()
name = args.input_file
out_file = args.out_file


# Name of the input file provided by the user in the arguments when they ran this program
in_file  = open(name, "rb")

# Name of the output file provided by the user in the arguments when they ran this program
out_file  = open(out_file, 'w')

# Import the csv file
reader = csv.reader(in_file)


# Assign the column titles to the col_head variable. Note that the reader will now start on the first line of data rather than the column titles
col_titles = reader.next()


# Store the first part of the google charts code in a multi line string
google_chart_code = """
<script type="text/javascript" src="https://www.google.com/jsapi"></script>

    <script type="text/javascript">



google.load('visualization', '1', {packages:['table']});

      google.setOnLoadCallback(drawTable);

      function drawTable() {

        var data = new google.visualization.DataTable();
"""

# Store the second part of the google charts code in a multi line string
google_chart_code_bottom = """
]);



        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true});

      }

    </script>

      <div id='table_div'></div>
"""

# Write first part of google code to file
out_file.write(google_chart_code)

#Write the colum titles to the output file in string format * I need to write a test to determine if they should be int or str * for the time being they are all being handled as strings
for word in col_titles:
	print("data.addColumn('string', '",word, "');",sep='',file=out_file)

# Write Google chart code to close out rows
print("data.addRows([",file=out_file)

# Cycle through each row of the CSV starting at row 2 and format the data to work with google charts a loop would be better to use here..
# Since row is already a list the data format matches what Google charts expects minus a comma
for row in reader:
    print(
    row,
    ",",
    sep='',
    file=out_file
    )
# Write the last bit of Google chart code to the output file
out_file.write(google_chart_code_bottom)

# Close the csv file
in_file.close()

# Close the output file
out_file.close()


# Format that google charts expects for table output
#  ['A', 'A', 1, 'A', 'A', 'A', 'A', 'A'],
