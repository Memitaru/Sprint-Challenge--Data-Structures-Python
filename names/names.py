import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
'''
Initial solution is O(n^2) because of the nested loops. .append() is O(1) and doesn't affect the overall runtime.

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

We can make this faster by putting one list into a binary search tree and then searching for each value in that tree.
'''

#create a BST with the first name and then insert all other names

bst = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    bst.insert(names_1[i])

for i in range(0, len(names_2)):
    if bst.contains(names_2[i]):
        duplicates.append(names_2[i])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
