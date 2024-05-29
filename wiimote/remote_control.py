import gpiozero
import cwiid
import time

robot = gpiozero.Robot(left=(5,6), right=(13,19))

red = gpiozero.LED(18)
green = gpiozero.LED(23)
blue = gpiozero.LED(24)

print("Press and hold the 1+2 buttons on your Wiimote simultaneously")
blue.blink(0.25, 0.25)
wii = cwiid.Wiimote()
print("Connection established")
blue.off()
green.on()
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

mode = 'BTN'

while True:
	buttons = wii.state["buttons"]

	if (buttons & cwiid.BTN_HOME):
		print('Exiting')
		break
	
	if (buttons & cwiid.BTN_MINUS and mode == 'BTN'):
		print('1: Accelerometer mode')
		green.off()
		red.on()
		mode = 'ACC'
	if (buttons & cwiid.BTN_PLUS and mode == 'ACC'):
		print('2: Button mode')
		red.off()
		green.on()
		mode = 'BTN'

	if (mode == 'ACC'):
		x = (wii.state["acc"][cwiid.X] - 95) - 25
		y = (wii.state["acc"][cwiid.Y] - 95) - 25
		print(x, y)
		continue

	if (buttons & cwiid.BTN_LEFT):
		print('Left')
		robot.left()
	if (buttons & cwiid.BTN_RIGHT):
		print('Right')
		robot.right()
	if (buttons & cwiid.BTN_UP):
		print('Forward')
		robot.forward()
	if (buttons & cwiid.BTN_DOWN):
		print('Backward')
		robot.backward()
	if (buttons & cwiid.BTN_B):
		print('B')
		robot.stop()
	
