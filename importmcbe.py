import pyautogui
import time
import os
import json
import uuid

#This will generate the block names for the other methods
def blockgen(imagenames):
    count = 0
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
        elif i[:10] == "fsandstone":
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

#Makes the list of commands and appends it to the list "commands"
def commandgen(imagenames, num_cols):
    column = num_cols
    row = 0
    commands = []

    commands.append(f'tickingarea add ~ ~ ~ ~ ~ ~{num_cols} imageimport')
    for i in imagenames:
        i = f'fill ~ ~{row} ~{column} ~ ~{row} ~{column} {i}'
        if column == 1:
            column = num_cols
            row += 1
        else:
            column -= 1
        commands.append(i)
    
    commands.append(f'tickingarea remove imageimport')

    return commands



#Generate the json content for the manifest file
def makemanifest(mainfilename):
    name = mainfilename + ' IMG Generator'
    uuid1 = str(uuid.uuid4())
    uuid2 = str(uuid.uuid4())
    manifestcontent = {
        "format_version": 2,
        "header": {
            "description": 'Created by groege#6236',
            "name": name,
            "uuid": str(uuid1),
            "version": [1, 0, 0],
            "min_engine_version": [1, 16, 0]
        },
        "modules": [
            {
                "description": 'Created by groege#6236',
                "type": "data",
                "uuid": str(uuid2),
                "version": [1, 0, 0]
            }
        ]
    }
    return manifestcontent


#This will turn the commands into an mcfunction
def functiongen(mainfilename, commands):
    max_commands_per_file=9750

    # Make the folders and manifest
    new_folder_path = os.path.join('functionpacks/', mainfilename)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    
    #Call manifest generation
    manifestcontent = makemanifest(mainfilename)

    #Create manifest file and dump json data into it
    file_path = os.path.join(new_folder_path, 'manifest.json')
    with open(file_path, "w") as f:
        json.dump(manifestcontent, f, indent=2)
    
    #Create the "functions" folder
    folder_path = os.path.join(new_folder_path, 'functions')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Write the commands to one or more function files
    num_files = len(commands) // max_commands_per_file + 1
    for i in range(num_files):

        # Create a new function file with a suffix if needed
        filename = f"{mainfilename}_{i}.mcfunction"
        file_path = os.path.join(folder_path, filename)
        
        # Write up to max_commands_per_file commands to the file
        start_idx = i * max_commands_per_file
        end_idx = (i + 1) * max_commands_per_file
        with open(file_path, "w") as f:
            for command in commands[start_idx:end_idx]:
                f.write(command + "\n")

    print("The mcfunction file has been generated.")



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
def mcbequestion(imagenames, num_cols, mainfilename):
    imagenames = blockgen(imagenames)
    commands = commandgen(imagenames, num_cols)
    importtype = input("How would you like to import?\n[1]: mcfunction\n[2]: fill commands (this takes a long time)\n")

    check = True
    while check == True:
        if importtype == "1":
            functiongen(mainfilename, commands)
            check = False
        elif importtype == "2":
            commandfill(commands)
            check = False
        else:
            importtype = input("Please pick 1 or 2.")