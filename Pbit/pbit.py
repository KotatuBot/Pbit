import binascii

class Pbit():
    """
    The pbit module was created to solve the annoyance of 
    the progress in Python.

    In the pbit module, 
    conversion and calculation of binary numbers, decimal numbers, and hexadecimal numbers can be executed smoothly.

    It also holds negative numbers handling in decimal, digit alignment, bit inversion, checksum calculation function, and so on.
    """

    def __init__(self):
        pass

    def pbit_help(self):
        pbit_message = """

        The pbit module was created to solve the annoyance of 
        the progress in Python.

        In the pbit module, 
        conversion and calculation of binary numbers, decimal numbers, and hexadecimal numbers can be executed smoothly.

        It also holds negative numbers handling in decimal, digit alignment, bit inversion, checksum calculation function, and so on.
                       """

        print(pbit_message)

        


if __name__ == "__main__":
    pd = Pbit()
    pd.pbit_help()

    
