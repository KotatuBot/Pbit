import Pbit.pbit_numerical_test
import Pbit.pbit_bit_operation

class Pbit_Calculation():
    """
    ビット計算系の関数
    """
    def __init__(self):
        self.numerical = Pbit.pbit_numerical_test.Pbit_Numerical_Test()
        self.operation = Pbit.pbit_bit_operation.Pbit_Bit_Operation()

    def addition(self,one_value,two_value):
        """
        Addition of bit string

        Args: one_value: First argument
              two_value:　Second argument

        return:
                numbers: Total_value
        """
        types,two_value= self.numerical.check_convert(one_value,two_value)
        one_value,two_value = self.numerical.check_negative(one_value,two_value,types)

        numbers = ""

        if types is "sixteen":
            sums = int(one_value,16) + int(two_value,16)
            numbers = hex(sums)
            # Carry
            numbers = self.operation.carry_digit(numbers)

        elif types is "two":
            sums = int(one_value,2) + int(two_value,2)
            hex_digitamal = self.operation.carry_digit(hex(sums))
            if hex_digitamal[:2] == "0x":
                numbers = bin(int(hex_digitamal,16))
            else:
                numbers = bin(int(hex_digitamal,16))

        elif types is "ten":
            numbers = int(one_value) + int(two_value)

        else:
            print("This is strings")
            numbers = None

        return numbers


    def subtraction(self,one_value,two_value):
        """
        Function to perform subtraction

        Args:
            one_value: First value
            two_value: Second value

        return:
            number: Subtracted value
        """
        types,two_value= self.numerical.check_convert(one_value,two_value)
        one_value,two_value = self.numerical.check_negative(one_value,two_value,types)

        numbers = ""

        if types is "sixteen":
            sums = int(one_value,16) - int(two_value,16)
            numbers = hex(sums)

        elif types is "two":
            sums = int(one_value,2) - int(two_value,2)
            numbers = bin(sums)

        elif types is "ten":
            numbers = int(one_value) - int(two_value)

        else:
            print("This is strings")
            numbers = None

        return numbers


