#LinkedList Program which performs most operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return
        if list2.head is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = list2.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage:
list1 = LinkedList()
list1.insert(3)
list1.insert(1)
list1.insert(2)
list1.display()  # Output: 2 1 3

list2 = LinkedList()
list2.insert(5)
list2.insert(9)
list2.insert(7)
list2.delete(7)
list2.display() #Output: deletion from 5 9 7 to 5 9

list4 = LinkedList()
list4.insert(3)
list4.insert(4)
list4.insert(5)
list4.traverse() #Traverse the list

list3 = LinkedList()
list3.insert(6)
list3.insert(5)
list3.insert(4)
list3.display()  # Output:insertion from a blank list created 4 5 6

list1.concatenate(list3)
list1.display()  # Output: 2 1 3 4 5 6
