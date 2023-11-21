import os

def launcher():
    while True:
        programs = os.listdir("./lib")
        folders = []
        print("Choose a program you want to run: ")
        for program in programs:
            if os.path.isdir("./lib/" + program) == True:
                print("(folder) " + program)
                folders.append(program)
            if program in folders:
                print
            else:
                print(program)
        print()

        program_to_run = input()
        if program_to_run not in programs:
            print("Not a valid program.")
    
        elif program_to_run in folders:
            new_programs = os.listdir("./lib/" + program_to_run)
            print(new_programs)
            
        else:
            print("Running program.")
            os.system("python ./lib/" + program_to_run)
            break

launcher()