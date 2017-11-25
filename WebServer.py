# Import socket module
from socket import *
import io

host = '127.0.0.1'
# Assign a port number
port = 8898
# Create a TCP server socket # (AF_INET is used for IPv4 protocols) # (SOCK_STREAM) is used for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# Bind the socket to server address and server port
address = (host, port)
serverSocket.bind(address)
# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while 1:
    print('ready to serve...')
    # Set up a new connection from the client
    connectionSocket, clientAddr = serverSocket.accept()
    # Receives the request message from the client
    message = connectionSocket.recv(1024)
    print(message.decode('utf-8'), '::', message.split()[0].decode('utf-8'), ':', message.split()[1].decode('utf-8'))
    # Parse the request to determine the specific file being requested
    filename = message.split()[1]
    print(filename.decode('utf-8'), '||', filename[1:].decode('utf-8'))

    try:
        returnType = filename.decode('utf-8')[1:].split('.')[1]
        # Get the requested file from the server’s file system
        if returnType == 'txt':
            f = io.open(filename[1:], "r", encoding="utf-8")
            data = f.read()
            # Create an HTTP response message consisting of the requested file preceded by header lines
            connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
            # Set content type!!! which can display Chinese characters
            connectionSocket.send('Content-Type: text/html; charset=utf-8\n\n'.encode('utf-8'))
            # Send the response over the TCP connection to the requesting browser
            connectionSocket.send(data.encode('utf-8'))
            connectionSocket.close()

        # Get the requested file from the server’s file system
        elif returnType == 'jpg':
            f = io.open(filename[1:], "rb")
            data = f.read()
            # Create an HTTP response message consisting of the requested file preceded by header lines
            connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
            # Set content type!!! which can display images.
            connectionSocket.send('Content-Type: image/jpg\n\n'.encode('utf-8'))
            # Send the response over the TCP connection to the requesting browser
            connectionSocket.send(data)
            connectionSocket.close()

        # Get the requested file from the server’s file system
        elif returnType == 'mp3':
            f = io.open(filename[1:], "rb")
            data = f.read()
            # Create an HTTP response message consisting of the requested file preceded by header lines
            connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
            # Set content type!!! which can display audios.
            connectionSocket.send('Content-Type: audio/mp3\n\n'.encode('utf-8'))
            # Send the response over the TCP connection to the requesting browser
            connectionSocket.send(data)
            connectionSocket.close()

        # Get the requested file from the server’s file system
        elif returnType == 'mp4':
            f = io.open(filename[1:], "rb")
            data = f.read()
            # Create an HTTP response message consisting of the requested file preceded by header lines
            connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
            # Set content type!!! which can display videos.
            connectionSocket.send('Content-Type: video/mp4\n\n'.encode('utf-8'))
            # Send the response over the TCP connection to the requesting browser
            connectionSocket.send(data)
            connectionSocket.close()

        else:
            raise IndexError()

    except (IOError, IndexError):
        # If a browser requests a file that is not present in your server
        # Server return a “404 Not Found” error message
        f = io.open('404.html', "r", encoding="utf-8")
        data = f.read()
        connectionSocket.send('\HTTP/1.1 404 not found\n\n'.encode('utf-8'))
        connectionSocket.send(data.encode('utf-8'))
        # Close the client connection socket
        connectionSocket.close()
serverSocket.close()
