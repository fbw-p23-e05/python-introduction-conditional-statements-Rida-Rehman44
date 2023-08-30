string = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius:")
number = int(input("Input the value of temperature you'd like to convert  :"))
if (string == "C"):
    C = ((number - 32)/9)*5
    print("Temperature in Celcius", C)
else :
    F = ((number +32)/5) *9   
    print("Temperature in Fehrenheit", F)
