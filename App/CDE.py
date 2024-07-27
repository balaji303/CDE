"""
Author: Balaji303
Date: 2024-07-27
Description: CD-E Your Language IDE v4.1 - A simple IDE for compiling and running C, C++, and Python code.
License: MIT License
"""

# Importing necessary wxPython modules
import wx.xrc
import wx.aui
import wx.richtext
import os
import subprocess

# Define the main GUI class inheriting from wx.Frame
class GUI(wx.Frame):
    def __init__(self, parent):
        # Initialize the base class wx.Frame with title and size
        wx.Frame.__init__(self, 
                          None,
                          -1, 
                          u"CD-E Your Language IDE v4.1", 
                          size=(600, 600),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        # Set the foreground and background colors
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(182, 180, 235))
        
        # Define the list of languages and C compilation stages
        language_list = ['C', 'C++', 'Python']
        c_stage_list = ['Preprocessor', 'Compiler', 'Assembler', 'Linker', 'All']
        
        # Create a StaticText widget to prompt user to enter code
        self.label_enter_code = wx.StaticText(self, -1, "Enter the Code:", (70, 100), style=wx.TE_RICH)
        self.label_enter_code.SetForegroundColour(wx.BLACK)
        
        # Create a font with the desired size
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        # Set the font for the StaticText widget
        self.label_enter_code.SetFont(font)
        
        # Create a RadioBox for language selection
        self.language_box = wx.RadioBox(self, 
                                        label='Language',
                                        pos=(10, 5), 
                                        choices=language_list,
                                        majorDimension=1,
                                        style=wx.RA_SPECIFY_COLS)
        
        # Create a RadioBox for C compilation stage selection
        self.c_stage_box = wx.RadioBox(self, 
                                       label='C Stages',
                                       pos=(100, 5), 
                                       choices=c_stage_list,
                                       majorDimension=1,
                                       style=wx.RA_SPECIFY_ROWS)
        
        # Create a RichTextCtrl for code input
        self.code_text_ctrl = wx.richtext.RichTextCtrl(self, 
                                                       wx.ID_ANY, 
                                                       wx.EmptyString, 
                                                       wx.Point(70, 120), 
                                                       wx.Size(440, 400), 
                                                       0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS | wx.FONTSIZE_X_LARGE)
        
        # Create a button for running the code
        self.run_button = wx.Button(self, 
                                    wx.ID_ANY, 
                                    u"Run", 
                                    wx.Point(250, 525))
        # Bind the button event to the compile function
        self.run_button.Bind(wx.EVT_BUTTON, self.compile_code)
    
    def compile_code(self, event):
        # Get the code from the text control
        code = self.code_text_ctrl.GetValue()
        
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)
        os.chdir(script_dir)
        
        # Get the selected programming language
        selected_language = self.language_box.GetStringSelection()
        
        if selected_language == 'C':
            # Write the code to a C file
            with open("program.c", "w") as c_file:
                c_file.write(code)
            c_file.close()
            
            # Get the selected C compilation stage
            selected_stage = self.c_stage_box.GetStringSelection()
            
            # Execute the corresponding gcc commands based on the selected stage
            if selected_stage == 'All':
                subprocess.call('gcc program.c -o program', shell=False)
                subprocess.call('.\\program', shell=False)
            elif selected_stage == 'Preprocessor':
                subprocess.call('gcc -E program.c -o program.i', shell=False)
            elif selected_stage == 'Compiler':
                subprocess.call('gcc -S program.i -o program.s', shell=False)
            elif selected_stage == 'Assembler':
                subprocess.call('gcc -c program.s -o program.o', shell=False)
            elif selected_stage == 'Linker':
                subprocess.call('gcc program.o -o program', shell=False)
        
        elif selected_language == 'C++':
            # Write the code to a C++ file
            with open("program.cpp", "w") as cpp_file:
                cpp_file.write(code)
            cpp_file.close()
            
            # Compile and run the C++ program
            subprocess.call('g++ program.cpp -o program', shell=False)
            subprocess.call('.\\program', shell=False)
        
        elif selected_language == 'Python':
            # Write the code to a Python file
            with open("program.py", "w") as py_file:
                py_file.write(code)
            py_file.close()
            
            # Run the Python program
            subprocess.call('python program.py', shell=False)
        
        else:
            print("Error")

# Main execution
if __name__ == '__main__':
    # Create an application object
    app = wx.App(False)
    # Create an instance of the GUI
    gui = GUI(None)
    # Show the GUI
    gui.Show(True)
    # Start the main event loop
    app.MainLoop()
