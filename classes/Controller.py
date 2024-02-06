#Name: Irfan Nasim
#Admission Number: 2201816
#Class: DAAA/FT/2B/07
import os
import string
from classes.InputOutput import InputOutput
from classes.Sorted import SortedList
from classes.MathTree import MathTree, global_hash_table
from classes.HashTable import HashTable
from classes.BuildParseTree import buildParseTree
class Controller:
    def __init__(self):
        self.choice = None
        self.alphabet=string.ascii_uppercase
        self.IO=InputOutput()
        self.__filedir = os.path.dirname(os.path.abspath(__file__))
  
    def display_menu(self):
        menu = self.IO.open_file('menu.txt')
        print(menu)

    def option1(self):
        expression=input("Enter the assignment statement you want to add/modify: \n For example, a=(1+2)\n")
        expression=expression.split("=")
        
        if len(expression)==2:
            if expression[0].isalpha() :
                e=buildParseTree(expression[1],expression[0])
                if e.validate():
                    global_hash_table[expression[0]]=e
                else:
                    print('Invalid input, please enter a valid assignment statement')

            else:
                print("Invalid input, please enter a valid assignment statement")


    def option2(self):
        print("Current Assignment Statements:")
        for i in global_hash_table:
            if global_hash_table[i].expression != None:
                print(f'{i} ={global_hash_table[i].expression}=> {global_hash_table[i].fast_eval}')
        return None
    
    def option3(self):
        variable=input("Please enter the variable you want to evaluate: ")
        if global_hash_table[variable] == None: 
            print(f'Variable {variable} does not exist!')
            return None
        elif global_hash_table[variable].fast_eval != None:
            global_hash_table[variable].root.printInorder(0)
        print(f'Value for variable \"{variable}\" is {global_hash_table[variable].fast_eval}')
        return None
    def option4(self):
        file_contents=self.IO.input_file("Please enter the file path of the file you want to read from: ","Invalid file path, please enter a valid file path")
        lines = file_contents.splitlines()
        for line in lines:
            expression=line.split("=")
            if len(expression)==2:
                if expression[0].isalpha() :
                    e=buildParseTree(expression[1],expression[0])
                    if e.validate():
                        global_hash_table[expression[0]]=e
        print("Current Assignment Statements:")
        for i in global_hash_table:
            if global_hash_table[i].expression != None:
                print(f'{i} ={global_hash_table[i].expression}=> {global_hash_table[i].fast_eval}')
        return None
    def option5(self):
        content =''
        prev_i = ('','','')
        outputpath = input('Please enter output file: ')
        sortedvalues = [(i[1].fast_eval, i[0], i[1].expression) for i in sorted(global_hash_table.items(), key=lambda x: float('-inf') if x[1].fast_eval is None else x[1].fast_eval, reverse=True)]
        for i in sortedvalues:
            if i[2] != None:
                if i[0] != prev_i[0] and i[0] != sortedvalues[0][0]:
                    content += (f'\n*** Statements with value=> {i[0]}\n')
                    content += (f'{i[1]}={i[2]}')
                    prev_i = i
                elif i[0] == prev_i[0]:
                    content += (f'{i[1]}={i[2]}')
                else:
                    content += (f'*** Statements with value=> {i[0]}\n')
                    content += (f'{i[1]}={i[2]}')
                    prev_i = i
                content += '\n'
        self.IO.write_file(outputpath,content)
        print(f'file {outputpath} written successfully!')
        return None
    def option6(self):
        
    def option7(self):
        return None

    def main(self):
        while True:
            self.display_menu()
            self.choice = input("Enter choice: ")

            match self.choice:
                case '1':
                    self.option1()
                    input("\nPress enter key, to continue....\n")
                case '2':
                    self.option2()
                    input("\nPress enter key, to continue....\n")
                case '3':
                    self.option3()
                    input("\nPress enter key, to continue....\n")
                case '4':
                    self.option4()
                    input("\nPress enter key, to continue....\n")
                case '5':
                    self.option5()
                    input("\nPress enter key, to continue....\n")
                case '6':
                    self.option6()
                    input("\nPress enter key, to continue....\n")
                case '7':
                    self.option7()
                    input("\nPress enter key, to continue....\n")
                case '8':
                    print("\nBye, thanks for using ST1507 DSAA: Evaluating & Sorting Assigment Statements")
                    return
                case _:
                    print("Invalid choice. Please enter a valid option (1-8).\n")
                