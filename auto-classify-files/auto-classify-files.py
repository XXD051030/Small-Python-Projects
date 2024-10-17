# this program will request enter a path and auto classify the files in the folder
# the program will classify the files according to the file suffix
# when the folder did not exist, the program will create the folder nammed by the file suffix

from pathlib import Path
import shutil
import time

while True:
    print('Enter the path:')                    # request for the path
    directory = input(">")
    directory = directory.replace('"','')
    path = Path(directory)
    if path.exists():
        print(f"The path is {path.exists()}")
        for file in path.iterdir():
            time.slee(0.2)
            print(file.name)
        if input(f'auto classify? (Yes/No) \n>').lower() == "yes":

            for file in path.iterdir():
                
                if file.is_file():
                    time.slee(0.2)
                    file_extension = file.suffix[1:]
                    target_folder = path / file_extension

                    if not target_folder.exists():
                        target_folder.mkdir()
                        print(f"Created folder: {target_folder}")

                    shutil.move(str(file), str(target_folder / file.name))
                    print(f"Moved {file.name} to {target_folder}")
            print('All done')
        else:
            print("invalid value")

    else:
        print("Path not exist")

    if input('Continue?(Yes/No) \n>').lower() == "no":
        break

