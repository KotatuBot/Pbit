class Pbit_Conversion_check():
    """
    変換前にチェックを行う関数
    """
    def __init__(self):
        pass

    def type_decimal_number(self,value):
        """
        Inspect the type of decimal　function
        
        Args:
            value: The radix of the test object

        return:
                transfer:　Type of Decimal
                           two -- > Binary number
                           sixteen -- > Hexadecimal
                           ten -- > Decimal number
                           None -- > Other than decimal numbers
        """

        value = str(value)
        # Negative
        if value[0] is "-":
            # get header
            head_identifer = value[1:3]
        else:
            # get header
            head_identifer = value[0:2]
        transfer = None

        # Binary number
        if head_identifer == '0b':
            transfer = 'two'
        # Hexdecimal
        elif head_identifer == '0x':
            transfer = 'sixteen'
        else:
            pass

        try:
            # None
            if transfer==None:
                # convert int
                int(value)
                return 'ten'
        except :
            pass

        return  transfer

    def check_negative(self,Negative_counter,values):
        """
        Fuction to add Negative

        Args:
            Negative_counter: check Negative
            values: value

        retun:
            values: value
        """
        #Negative_number_add
        if Negative_counter is 1:
            values = "-"+str(values)

        return values
 
