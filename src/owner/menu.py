def getSChoiceMainMenu()->int :
  try:
    choice = input("""What would you like to do?
                              1. List orders
                              2. List publishers 
                              3. Add new books
                              4. Remove books
                              5. Generate reports
                              6. Search books
                              7. Pay publisher
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=7:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")
  
def getSChoiceReports()->int :
  try:
    choice = input("""What would you like to do?
                              1. 
                              2. List publishers 
                              3. Add new books
                              4. Remove books
                              5. Generate reports
                              6. Search books
                              7. Pay publisher
                              0. return to previous menu 
                      Choice: """)
    if int(choice) >= 0 and int(choice) <=7:
      return int(choice)
    else:
      print ("Invalid choice")                  
  except:
    print("Not a valid integer")