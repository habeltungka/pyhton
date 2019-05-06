from pynput.keyboard import Key, Listener
import pynput

st = "s"


def on_press(key):
    global st
    run_key = "g"
    stop_key = "s"
    k = str(key).replace("'", "")
    if k == run_key:
        if st == stop_key:
            print("go Run")
            st = "g"
        else:
            print("already Run!")
    if k == stop_key:
        if st == run_key:
            print("stop Run")
            st = "s"
        else:
            print("already stop!")


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
