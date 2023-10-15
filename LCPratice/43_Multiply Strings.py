"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Time: O(n1) + O(n2) where n1 and n2 is length of the string
        Space: O(n1) + O(num2)
        """
        import collections
        m ={
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        n1 = collections.deque()
        n2 = collections.deque()
        f1 = ""
        f2 = ""
        for i in range(len(num1)):
            n1.append(m[num1[i]])
        for i in range(len(num2)):
            n2.append(m[num2[i]])
        for i in range(len(n1)):
            f1 = f1 + str(n1[i])
        for i in range(len(n2)):
            f2 += str(n2[i])
        return str(int(f1)*int(f2))
    
if __name__ == "__main__":
    print('hi')