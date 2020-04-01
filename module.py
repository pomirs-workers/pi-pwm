def parse(string):
    rules = string.split(' ')
    result_dict = {}
    for rule in rules:
        if rule != '':
            [rule_for, rule_val] = rule.split('=')
            result_dict[int(rule_for)] = float(rule_val)
    return result_dict


def stringify(rules):
    result_string = ''
    for rule in rules:
        result_string += str(rule) + '=' + str(rules[rule]) + ' '
    return result_string


class PWM:
    def __init__(self, pin, path='/dev/pi-blaster'):
        self.pin = pin
        self.path = path

    def set(self, value):
        i = open(self.path, 'r')
        now = i.read()
        i.close()
        parsed = parse(now)
        parsed[self.pin] = value
        o = open(self.path, 'w')
        o.write(stringify(parsed))
        o.close()
