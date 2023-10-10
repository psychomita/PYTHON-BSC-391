## Problem Statement :
Write a Python program that prints out the first n rows of Pascal's triangle.

## Pascal's Triangle :
Pascal’s triangle is a triangular array of binomial coefficients. The number of entries in every line is equal to line number. For example, the first line has “1”, the second line has “1 1”, the third line has “1 2 1”,.. and so on. Every entry in a line is value of a Binomial Coefficient. The value of ith entry in line number line is C(line, i). The value can be calculated using following formula :-

```
C(line, i) = line! / ( (line-i)! * i! )
```
![image](https://github.com/psychomita/BSC-391/assets/133328192/74c51a47-34ad-4b56-956e-917c998e50c0)

### Algorithm:

+ Run a loop for each row of pascal’s triangle i.e. 1 to N.
+ For each row, run an internal loop for each element of that row.
+ Calculate the binomial coefficient for the element using the formula mentioned in the approach.
