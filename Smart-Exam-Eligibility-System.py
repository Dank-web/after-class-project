atten_perc = int(input("Enter Your Attendance Percentage : "))
assignment_score = int(input("Enetr Your Assignment Score : "))
midterm_score = int(input("Enter Your Midterm Score : "))
if atten_perc >= 75:
    if assignment_score >= 40 and midterm_score >= 40:
        print("Congrats! You Eligible For Exams.")
    elif atten_perc >= 90:
     if assignment_score >= 80 and midterm_score < 40:
        print("Congrats! You Are Bearly Eligible For Exams. Focus On Your Midterms As well.")
     elif assignment_score < 40 and midterm_score >= 80:
        print("Congrats! You Are Bearly Eligible For Exams. Focus On Your Assignments As Well.")
     else: 
        print("Error")
    else:
        print("Sorry But You Are Not Eligible For Exams. Try Better Next Time And Focus Better On Midterms And Assignments")
else:
    print("Sorry Your Attendance Is Too Low . Next Time Come To School More.")