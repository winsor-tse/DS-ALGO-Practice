class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
#create a double linked list here

def transverse(Linked_list):
    while Linked_list:
        print(Linked_list.value)
        Linked_list = Linked_list.next

def reverse(Linked_list):
    #use stack
    # Time: O(n)
    #Space: O(n)
    stk = []
    while Linked_list:
        stk.append(Linked_list.value)
        Linked_list = Linked_list.next
    while stk:
        print(stk.pop())
if __name__ == '__main__':
    l = LinkedList(1)
    l.next = LinkedList(2)
    l.next.next = LinkedList(3)
    l.next.next.next = LinkedList(4)
    #transverse(l)
    reverse(l)