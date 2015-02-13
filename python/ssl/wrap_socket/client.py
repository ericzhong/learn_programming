import socket
import ssl
import os



ca_path = "./ca.pem"

if not os.path.exists(ca_path):
    ca = ssl.get_server_certificate(('127.0.0.1',8888))
    with open(ca_path, 'w') as f:
        f.write(ca)
        f.close()


if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(sock, ca_certs="ca.pem", cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect(('127.0.0.1', 8888))
    
    data = ssl_sock.recv(1024)
    print(data.decode())    # bytes -> string
    
    ssl_sock.close()
