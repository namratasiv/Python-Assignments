# Namrata Sivakumar - 1001508168
# Pythogorean Calculator
# PY Homework #5

import tkinter
import math

class PythGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x150')
        self.main_window.title('Right Triangle Calculator')

       
        self.top_frame = tkinter.Frame()
        self.mid1 = tkinter.Frame()
        self.mid2 = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

       
        self.label1 = tkinter.Label(self.top_frame,
                    text='Side A:', width=10)
        self.entry1 = tkinter.Entry(self.top_frame,
                                        width=25)
        self.label2 = tkinter.Label(self.mid1,
                    text='Side B:', width=10)
        self.entry2 = tkinter.Entry(self.mid1,
                                        width=25)


       
        self.label1.pack(side='left')
        self.entry1.pack(side='left')
        self.label2.pack(side='left')
        self.entry2.pack(side='left')

       
        self.result_label = tkinter.Label(self.mid2,
                                         text='Side C: ', width=10)
                                        
        
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()

        
        self.pyth_label = tkinter.Label(self.mid2,textvariable=self.value, width=26, borderwidth=1, relief="solid")

       
        self.result_label.pack(side='left')
        self.pyth_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate', width='10',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit', width='10',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid1.pack()
        self.mid2.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.
    
    def convert(self):
        
        a = float(self.entry1.get())
        b = float(self.entry2.get())

        c = math.sqrt(a**2 + b**2)
        str_c='{:.3f}'.format(c)

        
        self.value.set(str_c)

# Create an instance of the PythGUI class.
pyth = PythGUI()
