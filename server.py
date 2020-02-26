from enum import Enum
import socket                
  
s = socket.socket()          
print('Socket successfully created')
  
port = 12345                
  
s.bind(('', port))         
print('socket binded to {}'.format(port))
  
# put the socket into listening mode with a backlog of 5 connections
s.listen(5)
print('socket is listening')
  
while True: 
    conn, addr = s.accept()      
    data = receiveAll(conn)
    http_request = HttpRequest.parse(data)
    handle(http_request)
    conn.close()

# https://tools.ietf.org/html/rfc2616#section-5
# Request       = Request-Line              ; Section 5.1
#                 *(( general-header        ; Section 4.5
#                  | request-header         ; Section 5.3
#                  | entity-header ) CRLF)  ; Section 7.1
#                 CRLF
#                 [ message-body ]          ; Section 4.3
class HttpRequest:

    

# 5.1 Request-Line
# 
#    The Request-Line begins with a method token, followed by the
#    Request-URI and the protocol version, and ending with CRLF. The
#    elements are separated by SP characters. No CR or LF is allowed
#    except in the final CRLF sequence.
# 
#         Request-Line   = Method SP Request-URI SP HTTP-Version CRLF
class HttpRequestLine:
    

# Sections 9.2 - 9.9
class HttpMethod(Enum):
    OPTIONS = auto()
    GET     = auto()
    HEAD    = auto()
    POST    = auto()
    PUT     = auto()
    DELETE  = auto()
    TRACE   = auto()
    CONNECT = auto()

class HttpRequestParser:

    def parse():
        print('unimplemented parse')

    def _request_line():
        print('unimplemented _request_line')

    def _method():
        print('unimplemented _method')

    def _request_uri():
        print('unimplemented _request_uri')

    def _http_version():
        print('unimplemented _http_version')

    def _headers():
        print('unimplemented _headers')

    def _general_header():
        print('unimplemented _general_header')

    def _request_header():
        print('unimplemented _request_header')

    def _entity_header():
        print('unimplemented _entity_header')

    def _body():
        print('unimplemented _body')
