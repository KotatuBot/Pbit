import sys

import Pbit.pbit_conversion_check

class Pbit_Conversion():
    """
    変換系の関数を集めたモジュール
    """
    def __init__(self):
        self.pbit_check = Pbit.pbit_conversion_check.Pbit_Conversion_check()

    def convert_decimal(self,value):
        """
        This is a function to convert to decimal

        Args:
            value: Number to be converted

        return:
            ten_number: decimal
        """
        Negative_counter = 0
        value = str(value)
        
        #Negative_number_check
        if value[0] is "-":
            value = value[1:]
            Negative_counter = 1

        head_type = self.pbit_check.type_decimal_number(value)

        value = value[2:]

        if head_type is 'two':
            values = int(value,2)
            ten_number = self.pbit_check.check_negative(Negative_counter,values)
            return int(ten_number)

        elif head_type is 'sixteen':
            values = int(value,16)
            ten_number = self.pbit_check.check_negative(Negative_counter,values)
            return int(ten_number)

        elif head_type is "ten":
            sys.exit('This is value is not Binary number or Hexdecimal')

        else:
            sys.exit('Argument is not a numeric string ')
        
    def convert_binary(self,value):
        """
        This is a function to convert to Binary number 

        Args:
            value: Number to be converted

        return:
            two_number: Binary number
            
        """

        Negative_counter = 0
        value = str(value)

        #Negative_number_check
        if value[0] is "-":
            value = value[1:]
            Negative_counter = 1


        head_type = self.pbit_check.type_decimal_number(value)
        

        if head_type is not "ten":
            value = value[2:]
            
        if head_type is 'ten':
            values = bin(int(value))
            two_number = self.pbit_check.check_negative(Negative_counter,values)
            return two_number

        elif head_type is 'sixteen':
            values = bin(int(value,16))
            two_number = self.pbit_check.check_negative(Negative_counter,values)
            return two_number
        elif head_type is 'two':
            sys.exit('This is value is not Decimal number or Hexdecimal ')

        else:
            sys.exit("Argument is not a numeric string")

    def convert_hex(self,value):
        """
        This is a function to convert to Hexdecimal 

        Args:
            value: Number to be converted

        return:
            hex_number: Hexdecimal
        """
        Negative_counter = 0
        value = str(value)

        #Negative_number_check
        if value[0] is "-":
            value = value[1:]
            Negative_counter = 1

        head_type = self.pbit_check.type_decimal_number(value)

        if head_type is not "ten":
            value = value[2:]

        if head_type is 'ten':
            values = hex(int(value))
            hex_number = self.pbit_check.check_negative(Negative_counter,values)
            return hex_number

        elif head_type is 'two':
            values = hex(int(value,2))
            hex_number = self.pbit_check.check_negative(Negative_counter,values)
            return hex_number
        
        elif head_type is 'sixteen':
            sys.exit('This is value is not Decimal number or Binary number')
        else:
            sys.exit("Argument is not a numeric string")

    
