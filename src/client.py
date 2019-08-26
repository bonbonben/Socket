import socket, sys, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create a TCP socket
s.connect(("10.10.11.5", 9999))	# connect to server
mode = " ".join(sys.argv[1:2])
data = " ".join(sys.argv[2:])
fileFound = 0

if mode == 'echo':
    print 'Mode: %s' %mode
    print 'Data: %s' %data
	
    try:
        s.sendall(bytes(data + "\n"))	# send data to the server
        received = str(s.recv(1024))	# receive data from the server
    finally:
        s.close()

    print("Sent: {}".format(data))
    print("Received: {}".format(received))
elif mode == 'file':
    print 'Mode: %s' %mode
    print 'Data: %s' %data
	
    try:
        for file in os.listdir("/home/student/Desktop/"):
            if file == data:
                fileFound = 1
                break
        if fileFound == 0:
            print data+" not found"
        else:
            print data+" found"
            sendFile = open("/home/student/Desktop/"+data,"rb")
            sRead = sendFile.read(1024)
            while sRead:
                s.send(sRead)
                sRead = sendFile.read(1024)
            print "Send file successfully"
    finally:
        s.close()
else:
    print 'Please choose Echo mode or File mode'
    s.close()