import sys

Temp = int(input('Temperature: '))

if Temp <= 50:
	velocity = int(input('wind velocity: '))
	w = int(35.74+(0.6215*Temp)+((0.4275*Temp)-35.75)*velocity**0.16)
	print(w)

if Temp > 50:
	print ('Error, temperature can only be 50 degrees or below')
