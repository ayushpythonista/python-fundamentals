"""An OrderedDict is a dictionary subclass that remembers the order in which keys were first inserted. The only difference between dict() and OrderedDict() lies in their handling of key order in Python."""

"""`OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration. In contrast, a standard dictionary does not guarantee any specific order when iterated, providing values in an arbitrary sequence. `OrderedDict` distinguishes itself by retaining the original insertion order of items."""

from collections import OrderedDict


dict_a = {}
dict_a['a'] = 1
dict_a['b'] = 2
dict_a['c'] = 3
dict_a['d'] = 4
print("Standard Dict: ", dict_a)


dict_b = OrderedDict()
dict_b['a'] = 1
dict_b['b'] = 2
dict_b['c'] = 3
dict_b['d'] = 4
print("OrderedDict: ", dict_b)


dict_b['c'] = 17
print("OrderedDict 01: ", dict_b)


"""Equality Comparison in Python Dictionary Order
OrderedDicts in Python can be compared for equality not only based on their content but also considering the order of insertion. This is useful when comparing two OrderedDicts for both key-value pairs and their order.

Example : In this example the code creates two OrderedDicts, `od1` and `od2`, with different orderings of key-value pairs. It then demonstrates that the order of insertion is considered when comparing them for equality using the `==` operator, resulting in `False`."""

# Create two ordered dictionaries with different orderings
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Compare the ordered dictionaries for equality
print(od1 == od2)  


my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
reversed_my_dict = OrderedDict(reversed(list(my_dict.items())))
print(reversed_my_dict)


# OrderedDict Popitem()

last_removed_item = my_dict.popitem(last=True)
print(last_removed_item)
print(my_dict)


# move to end
my_dict['c'] = 117
my_dict['d'] = 23
my_dict['e'] = 56
my_dict.move_to_end('a')
print(my_dict)

my_dict.move_to_end('c', last=False)        # it moves to first
print(my_dict)


# pop to remove specific elements ~ remove specified key and return the corresponding value
rm = my_dict.pop('e')
print(rm)


# update dict
my_dict.update([('f', 73), ('g', 44)]) 
print(my_dict)

