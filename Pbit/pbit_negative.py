class Pbit_Negative():
    """
    負の数に関する関数
    """
    def __init__(self):
        pass

    def negative_number(self,plus_number):
        """
        Function returning negative number

        Args:
            plus_number: Plus number
        
        Return:
                negative_numbers: negative number
        """
        negative_numbers = "-"+str(plus_number)
        return negative_numbers

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


