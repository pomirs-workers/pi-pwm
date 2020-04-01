import os


class PWM:
    def __init__(self):
        pass

    @staticmethod
    def set(values):
        cmd = 'echo \"'
        for pin in values:
            cmd += str(pin) + '=' + str(values[pin]) + ';'
        cmd += '\" > /dev/pi-blaster'
        os.system(cmd)
