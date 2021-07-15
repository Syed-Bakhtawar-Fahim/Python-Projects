# Convert fahrenheit to Centigrade

class Temperature():


    #class objec attributes

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
        # self.minor_axis = minor_axis


    def conversion(self):
        return 5/9 * (self.fahrenheit - 32)



my_Temperature = Temperature(fahrenheit=float(input('Enter temperature in Fahrenheit\n')))

print(f'The Temperature in Centigrage is', my_Temperature.conversion())

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# Convert Centigrade to fahrenheit

class Temperature_1():

    # class objec attributes

    def __init__(self, Centigrade):
        self.Centigrade = Centigrade
        # self.Kelvin = Kelvin

    def conversion_Centigrade(self):
        return 9 / 5 *self.Centigrade + 32




my_Temperature_1 = Temperature_1(Centigrade=float(input('Enter temperature in Centigrade\n')))
#     def conversion_Kelvin(self):
#         return Centigrade + 273
#
print(f'The Temperature in Fahrenheit is', my_Temperature_1.conversion_Centigrade())



# Conversion of kelvin and fahrenheit


class Temperature_2():

    # class objec attributes

    def __init__(self, Centigrade):
        self.Centigrade = Centigrade


    def conversion_Centigrade(self):
        return 9 / 5 *self.Centigrade + 32


    # def __int__(self, kelvin):
    #     self.kelvin = kelvin
    #
    # def kelvin_con(self):
    #     return my_Temperature_2.kelvin_con() + 273




my_Temperature_2 = Temperature_2 (Centigrade=float(input('Enter temperature in Centigrade\n')))
print(f'The Temperature in Fahrenheit is', my_Temperature_2.conversion_Centigrade())
print(f'The Temperature in Kelvin is', my_Temperature_2.conversion_Centigrade() + 273)


#     def conversion_Kelvin(self):
#         return Centigrade + 273
#