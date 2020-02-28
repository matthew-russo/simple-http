import sys

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
    def parse(input_: str) -> HttpRequest:
        self.input = input_
        self.current = 0
        request_line = _request_line()
        headers = _headers()
        body = _body()

    def _request_line(self) -> RequestLine:
        method = self._method()
        request_uri = self.chomp_word()
        http_version = self._http_version()

    def _method(self):
        word = self.chomp_word()

        try:
            method = HttpMethod[word]
        except KeyError:
            raise InvalidHttpMethod(word)

    def _http_version():
        # TODO -> this should be an enum
        return self.chomp_word()

    def _headers():
        panic('unimplemented _headers')

    def _general_header():
        panic('unimplemented _general_header')

    def _request_header():
        panic('unimplemented _request_header')

    def _entity_header():
        panic('unimplemented _entity_header')


    # message-header = field-name ":" [ field-value ]
    # field-name     = token
    # field-value    = *( field-content | LWS )
    # field-content  = <the OCTETs making up the field-value
    #                  and consisting of either *TEXT or combinations
    #                  of token, separators, and quoted-string>
    def _message_header():
        let word = self.chomp_until(':')
        panic('unimplemented _message_header')

    def _body():
        panic('unimplemented _body')

    def chomp_until(self, delim: str) -> str:
        word = ''
        while self.current < len(self.input) and self.input[self.current].isspace() != delim:
            word += self.input[self.current]
            self.current += 1

        return word


    def chomp_word(self) -> str:
        word = ''
        while self.current < len(self.input) and not self.input[self.current].isspace():
            word += self.input[self.current]
            self.current += 1

        return word

    def chomp_rest(self) -> str:
        word = self.input[self.current:]
        self.current = len(self.input)
        return word



def panic(msg: str):
    print(msg)
    sys.exit(1)

def sample_get_request():
    return """GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive"""

def sample_post_request():
    return """POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: application/x-www-form-urlencoded
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

licenseID=string&content=string&/paramsXML=string"""

def sample_xml_post_request():
    return """POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

<?xml version="1.0" encoding="utf-8"?>
<string xmlns="http://clearforest.com/">string</string>"""


