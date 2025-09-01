FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5
def convert_to_celcius(farrenheit):
    celcius= (farrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius
def convert_to_farenheit(celcius):
    farrenheit= (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return farrenheit

temp=float(input("Enter your temperature:"))
type=input( "Is this in (C)elcius or (F)arenheit?").strip().upper() 
    
if type == 'C':
    Farenheit=convert_to_farenheit(temp)
    print(f"{temp} degrees Celcius is {Farenheit} degrees")
elif type =='F':
    Celcius=convert_to_celcius(temp)
    print(f"{temp} degrees Farenheit is {celcius} degrees")
else:
    print("Invalid input")
    
