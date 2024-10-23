
## zad.1 Czy reaktor jest krytyczny?

def is_criticality_balanced(temperature, neutronsPerSec):
   value = temperature * neutronsPerSec
   if temperature < 800 and neutronsPerSec > 500 and value < 500000:
     return True
   else:
     return False

temp = float(input('Enter the temperature: '))
neutronsPerSec = int(input('Enter how many neutrons are emitted per second: '))

print(is_criticality_balanced(temp, neutronsPerSec))