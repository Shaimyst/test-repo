# this is a document to work on list types and sorting gathered information

# python collection data types:
    # List - a collection which is ordered and changeable. Allows duplicate members.
    # Tuple - a collection which is ordered and unchangeable. Allows duplicate members.
    # Set - a collection which is unordered and unindexed. No duplicate members.
    # Dictionary - a collection which is ordered* and changeable. No duplicate members.

mylist = ["apple", "banana", "cherry"]
# print the class type
print(type(mylist))
# another way to make a list
anotherlist = list(("apple, banana, cherry"))
# count number of characters in list
print(len(anotherlist))
print(type(anotherlist))

mytuple = tuple(("apple", "banana", "cherry"))
# count how many items in a tuple
print(len(mytuple))
# print the class type
print(type(mytuple))
