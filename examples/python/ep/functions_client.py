# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import functions_pb2
import functions_pb2_grpc

##
import time
#import json
import functions
#from functions import Employee
##

def run():
    #with xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True) as proxy:
    channel = grpc.insecure_channel('localhost:50051')
    stub = functions_pb2_grpc.EpFunctionsStub(channel)
    from datetime import datetime
    print (str(datetime.now())) 


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

emp = functions.Employee()

tests = [
    ('f1_noop', lambda p: p.f1_noop(functions_pb2.Empty())),
    ('f2_square(0)', lambda p: p.f2_square(functions_pb2.NumberRequest(num=0))),
    ('f2_square(2)', lambda p: p.f2_square(functions_pb2.NumberRequest(num=2))),
    ('f2_square(1000)', lambda p: p.f2_square(functions_pb2.NumberRequest(num=1000))),
    ('f3_mean_8(1..1)', lambda p: p.f3_mean_8(functions_pb2.MeanRequest(n1=1,n2=1,n3=1,n4=1,n5=1,n6=1,n7=1,n8=1))),
    ('f3_mean_8(1..8)', lambda p: p.f3_mean_8(functions_pb2.MeanRequest(n1=1,n2=2,n3=3,n4=4,n5=5,n6=6,n7=7,n8=8))),
    ('f3_mean_8(10000..80000)', lambda p: p.f3_mean_8(functions_pb2.MeanRequest(n1=10000,n2=10002,n3=10003,n4=10004,n5=10005,n6=10006,n7=10007,n8=10008))),
    ('f4_str_is_palindrome(a)', lambda p: p.f4_str_is_palindrome(functions_pb2.PalindromeRequest(palindrome='a'))),
    ('f4_str_is_palindrome(arara)', lambda p: p.f4_str_is_palindrome(functions_pb2.PalindromeRequest(palindrome='arara'))),
    ('f4_str_is_palindrome(pneumoultramicroscopicossilicovulcanoconiotico)', lambda p: p.f4_str_is_palindrome(functions_pb2.PalindromeRequest(palindrome='pneumoultramicroscopicossilicovulcanoconiotico'))),
    ('f5_exp_rep_string(a)', lambda p: p.f5_exp_rep_string(functions_pb2.LongRequest(num='a'))),
    ('f5_exp_rep_string(arara)', lambda p: p.f5_exp_rep_string(functions_pb2.LongRequest(num='arara'))),
    ('f5_exp_rep_string(pneumoultramicroscopicossilicovulcanoconiotico)', lambda p: p.f5_exp_rep_string(functions_pb2.LongRequest(num='pneumoultramicroscopicossilicovulcanoconiotico'))),
    ('f6_create_employee(None)', lambda p: p.f6_create_employee(functions_pb2.Employee(id=None,name=None,age=None,manager=None))),
    ('f6_create_employee(employee)', lambda p: p.f6_create_employee(functions_pb2.Employee(id=emp.id,name=emp.name,age=emp.age,manager=emp.manager))),
    ('f7_get_employee', lambda p: p.f7_get_employee(functions_pb2.EmployeeId(id=1))),
    ('f8_get_employee_complete', lambda p: p.f8_get_employee_complete(functions_pb2.EmployeeId(id=1)))
]

def run_benchmark():
    channel = grpc.insecure_channel('localhost:50051')
    stub = functions_pb2_grpc.EpFunctionsStub(channel)
    print('test_name', 'duration')
    for test_name, test in tests:
        start = time.time()
        res = test(stub)
        end = time.time()
        print(test_name, end - start)


if __name__ == '__main__':
    run()
    run_benchmark()
  
