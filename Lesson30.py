# Parent Child
#
# class Parent():
#
#     def work(self):
#         print('earning money')
#
#
# class Child(Parent):
#
#     def play(self):
#         print('playing')
#
#     def work(self):
#         print('earning money 20h per week')
#
#
# child1 = Child()
# child1.play()
# child1.work()


class Age:

    def __init__(self, year):
        self.year = year

    def chinese_year(self):
        return self.year * 3

    def get_age(self):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def get_info(self):
        age = self.get_age()
        print(f' age is {age}, year of birth is {self.year}')


class NewAge(Age):

    def __init__(self, year, height):
        super().__init__(year)
        self.height = height

    def get_height(self, count_year):
        current_year = self.year + count_year
        height_at_twenty_five = self.height + 4.7 * 25
        if count_year >= 25:
            print(f'On {current_year} you have height of {height_at_twenty_five}'
                  f' you have reached your max height')
        else:
            result = self.height + 4.7 * count_year


            print(f'On {current_year} you have height of {result}')

    def new_get_age(self):
        year_1 = super().get_age()
        return year_1 + 1

# ulan = Age(1998)
# ulan.get_info()
kunduz = NewAge(1995, 53)
print(kunduz.get_age())
print(kunduz.new_get_age())
kunduz.get_height(22)
kunduz.get_info()
# nazgul = NewAge()
#
# print(nazgul.get_age(1996))
# print(nazgul.new_get_age(1996))
# print(nazgul.chinese_year(1996))
