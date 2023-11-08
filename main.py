# pip install keyboard
# pip install pybricks-stubs

import keyboard
from pybricks.hubs import PrimeHub
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

hub = PrimeHub()
motor_A = Motor(Port.A)
motor_B = Motor(Port.B)
motor_C = Motor(Port.C)

pressed_keys = set()
control_keys = {'w', 'a', 's', 'd'}
servo_position = 0
servo_angle = 0.25
def on_key_event(e):
    global servo_position
    if e.event_type == keyboard.KEY_DOWN:
        if e.name in control_keys:
            keyboard.press_and_release('backspace')
            hub.display.text(e.name)
        if e.name == 'w' and e.name not in pressed_keys:
            print("Forward")
            motor_A.run(1000)
            motor_B.run(1000)
        if e.name == 's' and e.name not in pressed_keys:
            print("Backward")
            motor_A.run(-100)
            motor_B.run(-100)
        if e.name == 'a' and 'd' not in pressed_keys and e.name not in pressed_keys:
            print("Left")
            target_angle = abs(servo_position)+servo_angle
            motor_C.run_target(100, -target_angle)
            servo_position = -target_angle
        if e.name == 'd' and 'a' not in pressed_keys and e.name not in pressed_keys:
            print("Right")
            target_angle = abs(servo_position)+servo_angle
            motor_C.run_target(100, target_angle)
            servo_position = target_angle
        pressed_keys.add(e.name)
    elif e.event_type == keyboard.KEY_UP:
        if e.name == 'w' or e.name == 's' and e.name in pressed_keys:
            motor_A.stop()
            motor_B.stop()
        if e.name == 'a' or e.name == 'd' and e.name in pressed_keys:
            motor_C.run_target(100, 0)
            servo_position = 0
        if e.name in pressed_keys:
            pressed_keys.remove(e.name)


keyboard.hook(on_key_event)
keyboard.wait()
