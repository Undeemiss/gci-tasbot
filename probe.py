from pynput import mouse
from pynput import keyboard

controller = keyboard.Controller()

def on_click(x, y, button, pressed):
    if button == mouse.Button.button9 and pressed == True:
        print(f"({x}, {y})")

    
try:
    print('Enabling hotkey')
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print('\nExiting')