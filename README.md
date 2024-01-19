# Grade-Management-Program
This Python script is a simple program for recording and storing student grades in a CSV file.
Here's a breakdown of the key components:

File Name Constant:
The script defines a constant FILENAME to store the name of the CSV file as "Gardes.csv."

Input Functions:
There are three functions: get_StudentName(), get_Midterm(), and get_Final().
These functions prompt the user for input (student name, midterm grade, and final grade) and ensure that the entered grades are greater than zero.

Main Function:
The main() function serves as the main entry point for the program.
It initializes an empty list called DataList to store student data.
The program enters a loop to allow the user to input multiple sets of student data.
After obtaining the student's name, midterm grade, and final grade, it calculates the total grade and displays it.
The user's data is stored in a list called Data, which is then appended to the DataList.
The loop continues until the user chooses not to enter more data.
Finally, the collected data is written to a CSV file named "Gardes.csv."

CSV File Writing:
The script uses the csv.writer to write the collected data in the DataList to the specified CSV file.

Execution:
The if __name__ == "__main__": block ensures that the main() function is executed when the script is run.

Overall, this script provides a simple way to gather and store student grades in a CSV file, making it easy to manage and analyze the data.






