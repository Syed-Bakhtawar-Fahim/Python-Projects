def Centrigrade():
    fahrenheit = int(input('Enter temperature in Fahrenheit\n'))
    return 5/9 * (fahrenheit - 32)

print(Centrigrade())

def Fahrenheit():
    Centigrade = int(input('Enter temperature in Centigrade\n'))
    return 9 / 5 *Centigrade + 32

print(Fahrenheit())

def Kelvin():
    Centigrade_1 = int(input('Enter temperature in Centigrade to Convert in Kelvin\n'))
    return Centigrade_1 + 273

print(Kelvin())
