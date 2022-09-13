# add widgets
import PySimpleGUIQt as s

myLayout = [
    [s.Text("Hello World"), s.Text("My name is Aniket Jain.")],
    [s.Button("Ok"), s.Button("Cancel")]
]
window = s.Window(title='Hello World', size=(640, 480), layout=myLayout)
window.read()
