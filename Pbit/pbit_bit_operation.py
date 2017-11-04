import sys

import Pbit.pbit_conversion_check

class Pbit_Bit_Operation():
    """
     ビット操作を行う関数
    """
    def __init__(self):
        self.conversion_check = Pbit.pbit_conversion_check.Pbit_Conversion_check()

    def digit_alignment(self,number,decimal_types="Binary",Number_of_digits=16):
        """
        Function for matching the number of digits

        Args:
            number: Binary_number or hexdecimal
            decimal_type: The default is binary.
            　　　　　　　In case of hexadecimal, pass "hex"
                        　
                        　hex -- > hexdecimal
                          Binary --> Decimal number
            Number_of_digits: Number of digits to match
                              default -->16
                              Value　available for 4,8, 16, 32, 64, 128

        return:
               sixteen_digit_binay_number:　Fix to 16 digit binary number
                                            "0b00000000000000000000000000000000001"
        """
        #Number of digits is 8,16,32,64,128
        if Number_of_digits is not 4 and Number_of_digits is not 8 \
           and Number_of_digits is not 16 and Number_of_digits is not 32\
           and Number_of_digits is not 64 and Number_of_digits is not 128:
           sys.exit("The number of digits is not one of 4,8, 16, 32, 64, 128")
            
        try:
            if decimal_types == "hex":
                Binary_numbers = bin(int(number,16))
                str_binary = str(Binary_numbers)
            else:
                str_binary = str(number)

            binary_payloads = str_binary[2:]

            # Determine whether there are Number_of_digits
            if len(binary_payloads)!=Number_of_digits:
                # Determine number of missing digits
                zero_str_len = Number_of_digits-len(binary_payloads)
                if zero_str_len < 0:
                    sys.exit("The digit of the original number exceeded the set number of digits")
                zero_str = ''

                # Fill in missing digits with zeros
                for counters in range(zero_str_len):
                    zero_str+="0"

                # digit_binary_number
                digit_binary_number = "0b" + zero_str + binary_payloads
                return digit_binary_number
            else:
                digit_binay_number = "0b" + binary_payloads
                return digit_binay_number

        except ValueError:
            sys.exit("Argument is not Binary number or hexdecimal")

    def carry_digit(self,numbers):
        """
        A function that adds one to a numerical value in case of carry

        Args:
            numbers: hexdiecimal

        return:
            numbers: carry number
        """
        # Carry
        if len(numbers) == 7:
            hex_cuts = "0x"+numbers[3:]
            # Add one
            updigit = int(hex_cuts,16)+int("0x0001",16)
            numbers = hex(updigit)
            return numbers
        else:
            return numbers

    def bit_inversion(self,bit_number,digits=16):
        """
        Function to invert a bit string

        Args:
            bit_number: Binary number or hexdecimal
                        "0b10101"
                        "0xA"
            digits: Number of digits to match
                    default -->16
                    Value　available for 4,8, 16, 32, 64, 128


        return:
            Inversion_number: Binary string inverted bit string
            　　　　　　　　　"0b111111111111110101"
            
        """
        head_type = self.conversion_check.type_decimal_number(bit_number)
        if head_type is "two":
            sixteen_degit = self.digit_alignment(bit_number,Number_of_digits=digits)

        elif head_type is "sixteen":
            sixteen_degit = self.digit_alignment(bit_number,"hex",Number_of_digits=digits)
        else:
            pass

        sixteen_degit = sixteen_degit[2:]
        
        try:
            Inversion_number = ""
            for digit in sixteen_degit:
                if digit=="1":
                    Inversion_number+="0"
                else:
                    Inversion_number+="1"

            return "0b"+Inversion_number
        except ValueError:
            print("This is not Binary number or hexdecimal")


