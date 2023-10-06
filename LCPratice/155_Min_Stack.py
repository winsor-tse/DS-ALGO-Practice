"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
https://leetcode.com/problems/min-stack/editorial/

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:
    import collections
    def __init__(self):
        self.stack = []
    def push(self, x) -> None:
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return
        """
        Structure is [curr, curr_min]
        [12,12] [30,12] [7,7] [6,6]
        popping this would be min is 6 and curr is 6
        popping again would be min is 7 curr is 7
        getting mim after that would be 12
        This is so when popping an element you can see what the previous min would be in the past
        """
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
    def pop(self) -> None: #removes the element on the top of the stack.
        self.stack.pop()
        #check for Min
    def top(self) -> int: #gets the top element of the stack.
        return self.stack[-1][0]
    def getMin(self) -> int: #retrieves the minimum element in the stack.
        return self.stack[-1][1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print('hello')