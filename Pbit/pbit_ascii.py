#!/bin/python
#-*-coding:utf-8-*-
import Pbit.pbit_processing
import sys

class Pbit_ASCII():
    """
    class to convert between binary and ascii 
    """
    def __init__(self):
        self.processing = Pbit.pbit_processing.Pbit_Processing()

    def convert_ascii(self,Decimal_list,return_types="List"):
        """
        Fuction to convert ascii from hex

        Args:
            Decimal_list:
                        hex_list
            return_types:
                        return data of types

        return:
            ascii_condes
        """
        ascii_chars = []
        for codeic in Decimal_list:
            # convert ascii codes
            one_ascii = chr(int(codeic,16))
            ascii_chars.append(one_ascii)

        if return_types is "String":
            # join ascii code
            ascii_chars = "".join(ascii_chars)

        return ascii_chars 
 
    def pbit_asciis(self,Decimal,return_types="List"):
        """
        Function to asciils is main

        Args:
            Decimal:
                datas
            data_types:
                data is type
                data_type of default is hex
                binary
                ten 

            return_types:
                return type
                retrun_types of defalut is List
                str is String
        """
        # Create hex_lists 
        hex_list = self.processing.change_bin_hex(Decimal)
        # Convert ascii codes         
        Ascii_list=self.convert_ascii(hex_list,return_types)
        return Ascii_list

    def ascii_hex(self,strings):
        """
        Fuction to create from ascii to hex

        Args:
            strings: string data

        return:
            hex_list: hex list
                      ["0x54","0x45","0x53","0x54"]
        """

        hex_list = []
        try:
            for charcture in strings:
                chars = ord(charcture)
                hex_list.append(hex(chars))
        except TypeError:
            sys.exit("argument is not string")

        return hex_list


        
