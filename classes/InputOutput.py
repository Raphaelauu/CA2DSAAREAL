#Name: Irfan Nasim & Raphael Lau
#Admission Number: 2201816 & ???????
#Class: DAAA/FT/2B/07
import re
import os
class InputOutput:
    # General purpose input + validation (regex) function with support for and error messages
    def input_valid(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp
    
    # General purpose input + validation function for txt files
    def input_file(self,msg,invalid_msg):
        file_contents = None
        while file_contents is None:
            file_path = self.input_valid("^.+\.txt$", msg, invalid_msg)
            file_contents = self.open_file(file_path)
        return file_contents
    
    # Barebones function to open a file from file_path, may not perform well on larger files
    def open_file(self,file_path):
        try:
            with open(file_path, "r") as file:
                file_contents = file.read()
            return file_contents
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Barebones function to write to a file from file_path, may not perform well on larger files
    def write_file(self,file_path,content):
        try:
            with open(file_path, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"An error occurred: {e}")
    # Function to get a list of file names from a folder
    def get_file_names_from_folder(self,current_directory, folder_name):
        folder_path = os.path.join(current_directory, folder_name)

        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            return []

        items = os.listdir(folder_path)
        
        return items