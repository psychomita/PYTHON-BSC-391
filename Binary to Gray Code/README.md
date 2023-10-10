## Problem Statement :
Write a Python program to convert Binary to Gray code using function.

## Binary to Gray Code Conversion :
Binary Number is the default way to store numbers, but in many applications, binary numbers are difficult to use and a variety of binary numbers is needed. This is where Gray codes are very useful. 

Gray code has a property that two successive numbers differ in only one bit because of this property gray code does the cycling through various states with minimal effort and is used in K-maps, error correction, communication, etc.

    Binary : 0011
    Gray   : 0010

    Binary : 01001
    Gray   : 01101

### Algorithm :
1. The Most Significant Bit (MSB) of the gray code is always equal to the MSB of the given binary code.
1. Other bits of the output gray code can be obtained by XORing binary code bit at that index and previous index.
