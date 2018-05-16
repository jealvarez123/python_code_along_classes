# Python Classes

# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@gmail.com'
#         self.initial = first[:1] + last[:1]
#         self.pay = input()
#
#
# emp_1 = Employee('Jaime', 'Alvarez')
# emp_2 = Employee('Buck', 'Merka')
# print('{} {}, Your email is {} {} Desired pay ${} Bonus of ${}'.format(emp_1.first, emp_1.last, emp_1.email, emp_1.initial, emp_1.pay, float(emp_1.pay) * .15))

class Employee:
    def __init__(self,first,last, pay):#self = this
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.initial = first[:1] + last[:1]
        self.pay = float(pay)
        self.bonus = float(pay) * .15

emp_1 = Employee('hide', 'baker', input())
# emp_2 = Employee('sloppy','toppy', input())

print('{} {}, Your email is {}. Your initial is {}. Annual Salary: ${}. Bonus: ${}'.format(emp_1.first, emp_1.last, emp_1.email, emp_1.initial, emp_1.pay, emp_1.bonus))
