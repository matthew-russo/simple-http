from enum import Enum
import socket                

class HttpServer:
    @staticmethod
    def on_port(port: int) -> Self:
        new_server = HttpServer()
        new_server.socket = socket.socket()          
        new_server.socket.bind(('', port))         
        # put the socket into listening mode with a backlog of 5 connections
        new_server.socket.listen(5)

    def serve():
        while True: 
            conn, addr = s.accept()
            http_request = self.parse_request(conn)
            handle(http_request)
            conn.close()

    def parse_request(conn: Connection) -> HttpRequest:
        data = receive_all(conn)
        http_request = HttpRequest.parse(data)

