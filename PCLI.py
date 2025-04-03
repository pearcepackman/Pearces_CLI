import cmd
from rich.console import Console
from rich.align import Align
import os

from datetime import date
from datetime import datetime

console = Console()

class mycli(cmd.Cmd):
    #Initializing stuff
    def __init__(self):
        super().__init__()
        ##Gets current directory and uses it as prompt so "file_path PCLI Command Line >> "
        self.current_directory = os.getcwd()
        self.prompt = f"{self.current_directory} PCLI Command Line >> "
        
    myname = """


    ____   ______ ___     ____   ______ ______ _  _____    ______ __     ____
   / __ \ / ____//   |   / __ \ / ____// ____/( )/ ___/   / ____// /    /  _/
  / /_/ // __/  / /| |  / /_/ // /    / __/   |/ \__ \   / /    / /     / /  
 / ____// /___ / ___ | / _, _// /___ / /___     ___/ /  / /___ / /___ _/ /   
/_/    /_____//_/  |_|/_/ |_| \____//_____/    /____/   \____//_____//___/   
                                                                             
                   ______ _   __     __ ____ __  __                          
                  / ____// | / /    / // __ \\ \/ /                          
                 / __/  /  |/ /__  / // / / / \  /                           
                / /___ / /|  // /_/ // /_/ /  / /                            
               /_____//_/ |_/ \____/ \____/  /_/                             
                                                                             
               
                                                                     """
    myname = Align.center(myname)
    os.system("clear")
    console.print(myname, style='red bold')
    # Startup stuff
    startupmsg = "Welcome to PCLI! To see available commands, type 'help'"
    console.print(startupmsg, style='green bold')
    
    #Quits out of the CLI and displays message
    def do_quit(self, line):
        """Type 'quit' to exit the CLI"""
        os.system("clear")
        goodbye = """

   ______ ____   ____   ____   ____ __  __ ______
  / ____// __ \ / __ \ / __ \ / __ )\ \/ // ____/
 / / __ / / / // / / // / / // __  | \  // __/   
/ /_/ // /_/ // /_/ // /_/ // /_/ /  / // /___   
\____/ \____/ \____//_____//_____/  /_//_____/   
                                                 
                                                 """
        goodbye = Align.center(goodbye)
        console.print(goodbye, style='red bold')
        return True

    def do_add(self, line):
        """Type 'add' to add two variables"""
        func_name = "Addition >> "
        self.prompt = f"{self.current_directory} {func_name}"
        while True:
            try:
                num1 = int(input(f"{self.prompt}Number 1: "))
                num2 = int(input(f"{self.prompt}Number 2: "))
                console.print(f"{self.prompt}The result of {num1} + {num2} = {num1 + num2}")
                console.print("")
                break
            except ValueError:
                console.print("Invalid input, use numbers only", style="red")

    def do_subtract(self, line):
        """Type 'subtract' to subtract two variables"""
        func_name = "subtraction >> "
        self.prompt = f"{self.current_directory} {func_name}"
        while True:
            try:
                num1 = int(input(f"{self.prompt}Number 1: "))
                num2 = int(input(f"{self.prompt}Number 2: "))
                console.print(f"{self.prompt}The result of {num1} - {num2} = {num1 - num2}")
                console.print("")
                break
            except ValueError:
                console.print("Invalid input, use numbers only", style="red")

    def do_multiply(self, line):
        """Type 'multiply' to multiply two variables"""
        func_name = "multiply >> "
        self.prompt = f"{self.current_directory} {func_name}"
        while True:
            try:
                num1 = int(input(f"{self.prompt}Number 1: "))
                num2 = int(input(f"{self.prompt}Number 2: "))
                console.print(f"{self.prompt}The result of {num1} * {num2} = {num1 * num2}")
                console.print("")
                break
            except ValueError:
                console.print("Invalid input, use numbers only", style="red")

    def do_divide(self, line):
        """Type 'divide' to divide two variables"""
        func_name = "divide >> "
        self.prompt = f"{self.current_directory} {func_name}"
        while True:
            try:
                num1 = int(input(f"{self.prompt}Number 1: "))
                num2 = int(input(f"{self.prompt}Number 2: "))
                res = round(num1 / num2, 4)
                console.print(f"{self.prompt}The result of {num1} / {num2} = {res}")
                console.print("")
                break
            except ValueError:
                console.print("Invalid input, use numbers only", style="red")

    def do_list(self, line):
        """List files in the current directory"""
        files_directories = os.listdir(os.getcwd())
        console.print("")
        for item in files_directories:
            
            console.print("- "+item)
        console.print("")

    def do_listtree(self, line):
        """Lists files in a tree format with relation to each other"""
        files_directories = os.listdir(os.getcwd())
        console.print("")
        console.print(" "+os.path.basename(self.current_directory), style='green')
        for item in files_directories:
            
            
            console.print(" |")
            console.print(" |-- "+item)
            subdir = 0
            
            try:
                subfile = os.listdir(item)
                subdir = 0
                
                for i in subfile:

                    if(subdir < 3):
                        console.print(" |   |")
                        console.print(" |   |-- "+i)
                        subdir += 1
                    else:
                        break
            except:
                console.print(" |")
        console.print("")

    def do_mkd(self, line):
        """Makes a directory"""
        if line:
            try:
                os.mkdir(line)
                os.chdir(line)
                self.current_directory = line
            except FileExistsError:
                console.print("Error: File already exists!", style = "red")
        else: console.print("Error: No filename specified!", style = "red")
    
    def do_rm(self, line):
        """Removes whatever is at the filepath specified"""
        if line:
            try:
                console.print("")
                ans = input("You are about to delete a file, are you sure you want to do this? y or n: ")
                if ans == "y":
                    console.print(f"{os.getcwd()}/{line} REMOVED!", style = "red")
                    os.chmod(os.getcwd()+"/"+line, 0o777)
                    os.remove(os.getcwd()+"/"+line)
            except FileNotFoundError:
                console.print("Error: File not found!", style = "red")
        else: console.print("Error: No filename specified!", style = "red")
        console.print("")

    def do_cwd(self, line):
        """Print the current working directory"""
        console.print(self.current_directory)
    
    def do_back(self, line):
        """Backs up one directory in file path"""
        newpath = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        os.chdir(newpath)
        self.current_directory = newpath

    def do_cd(self, line):
        """Changes directory"""
        self.prompt = self.current_directory
        if line:
            try: 
                os.chdir(line)
                self.current_directory = line
            except:
                console.print("No such directory exists!", style = "red")
        
        else: console.print("No directory specified!", style = "red")
    
    def do_mktxt(self, line):
        """Makes text file in current directory"""
        if line:
            
            console.print("Enter text (end with /e)")
            console.print("To go back a line, type /b")
            line_counter = 0
            lines = []
            while True:
                user_input = input(f"{len(lines)}: ")
                if user_input.endswith("/e"):
                    lines.append(user_input[:-2])  
                    break
                elif user_input.endswith("/b"):
                    
                    
                    lines.append(console.input(f"Editing line {len(lines)-1}: "))
                    
                    lines.pop(-2)
                    

                if user_input != "/b":
                    lines.append(user_input)
                line_counter += 1
                
            with open(f"{os.getcwd()}/{line}", 'w') as file:
                file.write("\n".join(lines))
            
    def do_readtxt(self, line):
        """Reads text file"""
        if line:
            console.print("")
            try:
                with open(f"{os.getcwd()}/{line}", 'r') as file:
                    line_num = 0
                    for line in file:
                        console.print(f"{line_num}: {line.strip()}")
                        line_num += 1
                    #console.print(file.read())
            except:
                console.print("Error, file not found!", style = 'red')
        console.print("")
    
    def do_edittxt(self, line):
        """Edits text file"""
        if line: 
            console.print("")
            with open(f"{os.getcwd()}/{line}", 'r+') as file:
                lines = file.readlines()
                
            for line_num, fileline in enumerate(lines):
                console.print(f"{line_num}: {fileline.strip()}")

            try:
                edit_line = int(console.input("What line do you want to edit?: "))

                if 0 <= edit_line < len(lines):
                    newline = console.input(f"Editing line #{edit_line}: ")
                    lines[edit_line] = newline+"\n"

                    with open(f"{os.getcwd()}/{line}", 'w') as file:
                        file.seek(0)
                        file.writelines(lines)
                        file.truncate
                    
                else: 
                    console.print("Error, line does not exist!", style='red')
            except:
                console.print("Error, invalid input", style = "red")

             

    def do_clear(self, line):
        """Clears the window"""
        os.system("clear")

    def do_screensaver(self, line):
        """This one is pretty self-explanatory, give it a shot!"""
        ss1 = """

 _______  _______  _       _________
(  ____ )(  ____ \( \      \__   __/
| (    )|| (    \/| (         ) (   
| (____)|| |      | |         | |   
|  _____)| |      | |         | |   
| (      | |      | |         | |   
| )      | (____/\| (____/\___) (___
|/       (_______/(_______/\_______/
                                     """
        belowmsg = """

______  _   _  _____  _    _____   _____  _   _  ______ __   __ _   _  _____  _____  _   _ 
| ___ \| | | ||_   _|| |  |_   _| |_   _|| \ | | | ___ \\ \ / /| | | ||_   _||  _  || \ | |
| |_/ /| | | |  | |  | |    | |     | |  |  \| | | |_/ / \ V / | |_| |  | |  | | | ||  \| |
| ___ \| | | |  | |  | |    | |     | |  | . ` | |  __/   \ /  |  _  |  | |  | | | || . ` |
| |_/ /| |_| | _| |_ | |____| |    _| |_ | |\  | | |      | |  | | | |  | |  \ \_/ /| |\  |
\____/  \___/  \___/ \_____/\_/    \___/ \_| \_/ \_|      \_/  \_| |_/  \_/   \___/ \_| \_/

                                                                                            """
        
        mymsg = """

______  _____   ___  ______  _____  _____  _  _____   _____  _      _____ 
| ___ \|  ___| / _ \ | ___ \/  __ \|  ___|( )/  ___| /  __ \| |    |_   _|
| |_/ /| |__  / /_\ \| |_/ /| /  \/| |__  |/ \ `--.  | /  \/| |      | |  
|  __/ |  __| |  _  ||    / | |    |  __|     `--. \ | |    | |      | |  
| |    | |___ | | | || |\ \ | \__/\| |___    /\__/ / | \__/\| |____ _| |_ 
\_|    \____/ \_| |_/\_| \_| \____/\____/    \____/   \____/\_____/ \___/ 
                                                                          







                                                                          
"""
        ss1 = Align.center(ss1)
        belowmsg = Align.center(belowmsg)
        mymsg = Align.center(mymsg)
        os.system("clear")
        console.print(ss1, style = 'red blink')
        console.print(mymsg, style = "blue")
        console.print(belowmsg, style = '#969493')

    def do_history(self, line):
        try:
            history_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history')
            history_text_path = os.path.join(history_dir, str(date.today()))
            with open(history_text_path, 'r') as historytext:
                console.print("")
                console.print(f"Command history for {date.today()}")
                for line in historytext:
                    console.print(f"{line.strip()}")
            console.print("")
        except:
            console.print("Error, history file does not exist yet!", style = 'red')
    def postcmd(self, stop, line):
        """This function is called after each command to update the prompt."""
        history_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history')
        if line:
            try:
                if not os.path.exists(history_dir):
                    os.mkdir(history_dir)

                history_text_path = os.path.join(history_dir, str(date.today()))
                
                if line != "quit":
                    with open(history_text_path, 'a') as historytext:
                        historytext.write(f"\n{datetime.now()} - {line}")
                else:
                    with open(history_text_path, 'a') as historytext:
                        historytext.write(f"\n{datetime.now()} ------------- QUIT SESSION ------------- ")
            except:
                console.print("ERROR", style='red')
        self.prompt = f"{os.getcwd()} PCLI Command Line >> "
        return stop


if __name__ == '__main__':
    mycli().cmdloop()
