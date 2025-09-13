# Web Server Lab 

## Overview
This project is part of **Lab 2: Web Server Lab**, which focuses on learning the basics of **socket programming** and **HTTP protocol handling** in Python.  
The goal is to implement a simple web server that:
- Creates and binds a TCP socket to a specific address and port
- Listens for and accepts a client connection
- Receives and parses a basic HTTP request
- Locates the requested file in the server’s local directory
- Returns an appropriate HTTP response to the client
  - **200 OK** with the file content if the file exists
  - **404 Not Found** if the file does not exist

This project provides hands-on experience with **network sockets, HTTP headers, and request/response message formatting**.

---

## Learning Objectives
- Understand how TCP sockets work in Python
- Practice creating, binding, and listening on sockets
- Learn the structure of a basic HTTP request and response
- Implement error handling for missing resources
- Send complete HTTP responses in a single transmission

---

## Features
- Serves static HTML files from the local server directory
- Handles **one HTTP request at a time**
- Provides properly formatted HTTP headers including:
  - `HTTP/1.1` status line (`200 OK` or `404 Not Found`)
  - `Content-Type`
  - `Server` (customizable)
  - `Connection`
- Sends the entire response in **one `send()` call**
- Compatible with browser requests and CLI tools like `curl`

---

## Running the Server
1. Place an HTML file (e.g., `helloworld.html`) in the same directory as `webServer.py`.
