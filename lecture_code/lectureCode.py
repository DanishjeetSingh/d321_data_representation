# Lists
def isEmpty(list):
    return list == []

def emptyList():
    return []

def makeList(element,list):
    return [element] + list


def first(list):
    return list[0]

def rest(list):
    return list[1:]

def length(list):
    return len(list)

# append(A,B) = AB
def append(A,B):
    if isEmpty(A): return B
    else: return makeList(first(A),append(rest(A),B))

# merge to sorted lists A and B
    
def Merge(A,B):
    if isEmpty(A): return B
    if isEmpty(B): return A
    if first(A) <= first(B):
        return makeList(first(A), Merge(rest(A), B))
    return makeList(first(B), Merge(A, rest(B)))

# merge Sort helf functions
# find left and right halves in a list A
def leftHalf(A):
   return A[:len(A)//2]

def rightHalf(A):
   return A[len(A)//2:]                                        

# sort the elements in the list A             

def mergeSort(A):
    if length(A) <= 1: return(A)
    return Merge(mergeSort(leftHalf(A)), mergeSort(rightHalf(A)))    

# remove the duplicates in the sorted list A
# Naive algorithm O(|A|^2)

def Distinct(A):
   distinct = []
   for i in range(0,length(A)):
     found = False
     for j in range(i+1,length(A)):
        if A[i] == A[j]: found = True
     if not found: distinct = distinct + [A[i]]
   return distinct 


# Remove the distinct elements from a sorted list A
    
def Distinct(A):
   if length(A) <= 1: return A
   if first(A) == first(rest(A)): return Distinct(A[1:])
   else: return makeList(first(A), Distinct(rest(A)))

# Compute the union of two sorted lists A and B

def sortUnion(A,B):
    return sortDistinct(mergeSort(A + B))

# Compute the intersection of two sorted lists A and B

def sortIntersect(A,B):
    if isEmpty(A) or isEmpty(B): return emptyList()
    if first(A) == first(B):
       return makeList(first(A), sortIntersect(rest(A),rest(B)))
    if first(A) < first(B): return sortIntersect(rest(A), B)
    else: return sortIntersect(A,rest(B))

# Compute the intersection of two lists
def Intersect(A,B):
    return sortIntersect(Distinct(mergeSort(A)),Distinct(mergeSort(B)))

# Compute the difference of two sorted lists
    
def sortDifference(A,B):
    if isEmpty(A): return emptyList()
    if isEmpty(B): return A
    if first(A) == first(B): return sortDifference(rest(A), rest(B))
    if first(A) < first(B):  return makeList(first(A), sortDifference(rest(A),B))
    else: return sortDifference(A,rest(B))

# Compute the difference of two lists
def Difference(A,B):
    return sortDifference(Distinct(mergeSort(A)),Distinct(mergeSort(B)))

# Determine of the lists A and B have elements in common
def Overlap(A,B):
    return not isEmpty(Intersect(A,B))

# Determine if all the elements in A occur in B (A is a subset of B)
def Subset(A,B):
    return isEmpty(Difference(A,B))


# Binary trees data structure
# We use Python dictionaries to represent a tree
# {root: value, left: a tree, right: a tree}



def makeTree(value,left,right):
    return {'value':value, 'left': left, 'right': right}


def leaf(value):
    return makeTree(value,emptyTree(),emptyTree())


def root(tree):
    return tree['value']


def left(tree):
    return tree['left']


def right(tree):
    return tree['right']

def isEmpty(tree):
    if tree == {}: return True
    else: return False

    

# Example of a binary tree

T = makeTree(5,makeTree(10,makeTree(11,leaf(20),emptyTree()),leaf(8)),makeTree(7,emptyTree(),leaf(3)))


# compute the height of a binary tree
def height(tree):
    if isEmpty(tree): return 0
    else: return 1 + max(height(left(tree)),height(right(tree)))

# compute the size (number of nodes) in a binary tree

def size(tree):
    if isEmpty(tree): return 0
    else: return 1 + size(left(tree)) + size(right(tree))


# determine if an element is in a binary tree    
def isIn(element,tree):
    if isEmpty(tree): return False
    if element == root(tree): return True
    else: return isIn(element,left(tree)) or isIn(element,right(tree))



# Example of a Binary Search Tree    

B= makeTree(10,makeTree(7,makeTree(5,leaf(3),emptyTree()),leaf(8)),makeTree(15,leaf(12),makeTree(18,leaf(17),emptyTree())))

# Determine if a element is in a Binary Search Tree
# Recursive version

def isIn(element, tree):
   if isEmpty(tree):  return False
   if element == root(tree): return True
   if element < root(tree):  return isIn(element,left(tree))
   else: return isIn(element,right(tree))

         
# Determine if a element is in a Binary Search Tree
# Iterative, non-recursive version, of membership

def isIn(element, tree):
   while ( not isEmpty(tree) and element != root(tree) ):
      if element < root(tree):
         tree = left(tree)
      else:
         tree = right(tree)
   return ( not isEmpty(tree) )


# Insert an element into a Binary Search tree
# It is assumed that the element is not already in the tree

def insert(element,tree):
  if isEmpty(tree):
     return makeTree(element, emptyTree(), emptyTree())
  if element < root(tree):
     return makeTree(root(tree), 
                     insert(element,left(tree)), 
                     right(tree))
  else: return makeTree(root(tree), 
                        left(tree), 
                        insert(element,right(tree)))

# This is a convenient function to create a BST starting
# from an array
  
def buildIndex(A):
    index = emptyTree()
    for i in range(0,length(A)):
        tree = insert(A[i],index)
    return index

# In order listing the elements of BST tree gives and order
# of the elements in the BST

def inOrderTravesal(tree):
    if ( not isEmpty(tree) ):
        innOrderTraversal(left(tree))
        print(root(tree))
        inOrderTraversal(right(tree))

# Index sort
def treeSort(A):
   index = buildIndex(A)
   inOrderTravesal(index)

# Delete an element from a binary search tree

def smallestNode(tree):
   if isEmpty(left(tree)): return root(tree)
   else: return smallestNode(left(tree))

def removeSmallestNode(tree):
  if isEmpty(left(tree)): return right(tree)
  else: return makeTree(root(tree), re
                        moveSmallestNode(left(tree)), right(tree))
                        

def delete(element, tree):
    if element < root(tree): return makeTree(root(tree), delete(element,left(tree)), right(tree))
    if element > root(tree): return makeTree(root(tree), left(tree), delete(element, right(tree)))
    if element == root(tree) and isEmpty(left(tree)): return right(tree)
    if element == root(tree) and isEmpty(right(tree)): return left(tree)
    else: return makeTree(smallestNode(right(tree)), left(tree), removeSmallestNode(right(tree)))


    


    




