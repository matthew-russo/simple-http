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

# OCTET          = <any 8-bit sequence of data>
# CHAR           = <any US-ASCII character (octets 0 - 127)>
# UPALPHA        = <any US-ASCII uppercase letter "A".."Z">
# LOALPHA        = <any US-ASCII lowercase letter "a".."z">
# ALPHA          = UPALPHA | LOALPHA
# DIGIT          = <any US-ASCII digit "0".."9">
# CTL            = <any US-ASCII control character
#                  (octets 0 - 31) and DEL (127)>
# CR             = <US-ASCII CR, carriage return (13)>
# LF             = <US-ASCII LF, linefeed (10)>
# SP             = <US-ASCII SP, space (32)>
# HT             = <US-ASCII HT, horizontal-tab (9)>
# <">            = <US-ASCII double-quote mark (34)>

# CRLF           = CR LF

# LWS            = [CRLF] 1*( SP | HT )

# token          = 1*<any CHAR except CTLs or separators>

# separators     = "(" | ")" | "<" | ">" | "@"
#                | "," | ";" | ":" | "\" | <">
#                | "/" | "[" | "]" | "?" | "="
#                | "{" | "}" | SP | HT

# comment        = "(" *( ctext | quoted-pair | comment ) ")"
# ctext          = <any TEXT excluding "(" and ")">

# quoted-string  = ( <"> *(qdtext | quoted-pair ) <"> )
# qdtext         = <any TEXT except <">>
# quoted-pair    = "\" CHAR

# HTTP-Version   = "HTTP" "/" 1*DIGIT "." 1*DIGIT

# message-header = field-name ":" [ field-value ]
# field-name     = token
# field-value    = *( field-content | LWS )
# field-content  = <the OCTETs making up the field-value
#                  and consisting of either *TEXT or combinations
#                  of token, separators, and quoted-string>

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
        chomp_
        chomp(':')
        panic('unimplemented _headers')

    def _general_header():
#   Cache-Control            ; Section 14.9
# | Connection               ; Section 14.10
# | Date                     ; Section 14.18
# | Pragma                   ; Section 14.32
# | Trailer                  ; Section 14.40
# | Transfer-Encoding        ; Section 14.41
# | Upgrade                  ; Section 14.42
# | Via                      ; Section 14.45
# | Warning                  ; Section 14.46

        panic('unimplemented _general_header')

    def _request_header():
#   Accept                   ; Section 14.1
# | Accept-Charset           ; Section 14.2
# | Accept-Encoding          ; Section 14.3
# | Accept-Language          ; Section 14.4
# | Authorization            ; Section 14.8
# | Expect                   ; Section 14.20
# | From                     ; Section 14.22
# | Host                     ; Section 14.23
# | If-Match                 ; Section 14.24
# | If-Modified-Since        ; Section 14.25
# | If-None-Match            ; Section 14.26
# | If-Range                 ; Section 14.27
# | If-Unmodified-Since      ; Section 14.28
# | Max-Forwards             ; Section 14.31
# | Proxy-Authorization      ; Section 14.34
# | Range                    ; Section 14.35
# | Referer                  ; Section 14.36
# | TE                       ; Section 14.39
# | User-Agent               ; Section 14.43
        panic('unimplemented _request_header')

    def _entity_header():
#   Allow                    ; Section 14.7
# | Content-Encoding         ; Section 14.11
# | Content-Language         ; Section 14.12
# | Content-Length           ; Section 14.13
# | Content-Location         ; Section 14.14
# | Content-MD5              ; Section 14.15
# | Content-Range            ; Section 14.16
# | Content-Type             ; Section 14.17
# | Expires                  ; Section 14.21
# | Last-Modified            ; Section 14.29
# | extension-header
        panic('unimplemented _entity_header')


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


