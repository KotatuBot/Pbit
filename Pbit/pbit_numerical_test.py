import Pbit.pbit_conversion_check 
import Pbit.pbit_conversion

class Pbit_Numerical_Test():
    """
    計算前の検査を行う関数
    """
    def __init__(self):
        self.check = Pbit.pbit_conversion_check.Pbit_Conversion_check()
        self.conversion = Pbit.pbit_conversion.Pbit_Conversion()

    def check_convert(self,one_value,two_value):
        """
        A function that checks whether the argument type is the same

        Arg:
            one_value: First value
            two_value: Second value

        return:
            one_type:　The first type(two,sixteen,ten)
            two_value: Value according to the first type


        """
        one_type = self.check.type_decimal_number(one_value)
        two_type = self.check.type_decimal_number(two_value)
        if one_type is not two_type:
            if one_type is "two":
                two_value = self.conversion.convert_binary(two_value)
            elif one_type is "sixteen":
                two_value = self.conversion.convert_hex(two_value)
            elif one_type is "ten":
                two_value = self.conversion.convert_decimal(two_value)
            else:
                pass
        return one_type,two_value

    def check_negative(self,one_value,two_value,types):
        """
        A function that checks whether it is a negative number

        Args:
            one_value: First value
            two_value: Second value
            types: First value of type

        return:
            one_value: First value
            two_value: Second value
        """
        # hex or sixteen 
        if types is "sixteen" or types is "two":
            # one_value and two_value is Negative
            if one_value[0] is "-" and two_value[0] is "-":
                one_value = one_value[0] + one_value[3:]
                two_value = two_value[0] + two_value[3:]
            # one_value is Negative
            elif one_value[0] is "-":
                one_value = one_value[0] + one_value[3:]
                two_value = two_value[2:]
            # two_value is Negative
            elif two_value[0] is "-":
                one_value = one_value[2:]
                two_value = two_value[0] + two_value[3:]
            # plus
            else:
                one_value = one_value[2:]
                two_value = two_value[2:]

        return one_value,two_value

