import socket
import ssl
import time


if __name__ == "__main__":

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    ctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8888))
    sock.listen(8)

    while True:
        try:
            new_sock,fromaddr = sock.accept()
            print("Connected by:", fromaddr)
            ssl_sock = ctx.wrap_socket(new_sock, server_side=True)
        except Exception:
            pass
        else:
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            ssl_sock.send(now.encode())   # string -> bytes
            ssl_sock.shutdown(socket.SHUT_RDWR)
            ssl_sock.close()
