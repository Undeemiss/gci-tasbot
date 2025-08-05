from pynput import mouse
from pynput import keyboard

controller = keyboard.Controller()

def on_click(x, y, button, pressed):
    print(f"({x}, {y}) - {button} : {pressed}")

    
try:
    print('Enabling hotkey')
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print('\nExiting')