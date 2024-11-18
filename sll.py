class Node:
      def __init__(self, data):
            self.data = data
            self.next = None

class SingleLinkList:
      def __init__(self):
            self.head = None
            self.size = 0

      def is_empty(self):
            return self.head is None
      
      def append(self, data):
            new_node = Node(data)
            if self.head is None:
                  self.head = new_node
            else:
                  current = self.head
                  while current.next:
                        current = current.next
                  current.next = new_node
            self.size += 1

      def prepend(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

      def delete(self, data):
            if self.head is None:
                  return False

            if self.head.data == data:
                  self.head = self.head.next
                  self.size -= 1
                  return True

            current = self.head
            while current.next:
                  if current.next.data == data:
                        current.next = current.next.next
                        self.size -= 1
                        return True
                  current = current.next
                  return False

      def search(self, data):
            current = self.head
            while current:
                  if current.data == data:
                        return True
                  current = current.next
                  return False

      def get_size(self):
            return self.size

      def print_list(self):
            elements = []
            current = self.head
            while current:
                  elements.append(str(current.data))
                  current = current.next
            print(" ->".join(elements) if elements else "Empty list.")            
