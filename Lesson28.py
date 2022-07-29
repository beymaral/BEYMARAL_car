# Incapsula

# protected, private, public
#
# class Bank:
#
#     def __init__(self, account, name, age):
#         self.name = name
#         self._age = age
#         self.__account = account
#
# nazgul = Bank('9301293', age=26, name='Nazgul')
# nazgul._Bank__account = '10000000'
# print(nazgul._Bank__account)
# # print(dir(nazgul))

# class Bank:
#
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self.__account = 0
#
#     @property
#     def get_account(self):
#         return self.__account
#
#     @get_account.setter
#     def get_account(self, money):
#         if money >= 100000:
#             raise Exception('Over Limit')
#         self.__account += money
#         return self.__account
#
#
# nazgul = Bank(age=26, name='Nazgul')
# nazgul.get_account()
# nazgul.add_money(10000000)
# nazgul.get_account()
#
# print(nazgul.get_account)
# nazgul.get_account = 21231231
# print(nazgul.get_account)

# class Example:
#     per_var1 = 100
#     per_var2 = 300
#
#     def __init__(self, d_var4):
# #
# #        return (self.d_var4)
# #
# #
# # print
#
# # Calculator
#
# class Calculator:
#     def __init__(self, dyn1, dyn2):
#         self.dyn1 = dyn1
#         self.dyn2 = dyn2
#
#     def summ1(self):
#         summ = self.dyn1 + self.dyn2
#         print(f'Sum = {summ}.')
#         return summ
#
#     def mult1(self):
#         mult = self.dyn1 * self.dyn2
#         print(f'Multiplied = {mult}.')
#         return mult
#
#     def division(self):
#         div = self.dyn1 / self.dyn2
#         print(f'Division = {div}')
#         return div
#
#
# a = int(input())
# b = int(input())
# obj1 = Calculator(a, b)
# obj1.summ1()
# obj1.mult1()
# obj1.division()

# Error - double printing:
# print(obj1.summ1())
# print(obj1.mult1())
# print(obj1.division())


#EVAL
# numbers = '21+32*3-7/2'
# result = eval(numbers)
#
# class Calculator:
#     def __init__(self) -> None:
#         self.operation = None
#
#     def calculate(self, operation):
#         self.operation = eval(operation)
#         return self.operation
#
#
# a = str(input())
# c = Calculator()
# print(c.calculate(a))


class Calculator:
    def __init__(self) -> None:
        self.operation = eval(input('Enter operation: '))

    def calculate(self, operation):
        self.operation = eval(operation)
        return self.operation

    def get_result(self):
        return self.operation


c = Calculator()
print(c.get_result())
