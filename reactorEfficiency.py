## zad.2 Okreslanie sprawnosci reaktora

def reactor_efficiency(voltage, current, theoretical_max_power):
     generated_power = voltage * current
     percentageValue = (generated_power/theoretical_max_power)*100
     if percentageValue >= 80:
         return 'green'
     elif 60 <= percentageValue < 80:
         return 'orange'
     elif 30 <= percentageValue < 60:
         return 'red'
     else:
         return 'black'


vol = float(input('Enter the voltage: '))
curr = float(input('Enter current: '))
theoretical_max = float(input('Enter theoretical max power of the reactor: '))

efficiency = reactor_efficiency(vol, curr, theoretical_max)
print(f'The reactor efficiency is: {efficiency}')