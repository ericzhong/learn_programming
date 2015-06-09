import socket
import ssl
import time
import os
import threading
import pprint

#just send user name
def user_login(socketfd):
	name = socketfd.recv(1024)
	ca = socketfd.recv(1024)

	print(name,ca)
	return name,ca

#generate ca
def genca(name):
	cmd = "sh make_pem.sh " + name
	os.system(cmd);

#send ca and key to client
def sendca(name):
	cmd = "cp ./ClientCA/" + name + "* ../Client/Cert/"
	os.system(cmd)
	cmdrm = "cp ./ClientCA/" + name + "_key.pem"

#client pthead
class client(threading.Thread):
	def __init__(self, socketfd):
		threading.Thread.__init__(self)
		self.socketfd = socketfd    
		self.thread_stop = False

	def run(self):
		username,ca = user_login(self.socketfd)
		if ca == '0':
			genca(username)
			sendca(username)
			time.sleep(2)

		ca_name = "./ClientCA/" + username + "_cert.pem"
	   	
	   	#Certificate authentication
		ssl_sock = ssl.wrap_socket(self.socketfd,ca_certs=ca_name,cert_reqs=ssl.CERT_REQUIRED)
		
		#Get ca info
		ca_dist = ssl_sock.getpeercert()
		print("Get User Certificate:")
		pprint.pprint(ca_dist)
		
		while True:
			recv_time = ssl_sock.recv(1024)
			if recv_time:
				print "%s:"%username,
				print(bytes.decode(recv_time))	
			else:
				print("user %s logout!" % username)
				ssl_sock.close()
				break

	def stop():
		self.thread_stop = True


def main():
	bindsocket=socket.socket()
	bindsocket.bind(('127.0.0.1',8888))
	bindsocket.listen(8)

	while True:
		newsocket,fromaddr=bindsocket.accept()
		print("get connect from:",fromaddr)

		newclient = client(newsocket)
		newclient.start()

if __name__ == '__main__':
	main()
