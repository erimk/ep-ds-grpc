import xmlrpc.client
import time
import json
from functions import Employee


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer

employee = Employee()

tests = [
    ('f1_noop', lambda p: p.f1_noop()),
    ('f2_square(0)', lambda p: p.f2_square(0)),
    ('f2_square(2)', lambda p: p.f2_square(2)),
    ('f2_square(1000)', lambda p: p.f2_square(1000)),
    ('f3_mean_8(1..1)', lambda p: p.f3_mean_8(1, 1, 1, 1, 1, 1, 1, 1)),
    ('f3_mean_8(1..8)', lambda p: p.f3_mean_8(1, 2, 3, 4, 5, 6, 7, 8)),
    ('f3_mean_8(10000..80000)', lambda p: p.f3_mean_8(10000, 10002, 10003, 10004, 10005, 10006, 10007, 10008)),
    ('f4_str_is_palindrome(a)', lambda p: p.f4_str_is_palindrome('a')),
    ('f4_str_is_palindrome(arara)', lambda p: p.f4_str_is_palindrome('arara')),
    ('f4_str_is_palindrome(pneumoultramicroscopicossilicovulcanoconiótico)', lambda p: p.f4_str_is_palindrome('pneumoultramicroscopicossilicovulcanoconiótico')),
    #('f5_exp_rep_string(a)', lambda p: p.f5_exp_rep_string('a')),
    #('f5_exp_rep_string(arara)', lambda p: p.f5_exp_rep_string('arara')),
    #('f5_exp_rep_string(pneumoultramicroscopicossilicovulcanoconiótico)', lambda p: p.f5_exp_rep_string('pneumoultramicroscopicossilicovulcanoconiótico')),
    ('f6_create_employee(None)', lambda p: p.f6_create_employee(None)),
    ('f6_create_employee(employee)', lambda p: p.f6_create_employee(employee)),
    ('f7_get_employee', lambda p: p.f7_get_employee(1)),
    ('f8_get_employee_complete', lambda p: p.f8_get_employee_complete(1))
]

def run_benchmark():
    with xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True) as proxy:
        print('test_name', 'duration')
        for test_name, test in tests:
            start = time.time()
            res = test(proxy)
            end = time.time()
            print(test_name, end - start)


if __name__ == '__main__':
    run_benchmark()
