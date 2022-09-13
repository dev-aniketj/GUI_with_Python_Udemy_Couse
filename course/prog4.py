import PySimpleGUIQt as s

form = s.FlexForm("My first GUI")
myLayout = [
    [s.Text('Enter your name : ', size=(14, 0.75)), s.InputText()],
    [s.Text('Enter your age : ', size=(14, 0.75)), s.InputText()],
    [s.Text('Enter your email : ', size=(14, 0.75)), s.InputText()],
    [s.Text('Enter your city : ', size=(14, 0.75)), s.InputText()],
    [s.Ok(), s.Cancel()]
]
button, values = form.Layout(myLayout).Read()

print(f'My name is {values[0]}')
print(f'My age is {values[1]}')
print(f'My email is {values[2]}')
print(f'My city is {values[3]}')
