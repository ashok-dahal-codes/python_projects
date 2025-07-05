#initialize variable for attempts and right password
attempts = 0
right_password = "ashok123"
#start a while loop for condition of less than 3
while attempts < 3:
#take user input for the password they know
    password = input("Enter password: ")
    if password == right_password:
#write a condition for checking the condition if the pasword is equal to the input
        print("you have entered the correct password")
        break
    else:
#write a else condition of password is incorrect with increasing of attempt with 1 at a time 
        attempts += 1
    if attempts == 3:
        print("no more attempts left")
#write another if statement when attempt is greater than 3 that prints no more attempts left and exit the loop
        
    
    
