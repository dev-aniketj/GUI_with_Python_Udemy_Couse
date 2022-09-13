import PySimpleGUIQt as s

myLayout = [
    [s.Text("Hello World")],
    [s.Text("My name is Aniket"), s.Button("Okay")],
    [s.Text("My age is 22.")]
]
window = s.Window(title='Hello World', size=(640, 480), layout=myLayout)
window.read()