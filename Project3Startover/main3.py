#MODULES for directories and more
def paths():
    from pathlib import Path

    #Absolute path

    #relative path - path starting from the current directory
    #path = Path('Project4Ok')
    #print(path.rmdir()) #mkdir to make folder/directory

    path = Path()
    # print(path.glob('*.*')) #only get files but not directories
    # print(path.glob('*')) #to iterate over everthing
    #print(path.glob('*.py')) #search all py files

    #all above ^^👆👆👆 will bring generator object
    # to iterate over it use for loop eg.
    for file in path.glob('*'):
        print(file)


# WORKING WITH SPREADSHEETS
import openpyxl as xl







#mosh - packages(3:30:25)