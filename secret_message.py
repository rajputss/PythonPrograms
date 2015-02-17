import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Shawn\Documents\Udacity\Foundations_Of_Programming\alphabet")
    #print(file_list)
    saved_path = os.getcwd()

    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Users\Shawn\Documents\Udacity\Foundations_Of_Programming\alphabet")

    #(2) for each file, rename_file
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "Bucharest"))
        os.rename(file_name, file_name.translate(None, "Bucharest"))
    os.chdir(saved_path)
        
rename_files()
                        
                           
