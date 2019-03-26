import Tkinter

window = Tkinter.Tk()
window.title("GUI")

labelText = Tkinter.StringVar()
labelText.set("Bubble Sort")

def func(algorithm):
    labelText.set(algorithm)


optionList = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
optionVar = Tkinter.StringVar()
optionVar.set("Bubble Sort")
dropMenu = Tkinter.OptionMenu(window, optionVar, *optionList, command=func)
dropMenu.grid(column=1, row=6)
dropMenu.pack()

label = Tkinter.Label(window, textvariable=labelText)
label.pack()

window.mainloop()
