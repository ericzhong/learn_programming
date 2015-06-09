import socket
import ssl
import time

def main():
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 8888))
	s.send(str.encode("test"))
	s.send(str.encode("0"))
	time.sleep(1)
	context=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	context.load_cert_chain(certfile="./Cert/test_cert.pem",keyfile="./Cert/test_key.pem")

	connstream=context.wrap_socket(s,server_side=True)
	while True:
		now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		connstream.send(str.encode(now_time))
		time.sleep(1)

if __name__ == '__main__':
	main()