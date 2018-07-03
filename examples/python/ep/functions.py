import random

class Employee():
    def __init__(self):
        self.id = 1
        self.name = ''
        self.age = 0
        self.manager = None

def f1_noop():
    pass

def f2_square(num):
    return num ** 2

def f3_mean_8(n1, n2, n3, n4, n5, n6, n7, n8):
    return (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8) / 8

def f4_str_is_palindrome(value):
    return value == value[::-1]

def f5_exp_rep_string(value):
    return value * len(value)

def f6_create_employee(employee):
    pass

def f7_get_employee(e_id):
    e = Employee()
    e.id = e_id
    e.name = random.choice(["Lukashenko", 'Petrovich', 'Schrodivich'])
    e.age = 30
    return e

def f8_get_employee_complete(e_id):
    e = f7_get_employee(e_id)
    e.manager = f7_get_employee(e_id + 1)
    return e
