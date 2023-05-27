import os
import json
import uuid
import zipfile
from commandgenerator import *

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


def functiongen(mainfilename, commands):
    max_commands_per_file = 9750

    # Make the folders and manifest
    new_folder_path = os.path.join('functionpacks/', mainfilename)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # Call manifest generation
    manifestcontent = makemanifest(mainfilename)

    # Create manifest file and dump json data into it
    file_path = os.path.join(new_folder_path, 'manifest.json')
    with open(file_path, "w") as f:
        json.dump(manifestcontent, f, indent=2)

    # Create the "functions" folder
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

    # Create a zip file
    zip_path = os.path.join('functionpacks/', f"{mainfilename}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(new_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, new_folder_path))

    # Change the file extension
    renamed_zip_path = os.path.join('functionpacks/', f"{mainfilename}.zip")
    renamed_zip_path = renamed_zip_path.replace('.zip', '.mcpack')
    os.rename(zip_path, renamed_zip_path)

    if os.name == 'nt':  # Windows
        os.startfile('functionpacks')

    print("The mcfunction file has been generated and zipped.")



#Makes the list of commands and appends it to the list "commands"
def commandgen(blocknames, num_cols, direction):

    #Positive X axis
    if direction == 1:
        commands = positiveX(blocknames, num_cols)

    #Positve Z axis
    if direction == 2:
        commands = positiveZ(blocknames, num_cols)

    #Remove ticking area
    commands.append(f'tickingarea remove imageimport')

    return commands



#This will ask which import type they want
def mcbequestion(imagenames, num_cols, mainfilename):
    #Convert to block names
    blocknames = blockgen(imagenames)

    #Ask question to find out if they want it to be upright or flat ---------------------------

    #Ask which direction to be imported
    check = True
    while check == True:
        try:
            direction = int(input("Which direction would you like it to be imported?\n[1]: Positive X\n[2]: Positive Z\n"))
            check = False
        except:
            print("\nPlease pick 1 or 2")
        
        if direction == 1 or 2:
            #Generates the command list
            commands = commandgen(blocknames, num_cols, direction)
        else:
            print("\nPlease pick 1 or 2")


    #Generates the function file
    functiongen(mainfilename, commands)
