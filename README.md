# Web-Server

SUSTech CS305 Computer Networking Lab 5 Socket programming.

A simple Web server in Python that is capable of processing only one request. Specifically, Web server will

1. create a connection socket when contacted by a client (browser);

2. receive the HTTP request from this connection;

3. parse the request to determine the specific file being requested;

4. get the requested file from the server’s file system;

5. create an HTTP response message consisting of the requested file preceded by header lines; and

6. send the response over the TCP connection to the requesting browser.

If a browser requests a file that is not present in the server, the server should return a “404 Not Found” error message. In the companion Web site, we provide the skeleton code for the server. Your job is to complete the code, run the server, and then test the server by sending requests from browsers running on different hosts. If you run the server on a host that already has a Web server running on it, then you should use a different port than port 80 for your Web server.

Also capable for mp3, mp4, jpg loading.
