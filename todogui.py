import functions
import FreeSimpleGUI as fsg

label1 = fsg.Text("Type in a to-do ")
input1 = fsg.InputText(tooltip="Enter a todo")
button1 = fsg.Button("Add")

layout = [[label1], [input1, button1]]

window = fsg.Window("My To-do App", layout=layout)
window.read()
window.close()