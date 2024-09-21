from art import *
students = [] #holding all student information
student_unique_id = 0 # id for all student
subjects = ["Python", "MySQL", "Flask", "Api", "Data Analytics"]

#++++++++++++++++++++++++++ === === === === === === === === (Adding New Student) === === === === === === === === === +++++++++++++++++++++++++++#
def adding_new_student(name)->dict:
    global student_unique_id
    student_unique_id += 1
    student = {"id": student_unique_id, "name": name, "subject": []}
    student_list = []
    
    total_score = 0
    for subject in subjects:
        score = float(input(f"What did '{name} score in '{subject}'? \n"))
        subject_info = {"name": subject, "score": score}
        student_list.append(subject_info)
        total_score += score
        
    student["subject"] = student_list
    student["total_score"] = total_score
    student["grade"] = calculating_grade(total_score)
    student["result"] = result(student["grade"])
    return student

#++++++++++++++++++++++++++ === === === === === === === === (Calculating Grades) === === === === === === === === === +++++++++++++++++++++++++++#
def calculating_grade(total_score):
    percent = (total_score / 400) * 100
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"
    
#++++++++++++++++++++++++++ === === === === === === === === (Checking Result) === === === === === === === === === +++++++++++++++++++++++++++#
def result(grade):
    if grade != "F":
        return "Pass"
    else:
        return "Fail"

#++++++++++++++++++++++++++ === === === === === === === === (Checking if Student Exist) === === === === === === === === === +++++++++++++++++++++++++++#
def student_exist(students, id:int):
    for student in students:
        if student["id"] == id:
            student_name = student["name"]
            print(f"Student with ID {id} is {student_name}")
            return True
    print(f"Student with ID {id} does not exist. Try searching again...\n")
    return False

#++++++++++++++++++++++++++ === === === === === === === === (Viewing Individual Fresh Man Report) === === === === === === === === === +++++++++++++++++++++++++++#
def view_report(students, id:int):
    if student_exist(students, id):
        subject_list = ""
        for subject in subjects:
            subject_list = f"{subject}  |   {subject_list}"
            
        print(f"Student_Name   |   {subject_list}  Score   |   Grade   |   Result  ")
        print("=" * 112)
        for student in students:
            if student["id"] == int(id):
                subject = {
                    tutee["name"]: tutee["score"]
                    for tutee in student["subject"]
                }
                subject_score_list = ""
                for sub in subjects:
                    subject_score_list = str(subject.get(sub,0)).rjust(len(sub)) + f"   |   {subject_score_list}"
                    
                student_name = str(student["name"]).ljust(15)
                total_score = str(student["total_score"]).rjust(6)
                student_grade = str(student["grade"]).rjust(6)
                result = str(student["result"]).rjust(6)
                                                        
                print(f"{student_name:<15}| {subject_score_list}  {total_score:<6}    | {student_grade:<6}    | {result:<7}")
                print("=" * 112)

#++++++++++++++++++++++++++ === === === === === === === === (Editing Student Report)=== === === === === === === === ===  +++++++++++++++++++++++++++#
def editing_student_report(students, id:int):
    if student_exist(students, id):
        for student in students:
            if student['id'] == id:
                new_name = input(f"Enter new name for '{student['name']}' OR (press enter to keep current name): ").capitalize()
                if new_name:
                    student["name"] = new_name
                student_subject = student["subject"]                
                for subject in student_subject:
                    score = subject["score"]
                    new_score =  input(f"Enter new score for '{subject['name']}' (current score is '{score}') OR (press enter to keep current score): ")
                    if new_score:
                        subject["score"] = float(new_score)
                        
                new_total = student["total_score"] = sum(subj["score"] for subj in student_subject)
                student_new_total = float(new_total)
                student["grade"] = calculating_grade(student_new_total)
                student["result"] = result(student["grade"])
                print(f"\nRecord for student ID {id} has been updated successfully. Check Report to confirm.")
                break

#++++++++++++++++++++++++++ === === === === === === === === (Viewing All Student Report)=== === === === === === === === ===  +++++++++++++++++++++++++++#
def view_student_db(students):
    subject_list = ""
    for subject in subjects:
        subject_list = f"{subject}  |   {subject_list}"
    print(f"ID  |  Student_Name  |   {subject_list} Score   |   Grade   |   Result  ")
    print("=" * 112)
    for student in students:
        student_id = student["id"]
        subject = {
            tutee["name"]: tutee["score"]
            for tutee in student["subject"]
        }
        
        student_name = str(student["name"]).ljust(15)
        
        subject_score_list = ""
        for sub in subjects:
            subject_score_list = str(subject.get(sub,0)).rjust(len(sub)) + f" |  {subject_score_list}"
      
            total_score = str(student["total_score"]).rjust(6)
            student_grade = str(student["grade"]).rjust(6)
            result = str(student["result"]).rjust(6)
                                                
        print(f"{student_id:<3} | {student_name:<15}| {subject_score_list} {total_score:<6}    | {student_grade:<6}    | {result:<7}")
        print("=" * 112)
    
#++++++++++++++++++++++++++ === === === === === === === === (Student Statistics)=== === === === === === === === ===  +++++++++++++++++++++++++++#
def student_statistics(students):
    # checking highest to lowest  score
    highest_to_lowest = sorted(students, key=lambda n: n["total_score"], reverse=True)
    # displaying highest_to_lowest result
    print(f"id  |   Student_Name   |   Total Score   |   Grade   |   Result  ")
    print("=" * 60)
    for student in highest_to_lowest:
        student_id = student["id"]
        student_name = student["name"].ljust(15)
        total_score = str(student["total_score"]).rjust(12)
        student_grade = student["grade"].rjust(6)
        student_result = student["result"].rjust(7)
        
        print(f"{student_id:<3} |   {student_name:<15}  |   {total_score:<12}    |   {student_grade:<6} |   {student_result:<7}")
        print("=" * 60)
#++++++++++++++++++++++++++ === === === === === === === === (Moment of Truth: Implementing the code)=== === === === === === === === ===  +++++++++++++++++++++++++++#

art_output = text2art("Student - Grading - System", font="bubble")
print(art_output)

while True:
    print(
        """
        {1}-->   ADD NEW STUDENT AND THEIR SCORE            <-{1}
        {2}-->   VIEW INDIVIDUAL REPORT                     <-{2}
        {3}-->   EDIT STUDENT RECORD                        <-{3}
        {4}-->   VIEW DATABASE OF ALL STUDENT AND REPORT    <-{4}
        {5}-->   GENERATE CLASS WIDE STATISTICS             <-{5}
        {0}-->   Exit\n 
"""
)#+✅done
    user_input = int(input("\nChoose from (0-4): "))
    # comparison
    if user_input == 1:
        student_name = input("Enter Student Name: ").capitalize()
        stud = adding_new_student(student_name)
        students.append(stud)
        print(f"Registration for {student_name} Successful. \n'{student_name}' ID is '{student_unique_id}'. Do not share with anyone")
        
    elif user_input == 2:
        student_id = int(input("Enter Student ID: "))
        view_report(students, student_id)
        
    elif user_input ==3:
        student_id = int(input("Enter Student ID to edit..: "))
        editing_student_report(students, student_id)

    elif user_input == 4:
        view_student_db(students)
    elif user_input == 5:
        student_statistics(students)
        
    elif user_input == 625:
            user_warning  = int(input("I need to verify who you are: (if you're ready press (1) / else press (0) to exit the app: "))
            if user_warning == 1:
                asking = input("Who are you: ").upper()
                if asking == "MASTER":
                    print("Welcome Back master what will you like to do today")
                    asking_master = input("Are you here to see the DATA STRUCTURE  of your student CLI app: if yes press (Y) else (N): ").lower()
                    if asking_master == "y":
                        print(f"Here is the DATA STRUCTURE (MASTER)-> \n {students}")
                    else:
                        print("See You Next Time (MASTER)")
                        break
                elif asking == "PROCESS GUY":
                    print("Just a step away to see my DATA STRUCTURE, (if you're ready proceed to the next line... \n)")
                    y_or_n = input("If you're ready press (Y) else (N): ").lower()
                    if y_or_n == "y":
                        print(f"\n {students}")
                    else:
                        break
                else:
                    print("The Program is unavailable in your region. Talk with my master 💻 🎶(NULL) \n BYE... 👋👋👋")
                    break
            else:
                break
    elif user_input == 0:
        print("See you next time 💻.\n Bye...👋👋👋 ")
        break
    else:
        print("\nInvalid Input... Choose from (0-4)")