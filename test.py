import random

assess = [1,2,3,4,5,6,7,8,9,10,11,12]
weights_ = [1,2,3,4,5,10,10,20,20,15,5,5]

for i in range(30):
    print(*random.choices(assess, weights_))


# args = [
#     ("Віра Жук", 7.161904761904762),
#     ("Альбіна Данькевич", 7.1313131313131315),
#     ("Алевтин Наливайко", 6.836956521739131),
#     ("Клавдія Демиденко", 6.77),
#     ("Ярина Швачка", 6.758241758241758),
# ]

# def formatted_grades(args):
#     return_args = []
#     iter = 1
#     for i in args:
#         return_args.append(("  {:<20}|" * len(i)).format(*i))
#         iter += 1
#     return return_args


# for print_args in formatted_grades(args):
#     print(print_args)


# a = None

# result = lambda a: "HEHEHE" if a != None else "HOHOHO"

# print(("  {:<5}|").format(result(a)))
# # print(result(a))


# # result = lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd"

# # # print for numbers
# # print(result(12))
# # print(result(11))


# my_list = [3, None]

# new_list = list(filter(lambda x: (x != None), my_list))

# print(new_list)


# my_list = [3, None]

# new_list = list(map(lambda x: "None" if x == None else x, my_list))

# print(new_list)
