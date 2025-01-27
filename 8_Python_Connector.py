
import mysql.connector

print ("Starting Katrin_Jogi_A8.py")

mydb = mysql.connector.connect(
    user = 'k',
    passwd = ' ',
    database ='EStore',
    host = '127.0.0.1',
    allow_local_infile = 1
)

print(mydb)
myc = mydb.cursor()   # myc name short for "my cursor"

#reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 

#use the PDA database Estore, that I have been working on throughout the quarter.
myc.execute("use EStore")

'''while loop to update - Add, Edit, Delete, Seller table. The program 
allows the user repeated updates and will quit once the user input is No
'''
while True:

    #Request for user input - Any updates to the Seller table?
    userInput2 = str(input("Would you like to update a Seller? Please pick yes or no: ")).lower()
    
    #If yes, continue to Add, Edit, Delete
    if userInput2 == "yes":
        
        #Request for user input - Add, Edit or Delete
        userInput_Question = str(input("Would you like to Add, Delete or Edit Seller?: ")).lower()

        #If user picks Edit, continue to Edit informtion for an existing Seller
        if userInput_Question == "edit":
            
            #Request for user input - pick the Seller Id to be updated
            userInput1 = int(input("Please enter the seller's sID: "))
            #Printout of existing
            myc.execute("Select * From Seller S Where S.sID = %s", (userInput1,))
            for x in myc:
                print(x)

            #Request for user input - pick the Variable to be updated
            userInput3 = str(input(""""Please enter the attribute you would like to change. 
            Please pick: password, name, address, email: """))
            
            #If user picks password, continue to change the password
            if userInput3 == "password":
                #Request for user input - new password
                userInput4 = str(input("Please enter the new password, up to 20 characters: "))
                myc.execute("""
                            Update Seller S 
                            SET password = %s
                            Where S.sID = %s""", (userInput4, userInput1))
                #printout of the updated information
                print("Please see the update: ")
                myc.execute("Select * From Seller S Where S.sID = %s", (userInput1,))
                for x in myc:
                    print(x)
                #Return to the beginning of the loop
                continue
            
            #If user picks name, continue to change the name
            elif userInput3 == "name":
                #Request for user input - new name
                userInput5 = str(input("Please enter the new name: "))
                myc.execute("""
                            Update Seller S 
                            SET sname = %s 
                            Where S.sID = %s""", (userInput5, userInput1))
                #printout of the updated information
                print("Please see the update:")
                myc.execute("Select * From Seller S Where S.sID = %s", (userInput1,))
                for x in myc:
                    print(x)
                #Return to the beginning of the loop
                continue
            
            #If user picks address, continue to change the address
            elif userInput3 == "address":
                #Request for user input - new address
                userInput6 = str(input("Please enter the new address: "))
                myc.execute("""
                            Update Seller S
                            SET saddress = %s 
                            Where S.sID = %s""", (userInput6, userInput1,))
                #printout of the updated information
                print("Please see the update:")
                myc.execute("Select * From Seller S Where S.sID = %s", (userInput1,))
                for x in myc:
                    print(x)
                #Return to the beginning of the loop
                continue
            
            #If user picks email, continue to change the email
            elif userInput3 == "email":
                #Request for user input - new email
                userInput7 = str(input("Please enter the new email: "))
                myc.execute("""
                            Update Seller S
                            SET semail = %s 
                            Where S.sID = %s""", (userInput7,userInput1,))
                #printout of the updated information
                print("Please see the update:")
                myc.execute("Select * From Seller S Where S.sID = %s", (userInput1,))
                for x in myc:
                    print(x)
                #Return to the beginning of the loop
                continue
            
            #If user input is invalid, they are returned to the beginning of the loop
            else:
                print("This is not a valid response")
                #Return to the beginning of the loop
                continue
                    

        #If user picks Add, continue to add a new Seller
        if userInput_Question == "add":
            #the seller Id is generated by the system
            myc.execute("Select max(S.sid) from Seller S")
            for x in myc:
                print("The sId is", x[0]+1)
            newsID = x[0]+1
            #Request for user input - enter password, name, address, email
            userInputAdd_2 = str(input("Please enter the password: "))
            userInputAdd_3 = str(input("Please enter the name: "))
            userInputAdd_4 = str(input("Please enter the address: "))
            userInputAdd_5 = str(input("Please enter the email: "))
            myc.execute("Insert Into Seller Values (%s,%s,%s,%s,%s)", (newsID, userInputAdd_2, userInputAdd_3, userInputAdd_4, userInputAdd_5,))
            #printout of the updated information
            print("Please see the update:")
            myc.execute("Select * From Seller S Where S.sID = %s", (newsID,))
            for x in myc:
                print(x)
            #Return to the beginning of the loop
            continue

        #If user picks Delete, continue to delete an existing Seller
        if userInput_Question == "delete":
            #Request for user input - Seller Id to be deleted
            userInputDelete_1 = int(input("Please enter the sID of the Seller to be deleted: "))
            myc.execute("Delete From Seller S Where S.sID = %s", (userInputDelete_1,))
            #Confirmation of deletion
            print("Seller has been Deleted.")
            #Return to the beginning of the loop
            continue
        
        #If user input is invalid, they are returned to the beginning of the loop
        else:
            print("This is not a valid response")
            #Return to the beginning of the loop
            continue
    
    #If no, user is thanked and the program exits
    #any changes. 
    if userInput2 == "no":
        print("Thank you for using our database.")
        break
    
    #If user input is invalid, they are returned to the beginning of the loop
    else:
        print("This is not a valid response")
    #Return to the beginning of the loop
    continue

mydb.commit()
mydb.close()
