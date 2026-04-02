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

print("Total commands used : ", len(commands))

