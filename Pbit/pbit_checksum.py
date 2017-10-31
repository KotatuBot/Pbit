import sys

import Pbit.pbit_calculation
import Pbit.pbit_bit_operation

class Pbit_Checksum():
    def __init__(self):
        self.calculate = Pbit.pbit_calculation.Pbit_Calculation()
        self.operation = Pbit.pbit_bit_operation.Pbit_Bit_Operation()

    def tcp_virtula_head(self,hex_list):
        """
        Function to create hexadecimal list of TCP pseudo header, 
        TCP header, TCP payload from binary data

        Args:
            hex_list: 
                    Four digit-separated list (from IP header to payload end)
        return:
            virtual_head:
                    Four digit hexadecimal data with pseudo header added
        """
        if len(hex_list) < 11:
            message = "\
                       The IP header is not included in the argument. To calculate TCP,\n \
                       payload values including IP header and TCP header are required. \n \
                       (IP header + TCP header + data)\
                       "
            sys.exit(message)
        IP_head = hex_list[:10]
        Payload = hex_list[10:]
        checksum = Payload[8]
        if checksum!="0x0000":
            sys.exit("Checksum is not 0x0000")
        source_IP_superior= IP_head[-4]
        source_IP_low_order = IP_head[-3]
        destination_IP_superior = IP_head[-2]
        destination_IP_low_order = IP_head[-1]
        tcp_type = "0x0006"
        ip_length = int(IP_head[0][3]) * 4
        packet_length_hex= hex((len(IP_head)+len(Payload))*2 - ip_length)
        padding_len = 6-len(packet_length_hex)
        padding = ""
        for i in range(padding_len):
            padding += "0"
        packet_length = "0x"+padding+packet_length_hex[2:]
        # 桁が奇数
        if len(Payload[-1]) is 4:
            Payload[-1]=Payload[-1]+"00"
        virtual_head = [source_IP_superior,source_IP_low_order,destination_IP_superior,destination_IP_low_order,tcp_type,packet_length]
        virtual_head.extend(Payload)

        return virtual_head

    def udp_virtual_head(self,hex_list):
        """
        A function to create a hexadecimal list of UDP pseudo header, 
        UDP header, UDP payload from binary data

        Args:
            hex_list: 
                    Four digit-separated list (from IP header to payload end)
        return:
            virtual_head:
                    Four digit hexadecimal data with pseudo header added
        """
        if len(hex_list) < 11:
            message = "\
                       The IP header is not included in the argument. To calculate UDP,\n \
                       payload values including IP header and UDP header are required. \n \
                       (IP header + UDP header + data)\
                       "
            sys.exit(message)
        IP_head = hex_list[:10]
        Payload = hex_list[10:]
        checksum = Payload[3]
        if checksum!="0x0000":
            sys.exit("Checksum is not 0x0000")
        source_IP_superior= IP_head[-4]
        source_IP_low_order = IP_head[-3]
        destination_IP_superior = IP_head[-2]
        destination_IP_low_order = IP_head[-1]
        udp_type = "0x0011"
        packet_length = Payload[2]
        # 桁が奇数
        if len(Payload[-1]) is 4:
            Payload[-1]=Payload[-1]+"00"
        virtual_head = [source_IP_superior,source_IP_low_order,destination_IP_superior,destination_IP_low_order,udp_type,packet_length]
        virtual_head.extend(Payload)
        return virtual_head


    def calculate_checksum(self,hex_number_lists,header="IP"):
        """
        Calculate the checksum from the list

        Args: 
            hex_number_lists: 4 digit hexadecimal list
                              ["0x4500","0x16ce","0x654c","0x4000","0x0111","0x0000","0xc0a8","0x651f","0xe000","0x001f"]
            
            checksums_place: Checksum location
                             IP --> IP header
                             TCP --> TCP header
                             UDP --> UDP header

        return:
                checksums: checksum
        """
        if header is "TCP":
            hex_number_lists = self.tcp_virtula_head(hex_number_lists)

        elif header is "UDP":
            hex_number_lists = self.udp_virtual_head(hex_number_lists)
        else:
            pass

        hex_score = hex_number_lists[0]
        for postion in range(1,len(hex_number_lists)):
            # First time processing
            hex_score = self.calculate.addition(hex_score,hex_number_lists[postion])
        # Invert bit string
        binary_number = self.operation.bit_inversion(hex_score)
        # change hexdecimal
        checksums = hex(int(binary_number[2:],2))

        return checksums
