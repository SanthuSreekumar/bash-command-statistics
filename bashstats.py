history_file= "/home/santhuc9/.bash_history"

with open(history_file, "r") as file:                       #reading the bash history file
    lines= file.readlines()

clean_lines = []                                            #clean blank spaces and blank lines

for line in lines:
    line = line.strip()

    if line != "":
        clean_lines.append(line)

commands=[]

for line in clean_lines:
    first_word=line.split()[0]
    commands.append(first_word)

command_count = {}                                         #counts the commands  #{}-Dictionary-counts the cmds in the list

for command in commands:
    if command in command_count:
        command_count[command] += 1
    else:
        command_count[command] = 1

print("Total commands used : ", command_count)

