

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




#Generate the commands for the different directions
def positiveX(blocknames, num_cols, commands = []):
    row = 0
    column = num_cols
    commands.append(f'tickingarea add ~ ~ ~ ~{num_cols} ~ ~ imageimport')
    for i in blocknames:
        i = f'fill ~{column} ~{row} ~ ~{column} ~{row} ~ {i}'
        if column == 1:
            column = num_cols
            row += 1
        else:
            column -= 1
        commands.append(i)
    return commands

def positiveZ(blocknames, num_cols, commands = []):
    row = 0
    column = num_cols
    commands.append(f'tickingarea add ~ ~ ~ ~ ~ ~{num_cols} imageimport')
    for i in blocknames:
        i = f'fill ~ ~{row} ~{column} ~ ~{row} ~{column} {i}'
        if column == 1:
            column = num_cols
            row += 1
        else:
            column -= 1
        commands.append(i)
    return commands