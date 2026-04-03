from collections import Counter

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

command_count = Counter(commands)                                     # counter is easier and simpler 

print("Ten most used commands- \n")

for command, count in command_count.most_common(10):                   #(10) gives the top 10 while ()[10] gives us the 11th unit in the list
    print(command, ":" ,count)

