history_file= "/home/santhuc9/.bash_history"

with open(history_file, "r") as file:                       #reading the bash history file
    lines= file.readlines()

clean_lines = []                                            #clean blank spaces and blank lines

for line in lines:
    line = line.strip()

    if line != "":
        clean_lines.append(line)

total_commands=len(clean_lines)                             #countining the commands

print("Total commands used : ", total_commands)

