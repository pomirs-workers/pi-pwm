import os

class PWM:
    def __init__(self):
        pass

    def set(self, values):
        cmd = 'echo \"'
        for pin in values:
            cmd += str(pin) + '=' + str(values[pin]) + ';'

        cmd += '\" > /dev/pi-blaster'
        print(cmd)
        # os.system(cmd)



a = PWM()

a.set({
    1: 2.46,
    16: 0.3455
})