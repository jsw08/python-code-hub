import os

def dir():
    while True:
        folders = []
        dir_programs = os.listdir("./lib/" + "/".join(directory))
        print("What program in directory ./lib/" + "/".join(directory) + " do you want to run?")
        for dir_program in dir_programs:
            if os.path.isdir("./lib/" + "/".join(directory) + "/" + dir_program) == True:
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
            dir_programs = os.listdir("./lib/" + "/".join(directory) + "/" + new_program_to_run)
            directory.append(new_program_to_run)
            dir()

        else:
            print("Running program.")
            os.system("python ./lib/" + "/".join(directory) + "/" + new_program_to_run)
            break
        
directory = []
dir()