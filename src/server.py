import SocketServer
class MyTCPSocketHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()	
        if "SECRET" in self.data:
            digits=filter(str.isdigit, self.data)
            count=len(digits)
            result="Digits: " + digits + " Count: " + repr(count)
            print("{} sent: ".format(self.client_address[0]) + self.data)
            filename='result.txt'
            f=open(filename,'wb')
            f.write(self.data)
            # return all the digits in the string and count of digits
            self.request.sendall(result)
        else:
            filename='result.txt'
            f=open(filename,'wb')
            f.write(self.data)
            print("{} sent: ".format(self.client_address[0]) + self.data)
            # return the same data
            self.request.sendall(self.data)		

if __name__ == "__main__":    
    HOST, PORT = "10.10.11.5", 9999
    # instantiate the server and bind to 10.10.11.5 on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPSocketHandler)
    # activate the server and keep running until Ctrl-C
    server.serve_forever()