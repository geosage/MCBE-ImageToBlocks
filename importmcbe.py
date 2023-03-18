import pyautogui
import time

#This will generate the block names for the other methods
def blockgen(imagenames):
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
        elif i[:3] == "log":
            a = i.split()
            b = a[1]
            i = f'wood ["wood_type":"{b}"]'
        elif i[:6] == "planks":
            a = i.split()
            b = a[1]
            i = f'planks ["wood_type":"{b}"]'
        elif i[:5] == "dpris":
            i = f'prismarine ["prismarine_block_type":"dark"]'
        elif i[:7] == "redsand":
            a = i.split()
            b = a[1]
            i = f'red_sandstone ["sand_stone_type":"{b}"]'
        elif i[:9] == "fsandstone":
            a = i.split()
            b = a[1]
            i = f'sandstone ["sand_stone_type":"{b}"]'
        elif i[:6] == "stonef":
            a = i.split()
            b = a[1]
            i = f'stone ["stone_type":"{b}"]'

        imagenames[count] = i
        count += 1

    imagenames = list(reversed(imagenames))

    return imagenames


def commandgen(imagenames, num_cols):
    column = num_cols
    row = 0
    commands = []

    commands.append(f'tickingarea add ~ ~ ~ ~ ~ ~{num_cols} imageimport')
    for i in imagenames:
        i = f'fill ~ ~{row} ~{column} ~ ~{row} ~{column} {i}'
        if column == 1:
            column = num_cols
            print(num_cols)
            row += 1
        else:
            column -= 1
        commands.append(i)
    
    commands.append(f'tickingarea remove imageimport')

    return commands


#This will turn the commands into an mcfunction
def functiongen():
    print("This will generate an mcfunction")


#Typing the commands into their chat
def commandfill(commands):
    print("Please open your minecraft...\nCommands will begin to be typed in 5 seconds.")
    time.sleep(5)
    a = 1
    for i in commands:
        print(f'Filled {a} block(s)')
        time.sleep(1)
        pyautogui.press('/')
        time.sleep(0.05)
        pyautogui.typewrite(i, interval=0.05)
        time.sleep(0.05)
        pyautogui.press('enter')
        a += 1
    print("Successfully entered commands!")


#This will ask which import type they want
def mcbequestion(imagenames, num_cols):
    imagenames = blockgen(imagenames)
    commands = commandgen(imagenames, num_cols)
    print(commands)
    importtype = input("How would you like to import?\n[1]: mcfunction\n[2]: fill commands\n")

    check = True
    while check == True:
        if importtype == "1":
            functiongen()
            check = False
        elif importtype == "2":
            commandfill(commands)
            check = False
        else:
            importtype = input("Please pick 1 or 2.")



