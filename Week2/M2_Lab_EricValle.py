# Author: Eric Valle
# File Name: GPA_Classification.py
# Description: The program will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll


studentLName = input("What is the student's last name: ")
#while student-name!= 'ZZZ'
while studentLName != 'ZZZ':
    studentFName = input("What is the student's first name: ")
    studentGPAstr = input("What is the student's GPA: ")
    studentGPA = float(studentGPAstr)

    if studentGPA >= 3.5:
        print("Student has made the Dean's List")
    elif studentGPA >= 3.25:
        print("Student has made the Honor Roll")
    
    studentLName = input("What is the student's last name: ")