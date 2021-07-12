

#UI/UX Librarys
import wx
from wx.core import Size
import wx.xrc
import wx.aui
import wx.richtext

#OS library
import os


class GUI ( wx.Frame ):
    
    def __init__( self, parent ):
    
        
        wx.Frame.__init__(self, 
                          None, 
                          -1, 
                          u"CD-E Your C Language IDE", 
                          size=(500, 500),#Window size
                          style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.SetBackgroundColour( wx.Colour( 182, 180, 235 ) )
        self.text1 = wx.StaticText( self, 
                                    -1,
                                    "Enter the C Code:", 
                                    ( 40,30 ), 
                                    style=wx.TE_RICH ) 
        self.text1.SetForegroundColour( wx.BLACK )
     
        self.text = wx.richtext.RichTextCtrl(self, 
                                              wx.ID_ANY, 
                                              wx.EmptyString, 
                                              wx.Point( 40,50 ), 
                                              wx.Size( 400,350 ), 
                                              0|wx.VSCROLL|
                                              wx.HSCROLL|wx.NO_BORDER|
                                              wx.WANTS_CHARS|wx.FONTSIZE_X_LARGE )
        
        self.compile_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Run", 
                                   wx.Point(210,420))
        self.compile_button.Bind(wx.EVT_BUTTON, self.compile_fun) 


    def compile_fun(self,e):
        code = self.text.GetValue()        
        pyfiledir  = os.path.dirname( __file__ )
        os.chdir(pyfiledir)
        with open( "setup.c","w" ) as cfile:
            cfile.write(code)
        cfile.close()
        os.system("gcc setup.c -o setup")
        os.system(".\setup")
        return
        

if __name__ == '__main__':
    
    app = wx.App(False) 
    app_gui = GUI(None) 
    app_gui.Show(True)      
    app.MainLoop()  
