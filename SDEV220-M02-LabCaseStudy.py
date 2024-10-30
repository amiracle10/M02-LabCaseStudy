# author: Alex Miracle
# SDEV220-M02-LabCaseStudy
# This app accpets student names and GPAs, determines if they quality for the dean's list or
# Honor Roll, and stops processing with 'ZZZ' is entered as the last name. 

def process_student_records():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            print("Goodbye!")
            break

        first_name = input("Enter the student's first name: ")
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Please enter a valid GPA.")
            continue


        if gpa>= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else: 
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

process_student_records()