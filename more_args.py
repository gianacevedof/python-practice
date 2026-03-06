# keywords in 'arguments' are simply identifiers for the arguments.
# def phone_number (country, area, first, last):
#     return f"+{country} ({area}) {first}-{last}"
#
# phone_num = phone_number(country=1, area=407, first=112, last=2216)
# print(phone_num)



# *args = this allows you to create a function with arbitrary arguments (a variable amount of arguments)
# def nums(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(nums(1, 2, 3, 4, 5))



# **kwargs = this allows you to create functions with arbitrary keyword arguments
# (a variable amount of arguments with keywords)
# def address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print(address(
#     Address = "123 Fake St.",
#     City = "Orlando",
#     State = "FL",
#     Zip = 12345
# ))