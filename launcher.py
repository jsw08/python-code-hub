import os

while True:
    programs = os.listdir("./lib")
    print("Choose a program you want to run: ")
    for element in programs:
        print(str(element))
    print("")

    program_to_run = input()
    if program_to_run not in programs:
        print("Not a valid program.")
    
    else:
        print("Running program.")
        os.system("python ./lib/" + program_to_run)
        break