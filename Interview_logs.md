# Beamery:
Question: https://leetcode.com/problems/fraction-to-recurring-decimal/description/
"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
0.012012...
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0

"""
#after you divide the integers -> float -> string
#hash set -> [0,1,2] [0,2,3]
#linked list -> 0 -> 1 -> 2 turtle rabbit 
#0 -> 1 -> 2 -> 0 -> 1 -> 2 
#^    ^ 
0.333333
#1/3 -> 3/1.0
0 1
1
#check the remainder for duplciates
#hashmap = {remmainder->digit}
14285
#1/7 -> 7|1.0
R = 3
30
20
R = 4
40 - 35
#142857 -> (142857)
#tracking sequence ->
1/2 0.5
         0.5
2| 1.0
1.0
0
numerator = 1
denominator = 2
remainder = 1
output = '0.'
map = {}
#loop through long division
while remainder != 0:
  #long division -> modulo function
  remainder = denominator % numerator
  remainder = numerator - remainder
  map[remainder] =  remainder
  print(map)
  #check for repeating
  #if remainder in map
  #multiply remainder by 10
  remainder= 10

# Google first round
Question: two sum
Q.1 >> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]


#hashmap - dictionary -> store what we look for in the next elements
{index:difference}
#{0:7,1:2,...}
0 , 1
map = {}
R = []
for i in range(len(nums)):
Diff = target - nums[i]
    Map[i] = Diff
    For k,v in Map.items()
        If map[k] == nums[i]:
            R.append((k,i))
Return R

# Peloton
#!/bin/python3

import math
import os
import random
import re
import sys

"""
    [1,18], [2,11], [4,15]
    
    base case-> len() == 0
        return 0
    
    1. order the lists based on the beginning time l[0] -> Arrays.sort[]
        2. Heap -> sort this by the max start time
            2a. pop and push based on the criteria here:
            3. l[1] compare l+1[0]
                3a. if l[1] == l+1[0] -> False
                3b. if l[1] < l+1[0] -> 4 < 6 -> False
                3c. if l[1] > l+1[0] -> 6 > 4 -> True  
            2b. maxx length of the heap
    [1,18] [2,11]
    heap -> [1,18]
    18 vs 2
        overlapping
        pushed on the heap
        heap -> [2,11], [1,18]
        2,11 vs 4,15
        heap -> [4,15] [2,11], [1,18]
        4,15 vs 5,13
        heap -> [5,13] ... -> len(4)
        5,13 vs [15,29]
        heap -> [15,29], [4,15]... -> len(4)
        15,29 vs  [18,23] -> len(5)?
        
    Time Complexity: O(n)*O(logn) + O(nlogn) n is the length of intervals
    O(nlogn)
    Space Complexiy: O(n) -> space of the heap n is the length of intervals
         
        
"""
import heapq
def minNumberOfInstructors(intervals):
    # Write your code here
    intervals.sort(key=lambda a: a[0])
    #compare i-1 and i
    hp = []
    #keeps track of the length of the heap
    m = 0
    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return 1
    #O(nlogn)
    heapq.heapify(hp)
    #O()
    heapq.heappush(hp, intervals[0])    
    for i in range(1, len(intervals)):
        l = hp[0]
        print(hp)
        if l[1] <= intervals[i][0]:
            #False
            #pop element then push the new element
            heapq.heappop(hp)
            #here 
            heapq.heappush(hp, intervals[i])
        elif intervals[i-1][1] > intervals[i][0]:
            #True
            #heappush an element into the maxheap
            heapq.heappush(hp, intervals[i])
        m = max(m, len(hp))
    print(m)
    print(hp)
    return m
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = minNumberOfInstructors(intervals)

    fptr.write(str(result) + '\n')

    fptr.close()

# Peloton 2nd Round
"""
In old times, there were no metro cards or tokens for the trains. People deposited their change and upon paying the full fare, the gate would open and change would be dispensed. We will model this from the standpoint of the turnstile.

Given:

-   The price of a ride (let us say 75 units/cents/pennies)
-   What coins are accepted by the machine (1, 5, 10, 25, similar to our current coinage, and also notably excluding 50 cent and dollar coins)
-   A sequence of coins seen by the machine (after all, the machine has no idea of the person putting the money in, only that money is coming in)

Write one or more functions to process the input and when the fare has been paid, open the gate (we will print the word "OPEN") and dispense the optimal (minimum coins) change (we will print the array of coins to dispense). The change is reliably taken by the person and is not used anywhere else.

c = [25, 25, 25, 5, 5, 25, 25, 25, 25, 25, 1, 25, 25, 25, 10, 10, 25]
     |---75---|  |--85, 10 back-| |--76, 1 back-| |--95, 20 back  -|
 
Expected Output:
OPEN
[] # no change
OPEN
[10] # note not [5, 5] or [5, 1, 1, 1, 1, 1]
OPEN
[1] # 1 penny back
OPEN
[10, 10] # 2 dimes returned

"""



"""


PRICE = 75
VALID_COINS = [1, 5, 10, 25]
c = [25, 25, 25, 5, 5, 25, 25, 25, 25, 25, 1, 25, 25, 25, 10, 10, 25]
#base case: if nothing return nothing
"""

""" 
    1. main fucntion:
        1a. for loop goes through every element
        1b. if the current sum (running count) = 75 or above
        1c. call min coins -> place into a list
        
    2. min coins(running count, price, accepted coins)
        2a. running count - price = diff
            2b. return the minimum coins to make up the difference
            [1, 5, 10, 25]
            [10,2,1,0]
            10
            running count
            while positive:
                for i in valid coins:
                    running count == 0:
                    
            
            10 
                10
            9 5 0 -15
        8 4 -x -x    
            
"""

def min_coins(running_count, PRICE, VALID_COINS):
    diff = running_count - PRICE
    r_c = 0
    temp = [0*len(VALID_COINS)]
    temp2 = [0*len(VALID_COINS)]
    for i in range(len(VALID_COINS)):
        r_c = VALID_COINS[i]
        while r_c >= 0:
            #
            r_c = r_c - VALID_COINS[i]
            if r_c >= 0:
                temp[i] += 1
        #once we hit a negative
        if r_c % VALID_COINS[i] !=0:
            temp2[i] = r_c
    # loop through the remainder o inside temp2
    # add the result to temp 1
    for i in range(len(temp2)):
        r_c = VALID_COINS[i]
        while r_c >= 0:
            #coins
            r_c = r_c - VALID_COINS[i]
            if r_c >= 0:
                temp[i] += 1
    #get the min inside temp
    #match that to type of coin
    r = ()
    curr_min = float('inf')
    for i in range(len(VALID_COINS))):
        if VALID_COINS[i] < curr_min:
            r = (VALID_COINS[i],temp[i])
    return r
        
        
        
        
    #[10,2,1,0]
    #[0,2,2,0]
    
    
            

if __name__ == "main":
    PRICE = 75
    VALID_COINS = [1, 5, 10, 25]
    c = [25, 25, 25, 5, 5, 25, 25, 25, 25, 25, 1, 25, 25, 25, 10, 10, 25]
    running_count = 0
    r = []
    r2 = []
    for i in range(len(c)):
        running_count += c[i]
        if running_count >= PRICE:
            l = []
            #call a function and return the coins
            l = min_coins(running_count, PRICE, VALID_COINS)
        r.append(l)
    #Sum of the coins here
    for a,b in r:
        r2.append([a] * b)
    return r2
    #[10,2] -? [10,10]

