################################
#Kyle Kruskamp Advamced Web Developement MWF : 8AM - 850AM
################################

#stringCount FxN
#def stringCount(aList):
#    aList.sort()
#    new_array = []
#    x = 0
#    i = 0
#
#    while x < len(aList):
#        dup = aList[x]
#        if dup not in new_array:
#                new_array.append(dup)
#        x += 1
#
#    while i < len(new_array):
#        d = aList.count(new_array[i])
#        i += 1

#stringCount FxN using dict
def stringCount(aList):
    import collections
    nList = collections.Counter(aList)
    for key, val in sorted(nList.items()):
        print (key, val)
    return None

################################
#isFloat FxN
def isFloat(str):

    try:
        float(str)
        #print(1)
        return True

    except ValueError:
        #print(0)
        return False

################################
#linkedList
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def printLL(self):
        current = self.head
        while current:
            print(current.get_data(), end = " ")
            current = current.get_next()
        print("")

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
                if current.get_data() == data:
                    found = True
                else:
                    previous = current
                    current = current.get_next()

                if current is None:
                    raise ValueError("Data not in list")

                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
