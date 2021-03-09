class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = self.head

        while current_node is not None:
            if current_node.data == data:
                # node found, proceed to delete
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                current_node = None

            else:
                # move previous and current nodes
                if previous_node != current_node:
                    previous_node = previous_node.next

                current_node = current_node.next

    def print_contents(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end='')
            current_node = current_node.next
            if current_node is not None:
                print('->', end='')


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete(self, data):
        previous_node = self.head
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                # node found, proceed to delete
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next

                if current_node == self.tail:
                    self.tail = current_node.prev

                # update previous and next linkage
                if current_node.next is not None:
                    current_node.next.prev = previous_node

                # free up deleted node
                current_node = None

                self.head.prev = None
                self.tail.next = None
            else:
                # move previous and current nodes
                if previous_node != current_node:
                    previous_node = previous_node.next
                current_node = current_node.next

    def print_links(self):
        current_node = self.head
        while current_node is not None:
            if current_node.prev is not None:
                print(current_node.prev.data, '<-', end='')
            else:
                print('None<-', end='')

            print(current_node.data, end='')

            if current_node.next is not None:
                print('->', current_node.next.data, end='')
            else:
                print('->None', end='')

            current_node = current_node.next
            input()

        if self.head is not None:
            print('head: ', self.head.data, end='')
            print('tail: ', self.tail.data, end='')
