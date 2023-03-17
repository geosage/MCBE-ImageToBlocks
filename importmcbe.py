


#This will generate the commands for the other methods
def commandgen(imagenames):
    count = 0
    print("Generate commands here")
    for i in imagenames:
        i = i.replace('.png', '')
        if i[:9] == "concrete ":
            a = i.split()
            b = a[1]
            i = f'concrete ["color":"{b}"]'
        elif i[:9] == "concrete_":
            a = i.split()
            b = a[1]
            i = f'concrete_powder ["color":"{b}"]'
        elif i[:9] == "stained_h":
            a = i.split()
            b = a[1]
            i = f'stained_hardened_clay ["color":"{b}"]'

        imagenames[count] = i
        count += 1
    imagenames.reverse()
    print(imagenames)
    print(len(imagenames))


#This will turn the commands into an mcfunction
def functiongen():
    print("This will generate an mcfunction")


#Typing the commands into their chat
def commandfill():
    print("This will type it into their chat")


#This will ask which import type they want
def mcbequestion(imagenames, num_cols, num_rows):
    commandgen(imagenames)
    importtype = input("How would you like to import?\n[1]: mcfunction\n[2]: fill commands\n")

    check = True
    while check == True:
        if importtype == "1":
            functiongen()
            check = False
        elif importtype == "2":
            commandfill()
            check = False
        else:
            importtype = input("Please pick 1 or 2.")



