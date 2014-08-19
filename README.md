csv_to_google_charts_table
==========================
###Overview
This python application will accept input from a CSV file and generate a text file that will create a sortable html table using google charts that has been populated with the data in the csv file.

###Command line usage:
python csv_to_google_charts_table.py <input_file_name.csv> <output_file_name.html>
This will output a file that contains a sortable HTML table of the data from the csv file passed to the application by the user.	

###Planned Features
- String / Integer detection for the data rows (they are currently all treated as strings)
- File type validation
- Error handling
