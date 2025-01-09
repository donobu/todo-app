import functions
import FreeSimpleGUI as fsg

label1 = fsg.Text("Type in a to-do ")
input1 = fsg.Input(tooltip="Enter a todo", key="to-do")
button1 = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key="to-dos",
                       enable_events=True, size=(44, 10))
edit_button = fsg.Button("Edit")

layout = [[label1], [input1, button1],
          [list_box, edit_button]]

window = fsg.Window("My To-do App", layout=layout, font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    """print(3, values['to-dos'][0])
    print(4, values['to-do'])"""
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # update the listbox instance when the user add a new value on the input box and click on
            # add button
            window['to-dos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['to-dos'][0]
            new_todo = values['to-do']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            # update the listbox instance with a key named to-dos when the user click on edit with
            # anything on the input box
            window['to-dos'].update(values=todos)
        case "to-dos":
            # update the input box instance with a key named to-do when the listbox is clicked
            window['to-do'].update(value=values['to-dos'][0])
        case fsg.WIN_CLOSED:
            break



window.close()