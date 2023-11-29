"""
Készítsen egy olyan szabványos ANSI C függvényt, amely visszatérési értékül egy double szám n-edik byte-ja medik bitjét szolgáltatja. 
Bemenő paraméterek: maga a double típusú valós szám, valamint n és m értéke, amelyek 1 és 8
közötti egészek. 
"""
import struct

def ansi_c(num, n, m):
    if n < 1 or n > 8 or m < 1 or m > 8:
        return None
    
    if type(num) not in[float, int]:
        return None 
    
    get_byte = struct.pack('d', num)
    
    byte_n = get_byte[n - 1]

    bit_value = (byte_n >> (m - 1)) & 1

    return bit_value

num = 123.456
n = 2
m = 3
bit_value = ansi_c(num, n, m)

if bit_value is not None:
    print(f"The {n}-th byte {m}-th bit in the given double is: {bit_value}")

















