# Pbit

---

# Overview

Pbit is a library that helps to manipulate the numbers in Python

# Description

Pbit can perform conversion of the radix, calculation of the radix, 
computation of the checksum in IP · TCP · UDP, and inversion of the bit string.


## Modules 

+ Pbit.pbit_calculate.py
   + **addition(one_value,two_value)**  

        A function that enables addition between the same or different numbers
   + **subtraction(one_value,two_value)**  

        Functions that allow subtraction between the same or different numbers

+ Pbit.pbit_conversion.py
   + **convert_decimal(values)**  

        Function to convert binary or hexadecimal numbers to decimal number
   + **convert_binary(values)**   

        Function to convert decimal or hexadecimal to binary number
   + **convert_hex(value)**   

        Function to convert binary or decimal number to hexadecimal number

+ Pbit.pbit_bit_operation.py
   + **digit_alignment(values,digit)**   

        A function that adds 0 only to the digits when the specified digits are not enough to perform the digit 
   + **bit_inversion(values,digit)**  

        Function for inverting a bit string


+ Pbit.pbit_checksum.py
   + **calculate_checksum(hex_list,header)**  

        A function that can calculate a checksum from hexadecimal packet data. The checksum can be calculated by IP, TCP, UDP. However, the packet of the argument must be a hexadecimal value and it is a 4-digit delimiter. This can be done easily using Pbit.change_bin_hex () and Pbit.align_to_four_ digits_hex ().Also, if you do not specify 0x0000 as the value of the checksum, an error will occur.

+ Pbit.pbit_process.py
   + **change_bin_hex(data)**  

        A function that creates a two-delimited hexadecimal list by giving byte data and character strings of packets
   + **change_hex_bins(data)**   

        A function that can create a byte type string that can be used in Python 3 from a hexadecimal list or a character string
   + **align_to_four_digits_hex(hex_list)**  

        A function that creates a four-delimited hexadecimal list from two hexadecimal lists

+ Pbit.pbit_ascii.py
   +  **pbit_asciis(Decimal)**

        Function to convert hexadecimal binary to ASCII code
   +  **ascii_hex(strings)**

        Function to convert ASCII characters to hexadecimal list

# Usage
```python
In [1]: import Pbit.pbit_calculation
In [2]: caluculation = Pbit.pbit_calculation.Pbit_Calculation()
In [3]: caluculation.addition("0x34","0x37")
Out[3]: '0x6b'
In [4]: caluculation.addition("0x35",10)
Out[4]: '0x3f'
In [5]: caluculation.addition("0x35","0b11111111")
Out[5]: '0x134'
In [6]: caluculation.subtraction("0x6b","0x34")
Out[6]: '0x37'
In [7]: caluculation.subtraction("0x3f",10)
Out[7]: '0x35'
In [8]: caluculation.subtraction("0x134","0b11111111")
Out[8]: '0x35'



In [1]: import Pbit.pbit_conversion
In [2]: conversion = Pbit.pbit_conversion.Pbit_Conversion()
In [3]: conversion.convert_decimal("0x34")
Out[3]: 52
In [4]: conversion.convert_decimal("0x3f")
Out[4]: 63
In [5]: conversion.convert_decimal("0b11111111")
Out[5]: 255
In [6]: conversion.convert_binary(256)
Out[6]: '0b100000000'
In [7]: conversion.convert_binary(10)
Out[7]: '0b1010'
In [8]: conversion.convert_binary("0x34")
Out[8]: '0b110100'
In [9]: conversion.convert_binary("0x3f")
Out[9]: '0b111111'
In [10]: conversion.convert_hex(10)
Out[10]: '0xa'
In [11]: conversion.convert_hex(35)
Out[11]: '0x23'
In [12]: conversion.convert_hex("0b11111111")
Out[12]: '0xff'



In [1]: import Pbit.pbit_bit_operation
In [2]: operation = Pbit.pbit_bit_operation.Pbit_Bit_Operation()
In [3]: operation.digit_alignment("0b1111")
Out[3]: '0b0000000000001111'
In [4]: operation.digit_alignment("0b1111",Number_of_digits=8)
Out[4]: '0b00001111'
In [5]: operation.digit_alignment("0b1111",Number_of_digits=32)
Out[5]: '0b00000000000000000000000000001111'
In [6]: operation.digit_alignment("0x34",decimal_types="hex",Number_of_digits=8)
Out[6]: '0b00110100'
In [7]: operation.digit_alignment("0x34",decimal_types="hex",Number_of_digits=16)
Out[7]: '0b0000000000110100'
In [8]: operation.digit_alignment("0b1111")
Out[8]: '0b0000000000001111'
In [9]: operation.bit_inversion("0b1111")
Out[9]: '0b1111111111110000'
In [10]: operation.bit_inversion("0b1111",8)
Out[10]: '0b11110000'
In [11]: operation.bit_inversion("0b1111",digits=32)
Out[11]: '0b11111111111111111111111111110000'
In [12]: operation.bit_inversion("0x32")
Out[12]: '0b1111111111001101'
In [13]: operation.bit_inversion("0x32",digits=8)
Out[13]: '0b11001101'



In [1]: import Pbit.pbit_processing
In [2]: import Pbit.pbit_checksum
In [3]: processing = Pbit.pbit_processing.Pbit_Processing()
In [4]: checksum = Pbit.pbit_checksum.Pbit_Checksum()
In [5]: binary_data = "45100036092640004006cd84ac010602ac010603"
In [6]: hex_list = processing.change_bin_hex(binary_data)
In[7]: hex_list
Out[7]:
['0x45','0x10','0x00','0x36','0x09','0x26','0x40','0x00','0x40','0x06','0xcd','0x84','0xac','0x01','0x06','0x02','0xac','0x01','0x06','0x03']
In [8]: four_hex_list = processing.align_to_four_digits_hex(hex_list)
In [8]: four_hex_list
Out[8]:
['0x4510','0x0036','0x0926','0x4000','0x4006','0xcd84','0xac01','0x0602','0xac01','0x0603']
In [9]: ip_checksum= four_hex_list[5]
In [10]: ip_checksum
Out[10]: '0xcd84'
In [11]: four_hex_list[5] = "0x0000"
In [12]: four_hex_list
Out[12]:
['0x4510','0x0036','0x0926','0x4000','0x4006','0x0000','0xac01','0x0602','0xac01','0x0603']
In [13]: checksum.calculate_checksum(four_hex_list,"IP")
Out[13]: '0xcd84'
In [14]: binary = "45100036092640004006cd84ac010602ac010603041000173102d60e4174fb2a80188218000000000101080a000566bc00043c1a0d00"
In [15]:hex_list = processing.change_bin_hex(binary)
In[16]: hex_list
Out[16]: 
['0x45','0x10','0x00','0x36','0x09','0x26','0x40','0x00','0x40','0x06','0xcd','0x84','0xac','0x01','0x06','0x02','0xac','0x01','0x06','0x03','0x04','0x10','0x00','0x17','0x31','0x02','0xd6','0x0e','0x41','0x74','0xfb','0x2a','0x80','0x18','0x82','0x18','0x00','0x00','0x00','0x00','0x01','0x01','0x08','0x0a','0x00','0x05','0x66','0xbc','0x00','0x04','0x3c','0x1a','0x0d','0x00']
In [17]: four_hex_list = processing.align_to_four_digits_hex(hex_list)
In [18]: four_hex_list
Out[18]:
['0x4510','0x0036','0x0926','0x4000','0x4006','0xcd84','0xac01','0x0602','0xac01','0x0603','0x0410','0x0017','0x3102','0xd60e','0x4174','0xfb2a','0x8018','0x8218','0x0000','0x0000','0x0101','0x080a','0x0005','0x66bc','0x0004','0x3c1a','0x0d00']
In [19]: checksum.calculate_checksum(four_hex_list,"TCP")
Out[19]: '0x98dc'
In[20]:hex_list = ['0x4500', '0x0047','0x497f','0x0000','0xff11','0xdc70','0xc0a8','0x0a64','0xc0a8','0x0a01','0xee92','0x0035','0x0033','0x0000','0x1bc6','0x0100','0x0001','0x0000','0x0000','0x0000','0x0565','0x3336','0x3830','0x0464','0x7363','0x670a','0x616b','0x616d','0x6169','0x6564','0x6765','0x036e','0x6574','0x0000','0x0100']
In [21]: checksum.calculate_checksum(hex_list,"UDP")
Out[21]: '0xb2b7'

In [1]: import Pbit.pbit_ascii
In [2]: ascii = Pbit.pbit_ascii.Pbit_ASCII()
In [3]: ascii.pbit_asciis("3d4142")
Out[3]: ['=', 'A', 'B']
In [4]: ascii.ascii_hex("=AB")
Out[4]: ['0x3d', '0x41', '0x42']
```
# Author
[KotatuBot](https://github.com/KotatuBot)

