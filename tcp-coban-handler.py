#!/usr/bin/python3


from time import sleep
import socket
import threading


def logging_process(text: str, type: str) -> str:
    return f"[*] Done {text}" if type == "OK" else "[x] Error in the connection os something like that"


class CobanHandler:
    def __init__(self, imei: str) -> None:
        self.imei = imei

    @staticmethod
    def connection() -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 5001))
        sock.listen(3)
        return sock

    def encoding_message(self) -> hex:
        command: hex = self.imei.encode().hex()
        return command


def client_handler(sock: socket.socket) -> None:
    request = sock.recv(2048)
    print(logging_process(f"Received {request.decode('utf-8')}", type="OK"))


def main():
    try:
        coban_connection = CobanHandler(imei="868166051864296")
        coban_sock = coban_connection.connection()
        client, address = coban_sock.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        while True:
            # receiving data stream
            request = client.recv(2048)
            if not request:
                break
            print(f"Received {request.decode('utf-8')} from {address[0]}:{address[1]}")
            # print(f"sending commands to {address[0]}:{address[1]}")
            command_to_send = input("send something># ")
            client.send(command_to_send.encode())
            print(f"commands sent")
            #thread_client = threading.Thread(target=client_handler, args=(client, ))
            # thread_client.start()
    except Exception as e:
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        print("exiting...")
        exit(0)


if __name__ == "__main__":
    main()