"""
Arjun Sehgal
To-Do List with Tkinter
22nd May 2020
"""

"""
https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
I used that for all of my imformation on the entry widget from Tkinter. I will explain every line where I used this source.
Everywhere it says box.get() is from here. box.get() is used to get whatever was typed into the entry widget called box, so you can think of it as the variable which stores whatever you type in that keeps changing.
"""



import tkinter as tk # lets python use the tkinter module, and calls it tk

items = []
itemsDone = []
labels = []
finishedTasks = []
percentage = 100
tasks = 0
totalTasks = 0
doneTasks = 0 # assigning a lot of empty lists and variables for later use

info = tk.Tk()
wn = tk.Tk()
percentWindow = tk.Tk()
finish = tk.Tk()
percentWindow.title("Percentage")
info.title("Info")
wn.title("To-Do List")
finish.title("Completed Tasks") # setting up windows, by making them and giving them titles

instructions = tk.Label(info, text = "To add an item, type the item into the entry box and click add.\nTo remove, type the corresponding number into the box and click remove.\n Eg, the top item on the list is 1, and the second is 2.\n If you type 2 and click remove, the second item will get removed.\nAll entries should have no more than 30 characters.", font = "Verdana 15")
instructions.pack() # making the instructions text and putting it on the window

percent = tk.Label(percentWindow, text = "You have done {}% of your total tasks!".format(percentage), font = "Verdana 20") # making the percentage text


def add(): # This is the function that will run whenever you click the add button
    global items
    global tasks
    global doneTasks
    global totalTasks
    global percent # setting variables to global
    if len(box.get()) >= 1: # making sure what you types was more than 0 characters
        if len(box.get()) <= 30: # making sure what you types was less than 31 characters
            items.append(box.get())
            tasks += 1
            totalTasks = tasks + doneTasks
            percentage = round( ( doneTasks / totalTasks ) * 100, 2)
            percent.destroy()
            percent = tk.Label(percentWindow, text = "You have done {}% of your total tasks!".format(percentage), font = "Verdana 20")
            percent.pack() # calculating the new percentage of everything you have done, and replaces the old text with the new one
            things = tk.Label(wn, text = "- {}".format(box.get()), font = "Verdana 30")
            things.pack() # puts the next item on the list
            labels.append(things)
            itemsDone.append(box.get()) 
            added = tk.Label(info, text = "Added!", font = "Verdana 20")
            added.pack() # telling you that it has been added, and puts it onto the window
        else:
            tooLong = tk.Label(info, text = "Too Long!", font = "Verdana 20")
            tooLong.pack() # this runs if the entry was over 31 characters. It tells you it was too long, and puts it on the window.
    else:
        empty = tk.Label(info, text = "Type something!", font = "Verdana 20")
        empty.pack() # this runs if the entry was 0 charactes. It tells you to type something, and it puts it on the screen.
    box.delete(0, len(box.get())) # This removes whatever was typed into the box, so you don't have to delete everything every time. SOURCE USED HERE.
    

def remove(): # This runs whenever you click the remove button.
    global percent
    global doneTasks
    global items
    global totalTasks
    global tasks # setting all the needed variables as global
    word = box.get()
    if len(itemsDone) != 0: # making sure there is something in the list
        try: # if there are any errors (eg, what you type is a string), it will not do this
            word = int(word)
            index = int(box.get()) - 1
            finished = tk.Label(finish, text = "- {}".format(itemsDone[index]), font = "Verdana 30")
            finished.pack() # makes the thing you removed move to the other window 
            itemsDone.remove(itemsDone[index])
            labels[index].destroy()
            labels.remove(labels[index])
            doneTasks += 1
            tasks -= 1
            totalTasks = tasks + doneTasks
            percentage = round (( doneTasks / totalTasks ) * 100, 2)
            percent.destroy()
            percent = tk.Label(percentWindow, text = "You have done {}% of your total tasks!".format(percentage), font = "Verdana 20")
            percent.pack() # updating what the percentage is
            removed = tk.Label(info, text = "Removed!", font = "Verdana 20")
            removed.pack() # tells you it has been removed
        except:
            NumberOnly = tk.Label(info, text = "Type a number that is in range!", font = "Verdana 20")
            NumberOnly.pack() # this will only run if there were errors in the previous section, it tells you that what you type should be a number, and that it should be in range and puts it on the screen
    else:
        nothing = tk.Label(info, text = "No items in list!", font = "Verdana 20")
        nothing.pack() # this only runs if you have nothing in the list, it tells you that there is nothing in the list and puts it on the screen
    box.delete(0, len(box.get())) # This removes whatever was typed into the box, so you don't have to delete everything every time.

    
percent.pack() # puts the percentage on the screen

box = tk.Entry(wn) # This makes the entry box, and assigns it to the window "wn"
box.pack() # This puts the entry box on the assigned window

buttonAdd = tk.Button(wn, text = "Add", font = "Verdana 20", command = add)
buttonAdd.pack() # makes the add button and puts it on the screen, assigns "add" as its function

buttonRemove = tk.Button(wn, text = "Remove", font=  "Verdana 20", command = remove)
buttonRemove.pack() # makes the remove button and puts it on the screen, assigns "remove" as its function

wn.mainloop()
finish.mainloop()
info.mainloop()
percentWindow.mainloop() # code will keep running until windows are closed
