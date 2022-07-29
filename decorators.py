#
# def uppercase(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
#
#
# def shout(func):
#     def wrapper():
# #         return func() + '!!!'
# #     return wrapper
# #
# # @shout
# # @uppercase
# # def greet():
# #     return 'hello'
#
#
# def strong(func):
#     def wrapper(*args, **kwargs):
#         return f'<strong> {func(*args, **kwargs)} </strong>'
#     return wrapper
#
#
# def emphasis(func):
#     def wrapper(*args, **kwargs):
#         return f'<em> {func(*args, **kwargs)} </em>'
#     return wrapper
#
#
# # def uppercasse(func):
# #     def wrapper(*args, **kwargs):
# #         return func(*args, **kwargs).upper()
# #     return wrapper
#
# @strong
# @emphasis
# def greet_with_name(name: str):
#     return f'hello {name}'
#
#
# print(greet_with_name('Miles'))

import functools


def usd(func):
    @functools .wraps(func)
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}$'
    return wrapper


@usd
def kgs_to_usd(som: float):
    '''Converts KGS to USD'''
    return som / 84


print(kgs_to_usd(8400))
print('name', kgs_to_usd.__name__)
print('name', kgs_to_usd.__doc__)