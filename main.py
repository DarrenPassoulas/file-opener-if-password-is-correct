import time


password = "yes"

user_name = input("Please enter user name:\n")

file = open("textd")

sec = 10


def verification():
  trys = 0
  a = 0
  
  while (a == 0):
    while trys < 3:
      trys += 1
      password_attemp = input("Hi! " + str(user_name)+" please enter correct password to open text document, 3 attempts allowed \n You have "+ str(trys)+ " attempts made:")
      if password_attemp == (password):
        print(file.read())
        a = 1
    
        break
        #exit("Thank you")
        
      if password_attemp != (password):
        print("wrong")
        if trys == 3:
          print("You have made too many attempts please wait 10 seconds")
          for i in range (1, 11):
            print(i, end= " seconds lapsed \r")
            time.sleep(1)
          trys = 0
      

      
verification()