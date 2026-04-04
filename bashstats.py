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
    if first_word.isalpha():                                        #isalpha only check for alphabetical cmds
        commands.append(first_word)

command_count = Counter(commands)                                     # counter is easier and simpler

while True:
    print("\n\n=======================")
    print("1. Show 10 most used commands")
    print("2. Search for command")
    print("3. Create report file")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        print("Ten most used commands- \n")

        for command, count in command_count.most_common(10):                   #(10) gives the top 10 while ()[10] gives us the 11th unit in the list
            print(command, ":" ,count)

    elif choice=="2":
        search_command = input("\nEnter the command you want to search : ")     #search for specific command

        if search_command in command_count:
            print(search_command,":",command_count[search_command])
        else:
            print("Command not found")

    elif choice=="3":
        with open("cmds_report.txt","w") as file:                               #creates (.txt) report file for the top 10 cmds
            file.write("Top commands\n")

            for command,count in command_count.most_common(10):
                file.write(f"{command} : {count}\n")
        print("\n\033[1;36mReport file created\033[0m")

    elif choice=="4":
        print("Exiting..")
        break
    else:
        print("Invalid choice")
