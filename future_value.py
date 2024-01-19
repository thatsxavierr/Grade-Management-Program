#!/usr/bin/env python3
# Defining the CSV file name
import csv
FILENAME = "Gardes.csv"

def get_StudentName():
    StudentName = input("Enter Your Name:\t")                    
    return StudentName

def get_Midterm():
    while (MidtermGrade := float(input("Enter Midterm Grade:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return MidtermGrade
          
def get_Final():
    while (FinalGrade := float(input("Enter Final Grade:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return FinalGrade

        
def main():
    # display a welcome message
    print("Grade example Program")
    print()
     ## Create an empty List
    DataList=[]
    
    more = "y"
    while more.lower() == "y":
        StudentName= get_StudentName()
        MidtermGrade = get_Midterm()
        FinalGrade = get_Final()
        
        TotalGrade = round(((MidtermGrade+FinalGrade) / 2), 2)
        print("Total Grade: " , TotalGrade)
        print()
## Add to the list the user inputs values
        Data = [StudentName, MidtermGrade, FinalGrade,TotalGrade ]
        DataList.append(Data)
        
        more = input("More entries? (y or n): ")
## Write the data in the list into the CSV file
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(DataList) 
    
    print("Bye!")

if __name__ == "__main__":
    main()
