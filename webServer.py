# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1) #listen to 1 connection
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024) #Fill in start -a client is sending you a message   #Fill in end 
      print('Message', message)
      filename = message.split()[1]
      print('File name  ', filename)
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:]) #fill in start #fill in end)
      outputdata = f.read()
      
      #fill in end
      
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
      #Fill in end
               
      for i in f: #for line in file
      #Fill in start - append your html file contents #Fill in end 
        connectionSocket.send(outputdata[i])
		    connectionSocket.send("\r\n")
      #Send the content of the requested file to the client (don't forget the headers you created)!
      # Fill in start


      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      connectionSocket.send('404 Not Found')
      # Remember the format you used in the try: block!
      #Fill in start
      connectionSocket.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n")
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
