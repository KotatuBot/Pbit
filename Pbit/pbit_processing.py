import binascii

class Pbit_Processing():
    def __init__(self):
        pass

    def change_bin_hex(self,data):
        """
        A function that converts a binary or character string into a two-digit delimited hexadecimal list
        Args:
            data: binary or string data

        Returns: 
            hex_py_list: list of python
                ["0x34","0x35","0x35"]
        """
        if type(data) is bytes:
            data = data.decode("utf-8")

        # str-->slice
        slice_data = list(data)
        slice_length = len(slice_data)
        
        hex_py_list = []
        for number in range(0,slice_length,2):
            tip_list = slice_data[number:number+2]
            hexs = "0x" + tip_list[0]+tip_list[1]
            hex_py_list.append(hexs)

        return hex_py_list

    def change_hex_bins(self,data):
        """
        Function to convert hexadecimal to binary string
        Args:
            data:hex_list or binary_strings

        retrun:
            binally_strings: bin_strings
        """
        if type(data) is list:
            data_kari = ""
            for one_data in data:
                data_kari+=one_data[2:]
            data = data_kari
        # binary case
        binally_data = data.encode("utf-8")
        # binarys
        binally_strings = binascii.unhexlify(binally_data)
        return binally_strings

    def align_to_four_digits_hex(self,hex_list):
        """
        A function that converts a list of hexadecimal numbers to a four-digit hexadecimal list
        Args:
            hex_list: ['0x30','0x35','0x0000']

        return:
            four_hex_list: ['0x3035',0x0000]
        """
        hex_strings = "".join(hex_list)
        hex_string_char = "".join(hex_strings.split("0x"))
        hex_length = len(hex_string_char)
        four_hex_list = []
        for number in range(0,hex_length,4):
            four_hex_list.append("0x"+hex_string_char[number:number+4])

        return four_hex_list

