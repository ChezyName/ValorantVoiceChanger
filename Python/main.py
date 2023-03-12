from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key

def on_press(key):
    print("Key pressed: {0}".format(key))
    if(key == Key.esc): return False

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse presseed: {0}'.format(button))


# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()