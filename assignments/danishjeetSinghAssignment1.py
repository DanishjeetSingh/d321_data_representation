# I understand that the code may be difficult to understand at first glance,
# but please let me know if there is anything specific that you would like me to clarify.
# I am happy to provide any additional information that may be helpful.

# Question 2
# -----------------------------------------------------------------------------
def merge_sort(arr):
    # base case - if the array has one or zero element, it is already sorted
    if len(arr) <= 1:
        return arr
    # divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)
    # merge the sorted halves back together
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    # iterate through both lists and add the smaller element to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # add any remaining elements from the left and right lists to the result
    result += left[i:]
    result += right[j:]
    return result


# -----------------------------------------------------------------------------

# Question 3
# -----------------------------------------------------------------------------

from collections import Counter  # import the Counter function from the collections module


def frequencyCount(A):  # define a function named frequencyCount that takes in a list A
    count = Counter(A)  # create a count variable that calls the Counter function on A
    return [(a, n) for a, n in count.items() if n > 0]
    # return a list of tuple where the first element of tuple is the element and second element
    # is the number of times it appears in the list, for elements that appear more than 0 times in the list.


# -----------------------------------------------------------------------------

# Question 4
# -----------------------------------------------------------------------------

# Binary trees data structure
# We use Python dictionaries to represent a tree
# {root: value, left: a tree, right: a tree}

def emptyTree():
    return {}


def makeTree(value, left, right):
    return {'value': value, 'left': left, 'right': right}


def leaf(value):
    return makeTree(value, emptyTree(), emptyTree())


def root(tree):
    return tree['value']


def left(tree):
    return tree['left']


def right(tree):
    return tree['right']


def isEmpty(tree):
    if tree == {}:
        return True
    else:
        return False


# compute the height of a binary tree
def height(tree):
    if isEmpty(tree):
        return 0
    else:
        return 1 + max(height(left(tree)), height(right(tree)))


# compute the size (number of nodes) in a binary tree

def size(tree):
    if isEmpty(tree):
        return 0
    else:
        return 1 + size(left(tree)) + size(right(tree))


# determine if an element is in a binary tree
# def isIn(element, tree):
#     if isEmpty(tree): return False
#     if element == root(tree):
#         return True
#     else:
#         return isIn(element, left(tree)) or isIn(element, right(tree))

# saad azeem helped me with these 2 functions below

def Descendant(tree, element):
    # Check if the tree is empty, return empty list if it is
    if isEmpty(tree): return []

    # Check if the current node is the element we are looking for
    if root(tree) == element:
        # Check if the left subtree is empty and right subtree is not
        if not isEmpty(left(tree)) and isEmpty(right(tree)):
            # Return the root of the tree and the descendants of the left subtree
            return [root(tree)] + [Descendant(left(tree), root(left(tree)))]
        # Check if the right subtree is empty and left subtree is not
        elif isEmpty(left(tree)) and not isEmpty(right(tree)):
            # Return the root of the tree and the descendants of the right subtree
            return [root(tree)] + [Descendant(right(tree), root(right(tree)))]

        # Check if both left and right subtrees are not empty
        elif not isEmpty(left(tree)) and not isEmpty(right(tree)):
            # Return the root of the tree and the descendants of both the left and right subtrees
            return [root(tree)] + [Descendant(left(tree), root(left(tree)))] + [
                Descendant(right(tree), root(right(tree)))]

        # If no children left
        else:
            return [root(tree)]

    # Check if element is greater than root of the tree
    elif element > root(tree):
        # Call function on right subtree
        return [Descendant(right(tree), element)]

    # Check if element is less than root of the tree
    else:
        # Call function on left subtree
        return [Descendant(left(tree), element)]


def Ancestors(tree, element):
    # Check if the tree is empty, return empty list if it is
    if isEmpty(tree): return []

    # Check if the current node is the element we are looking for
    if root(tree) == element:
        # Return the root of the tree
        return [root(tree)]

    else:
        # Check if the left subtree is not empty and right subtree is
        if not isEmpty(left(tree)) and isEmpty(right(tree)):
            # Check if the element is in the left subtree
            if root(left(tree)) == element:
                # Return the root of the current tree and the ancestors in the left subtree
                return [root((tree))] + [Ancestors(left(tree), element)]

        # Check if the right subtree is not empty and left subtree is
        elif isEmpty(left(tree)) and not isEmpty(right(tree)):
            # Check if the element is in the right subtree
            if root(right(tree)) == element:
                # Return the root of the current tree and the ancestors in the right subtree
                return [root(tree)] + [Ancestors(right(tree), element)]

        # Check if both left and right subtrees are not empty
        elif not isEmpty(left(tree)) and not isEmpty(right(tree)):
            # Check the left and right subtrees for ancestors and return the root of the current tree and all ancestors found
            return [root(tree)] + [Ancestors(left(tree), element)] + [Ancestors(right(tree), element)]


# -----------------------------------------------------------------------------

# Question 5
# -----------------------------------------------------------------------------
def insert(element, tree):
    if isEmpty(tree):
        return makeTree(element, emptyTree(), emptyTree())
    if element < root(tree):
        return makeTree(root(tree),
                        insert(element, left(tree)),
                        right(tree))
    else:
        return makeTree(root(tree),
                        left(tree),
                        insert(element, right(tree)))

def isIn(element, tree):
   while ( not isEmpty(tree) and element != root(tree) ):
      if element < root(tree):
         tree = left(tree)
      else:
         tree = right(tree)
   return ( not isEmpty(tree) )

def buildIndex(A):
    tree = emptyTree()
    for i in range(0, len(A)):
        tree = insert(A[i], tree)
    return tree


def Intersect(A, B):
    list1 = []
    tree = buildIndex(B) # makes a BST of B

    for node in A:
        if isIn(node, tree): # if element is in tree of B then append it else leave it
            list1.append(node)
    return list1

def Difference(A,B):
    list1 = []
    tree = buildIndex(B)  # makes a BST of B


    for node in A:
        if not isIn(node, tree):  # if element is not in tree of B then append it else leave it
            list1.append(node)
    return list1

def equalSet(A,B):
    list1 = []
    tree = buildIndex(B) # makes a BST of B

    if len(A) != len(B):
        return False
    for node in A:
        if isIn(node, tree): # if element is in tree of B then append it else leave it
            list1.append(node)
    if len(list1) != len(A):
        return False
    else:
        return True



# -----------------------------------------------------------------------------

# Question 6
# -----------------------------------------------------------------------------

# ranvir singh and saad azeem helped in this class below

class HashTable:

    def __init__(self, p):
        # Initialize the Hash Table with a given size (p)
        self.p = p
        self.table = [[] for _ in range(p)]

    def _hash(self, key):
        # Calculate the hash value of a given key using modulo operator
        return key % self.p

    def isIn(self, key):
        # Check whether the given key is present in the Hash Table or not
        for k, v in self.table[self._hash(key)]:
            if k == key:
                return True
        return False

    def insert(self, key):
        # Insert a new key-value pair into the Hash Table
        hashcode = self._hash(key)
        if self.isIn(key):
            self.getValue(key) + 1
        self.table[hashcode].append((key, 1))

    def delete(self, key):
        # Delete a key-value pair from the Hash Table
        if self.isIn(key):
            hashcode = self._hash(key)
            for i, (k, v) in enumerate(self.table[hashcode]):
                if k == key:
                    self.table[hashcode].pop(i)
            return True
        return False

    def set_item(self, key, val):
        h = self._hash(key)
        found = False
        #set the value of key
        for i, j in enumerate(self.table[h]):
            if len(j) == 2 and j[0] == key:
                self.table[h][i] = (key,val)
                found = True
        if not found:
            self.table[h].append((key,val))

    def insert_list(self, lst):
        # insert a list of elements in the Hash Table
        for i in lst:
            if not self.isIn(i):
                self.set_item(i, 1)
            else:
                self.set_item(i, self.getValue(i) + 1)

    def getValue(self, key: int, default: int = None):
        # get value of a specific key
        if self.isIn(key):
            hashcode = key % self.p
            for (k, v) in self.table[hashcode]:
                if k == key:
                    return v
        if default is None:
            raise KeyError("Key absent from the Hash Table")
        else:
            return default




# -----------------------------------------------------------------------------

# Question 8
# -----------------------------------------------------------------------------

def IntersectHT(A, B):
    t = HashTable(p=4) # Initialize a HashTable with size 4
    res = []
    for i, j in enumerate(A):
        t.set_item(j, i)  # Insert elements of A into the HashTable

    for num in B:
        if t.delete(num):  # If element is present in HashTable, delete it and append to result list
            res.append(num)
    return res

def DifferenceHT(A,B):
    t = HashTable(4) # Initialize a HashTable with size 4
    res = []
    for i, j in enumerate(A):
        t.set_item(j, i)  # Insert elements of A into the HashTable

    for num in B:
        if not t.delete(num):  # If element is not present in HashTable, append it to result list
            res.append(num)

    return res

def equalSetHT(A,B):
    t = HashTable(4) # Initialize a HashTable with size 4
    for i, j in enumerate(A):
        t.set_item(j, i)  # Insert elements of A into the HashTable

    for num in B:
        if not t.delete(num):  # If element is not present in HashTable, return False
            return False

    return True  # If all elements are present in the HashTable, return True


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # A = [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
    # B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][::-1]
    # print(frequencyCount(A))
    # print(B)
    # print(merge_sort(B))
    # tree = makeTree(1, makeTree(2, leaf(4), leaf(5)), makeTree(3, leaf(6), leaf(7)))
    # print(Descendant(tree, 1))
    # print(Ancestors(tree, 1))
    # A = [1, 2, 3]
    # B = [1, 2, 4]
    # print(Intersect(A, B))
    # print(equalSet(A,B))
    # print(Difference(A,B))
    # table = HashTable(p=5)
    # A = [1,2,3,3,3,3]
    # table.insert_list(A)
    # print(table.table)
    # print(table.isIn(4))
    # print(table.delete(2))
    # print(table.set_item(3,6))
    # print(table.table)

    # Question 7
    # -----------------------------------------------------------------------------

    t2 = HashTable(p=7)
    A = [5, 3, 7, 5, 5, 1, 2, 10, 3, 3, 3, 2, 3, 4, 7, 1, 1]
    t2.insert_list(A)
    print(t2.table)

    # -----------------------------------------------------------------------------
    X = [1,2,3]
    Y = [1,2,3]
    print(IntersectHT(X,Y))
    print(DifferenceHT(X, Y))
    print(equalSetHT(X, Y))


