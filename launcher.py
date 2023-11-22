import os

def dir():
    while True:
        directories = []
        directories.append()
        folders = []
        dir_programs = os.listdir("./lib/" + program_to_run)
        print("What program in directory ./lib/" + program_to_run + " do you want to run?")
        for dir_program in dir_programs:
            if os.path.isdir("./lib/" + program_to_run + "/" + dir_program) == True:
                print("(dir) " + dir_program)
                folders.append(dir_program)
            if dir_program in folders:
                print
            else:
                print(dir_program)
        print()

        new_program_to_run = input()
        if new_program_to_run not in dir_programs:
            print("Not a valid program or directory.")
            
        elif new_program_to_run in folders:
            dir_programs = os.listdir("./lib/" + program_to_run + "/" + new_program_to_run)
            dir()

        else:
            print("Running program.")
            os.system("python ./lib/" + program_to_run + "/" + new_program_to_run)
            break


def launcher():
    while True:
        programs = os.listdir("./lib")
        folders = []
        print("Choose a program you want to run: ")
        for program in programs:
            if os.path.isdir("./lib/" + program) == True:
                print("(dir) " + program)
                folders.append(program)
            if program in folders:
                print
            else:
                print(program)
        print()

        global program_to_run
        program_to_run = input()
        if program_to_run not in programs:
            print("Not a valid program or directory.")
    
        elif program_to_run in folders:
            dir_programs = os.listdir("./lib/" + program_to_run)
            dir()
            
        else:
            print("Running program.")
            os.system("python ./lib/" + program_to_run)
            break

launcher()