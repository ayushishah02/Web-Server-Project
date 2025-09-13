# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            
            # Open the client requested file
            f = open(filename[1:], "rb")
            outputdata = f.read()
            f.close()

            # Send HTTP header line for a valid request
            header = "HTTP/1.1 200 OK\r\n"
            header += "Content-Type: text/html; charset=UTF-8\r\n"
            header += "Content-Length: " + str(len(outputdata)) + "\r\n"
            header += "\r\n"

            # Send the header and the content of the requested file to the client
            connectionSocket.send(header.encode())
            connectionSocket.send(outputdata)

            connectionSocket.close()

        except IOError:
            # Send response message for invalid request (404 Not Found)
            header = "HTTP/1.1 404 Not Found\r\n\r\n"
            response = "<html><head></head><body><h1>404 Not Found</h1></body></html>"

            connectionSocket.send(header.encode())
            connectionSocket.send(response.encode())
            connectionSocket.close()

    serverSocket.close()
    sys.exit()

if __name__ == "__main__":
    webServer(13331)