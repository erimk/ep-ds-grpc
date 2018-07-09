from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import functions

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    #rpc_paths = ('/RPC2',)
    pass

# Create server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    server.register_function(functions.f1_noop)
    server.register_function(functions.f2_square)
    server.register_function(functions.f3_mean_8)
    server.register_function(functions.f4_str_is_palindrome)
    server.register_function(functions.f5_exp_rep_string)
    server.register_function(functions.f6_create_employee)
    server.register_function(functions.f7_get_employee)
    server.register_function(functions.f8_get_employee_complete)

    # Run the server's main loop
    print('Starting XMLRPC Server...')
    server.serve_forever()
