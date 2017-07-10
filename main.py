import Tkinter
import tkFileDialog
import tkMessageBox
import FileMenu
import ScrolledText
        # as Tkinter Text Area does not provide Scrolling

root = Tkinter.Tk(className="NotePad")
textPad = ScrolledText.ScrolledText(root, width = 95, height = 45,bg="BLACK",fg="MediumBlue",
                    bd=10,font="Helvetica 16 bold italic",cursor="xterm",highlightcolor="green",
                    highlightbackground="indian red", highlightthickness=5, insertborderwidth=3,
                    insertwidth=3, padx=10,pady=10, relief ="raised", selectbackground="green3",
                    wrap="word")



# create a menu
def new_file():
      t=textPad.get("1.0", "end-1c")
      if t=="":
        label = tkMessageBox.showinfo("New File","   Your New File\nClick OK to Continue")
      else:
        result = tkMessageBox.askquestion("New File","You already save previous data!")
        if(result=="yes"):
          textPad.delete('1.0', "end-1c")
        else:
          t = textPad.get("1.0", "end-1c")
          savelocation=tkFileDialog.asksaveasfilename(title='Save File As',
          filetypes= (("Text Files","*.txt"),("All Files","*.*"),("All Files Linux","**")))
          file1=open(savelocation, "w+")
          file1.write(t)
          file1.close()
          textPad.delete('1.0', "end-1c")
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file',
          filetypes= (("Text Files","*.txt"),("All Files","*.*"),("All Files Linux","**")))
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_as_command():
    t = textPad.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename(title='Save File As',
          filetypes= (("Text Files","*.txt"),("All Files","*.*"),("All Files Linux","**")))
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "A Notepad created by Mudit Jain \n                Copyright      \n Nope! Make changes as you Want")


menu = Tkinter.Menu(root,activebackground="cyan3",bg="snow",activeborderwidth=3,
            activeforeground="magenta4",bd=2,cursor="man",disabledforeground="red",font="TkMenuFont 10 bold")
root.config(menu=menu)
filemenu = Tkinter.Menu(menu,bg="khaki",activebackground="blue violet",
          activeforeground="firebrick1")
menu.add_cascade(label="File", menu=filemenu,)
filemenu.add_command(label="New", command=new_file,)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_as_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Tkinter.Menu(menu,bg="khaki",activebackground="blue violet",
          activeforeground="firebrick1")
menu.add_cascade(label="Help", menu=helpmenu,)
helpmenu.add_command(label="About...", command=about_command,activebackground="dark blue",)
# end of menu creation

textPad.pack()
root.mainloop()
