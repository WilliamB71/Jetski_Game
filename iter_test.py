import itertools

test_list = [1, 2, 3]
repeating_list = itertools.cycle(test_list)
iter_list = iter(test_list)

# def repeating_function(repeating_list):
#     for i in repeating_list:
#         yield i

# print(repeating_function(repeating_list))


# class Iterate_images:
#     def __init__(self, iterating_list) -> None:
#         self.ilist = iterating_list

#         def __iter

print(next(repeating_list))
print(next(repeating_list))