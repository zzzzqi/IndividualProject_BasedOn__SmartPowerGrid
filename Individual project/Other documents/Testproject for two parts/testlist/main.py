import copy

sublist = []
mainlist = []
sublist.append(1)
sublist.append(2)
mainlist.append(copy.copy(sublist))
print(mainlist)
sublist.append(3)
mainlist.append(copy.copy(sublist))
print("//////////")
print(mainlist)
test_Str = "test"
mainlist.append(test_Str)
print(mainlist)
test_int = 1111
mainlist.append(test_int)
print(mainlist)