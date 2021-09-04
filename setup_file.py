#CD-E


import wx
from wx.core import Size
import wx.xrc
import wx.aui
import wx.richtext
import os


class GUI ( wx.Frame ):
    
    def __init__( self, parent ):
    
        
        wx.Frame.__init__(self, 
                          None, 
                          -1, 
                          u"CD-E Your Language IDE v2", 
                          size=(500, 500),#Window size
                          style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.Colour( 182, 180, 235 ) )
        
        langlist = ['C', 'C++'] 
        self.text1 = wx.StaticText( self, 
                                    -1,
                                    "Enter the Code:", 
                                    ( 40,50 ), 
                                    style=wx.TE_RICH ) 
        self.text1.SetForegroundColour( wx.BLACK )
        self.languagebox = wx.RadioBox(self, 
                                label = 'Language',
                                pos = (200,5), 
                                choices = langlist,
                                majorDimension = 1,
                                style = wx.RA_SPECIFY_ROWS)

        self.text = wx.richtext.RichTextCtrl(self, 
                                              wx.ID_ANY, 
                                              wx.EmptyString, 
                                              wx.Point( 40,70 ), 
                                              wx.Size( 400,340 ), 
                                              0|wx.VSCROLL|
                                              wx.HSCROLL|wx.NO_BORDER|
                                              wx.WANTS_CHARS|wx.FONTSIZE_X_LARGE )
        
        self.compile_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Run", 
                                   wx.Point(210,425))
        self.compile_button.Bind(wx.EVT_BUTTON, self.compile_fun) 


    def compile_fun(self,e):
        code = self.text.GetValue()        
        pyfiledir  = os.path.dirname( __file__ )
        os.chdir(pyfiledir)
        language=self.languagebox.GetStringSelection()
        if language == 'C':
            with open( "setup.c","w" ) as cfile:
                cfile.write(code)
            cfile.close()
            os.system("gcc setup.c -o setup")
        elif language == 'C++':
            with open( "setup.cpp","w" ) as cppfile:
                cppfile.write(code)
            cppfile.close()
            os.system("g++ setup.cpp -o setup")
        else:
            print("Error")
        os.system(".\setup")
        return
        

if __name__ == '__main__':
    
    app = wx.App(False) 
    app_gui = GUI(None) 
    app_gui.Show(True)      
    app.MainLoop()  
