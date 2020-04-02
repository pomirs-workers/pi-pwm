import os

class PWM:
    def __init__(self, pin):
        self.pin = pin

    def set(self, value):
        cmd = 'echo \"' + str(self.pin) + '=' + str(value) + '\" > /dev/pi-blaster'
        print('use ' + cmd)
        os.system(cmd)
