students_db = {
    'grading_scales': {
        'percentage': {
            'Math': {'min': 97, 'max': 100, 'grade': 'A'},
            'Science': {'min': 93, 'max': 96, 'grade': 'A+'},
            'English': {'min': 90, 'max': 92, 'grade': 'A++'},
            'History': {'min': 87, 'max': 89, 'grade': 'B'},
            'Physics': {'min': 83, 'max': 86, 'grade': 'B+'},
        }
    }
}
subject=input("Enter the subject:")
if subject=="Math":
   print("97 to 100 the grade is A")  
elif subject=="Science":
   print("93 to 96 the grade is A+")
elif subject=="English":
   print("90 to 92 the grade is A++")
elif subject=="History":
   print("87 to 89 the grade is B")
elif subject=="physics":
   print("93 to 96 the grade is A+")


  
