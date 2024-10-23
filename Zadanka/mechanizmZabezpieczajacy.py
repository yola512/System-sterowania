## zad.3 mechanizm zabezpieczajacy przez przeciazeniem i stopieniem reaktora

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    if value < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= value <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'

temp = float(input('Enter the temperature of the reactor: '))
neutronsPerSec = int(input('How many neutrons are produced per second?: '))
threshold_value = float(input('Enter the threshold value: '))

print(fail_safe(temp, neutronsPerSec, threshold_value))