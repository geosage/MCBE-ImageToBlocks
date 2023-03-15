check = True


#This will generate the commands for the other methods
def commandgen():
    print("Generate commands here")


#Typing the commands into their chat
def fillgen():
    print("This will type it into their chat")


#This will turn the commands into an mcfunction
def functiongen():
    print("This will generate an mcfunction")


#This will ask which import type they want
def mcbequestion():
    importtype = input("How would you like to import?\n[1]: mcfunction\n[2]: fill commands")
    while check == True:
        if importtype == 1:
            functiongen()
            check = False
        if importtype == 2:
            fillgen()
            check = False
        else:
            importtype = input("Please pick 1 or 2.")



