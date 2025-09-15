# Web Server Lab

## 📌 Overview
This project implements a lightweight HTTP web server in **Python**, designed to provide a foundational understanding of **socket programming** and the **HTTP protocol**.  

The server demonstrates how modern web infrastructure works at a low level by:  
- Creating and binding a **TCP socket** to a network interface and port  
- Accepting client connections (e.g., browsers or CLI tools like `curl`)  
- Parsing **raw HTTP requests**  
- Locating and serving requested resources from the server’s local directory  
- Returning fully formatted HTTP responses, including appropriate status codes (`200 OK`, `404 Not Found`)  

By building the server from scratch, the project offers hands-on experience in **network programming, protocol parsing, and error handling**, mirroring the behavior of production-grade web servers in a simplified environment.  

---

## ⚙️ Tools, Languages & Technologies
- **Programming Language**: Python (socket programming, file handling, string parsing)  
- **Libraries**: Python standard library (`socket`, `os`) — no external dependencies  
- **Protocols**: TCP/IP and HTTP/1.1  
- **Testing Tools**:  
  - Web browsers (Chrome, Firefox)  
  - CLI utilities (`curl`, `telnet`) for raw HTTP requests  

---

## ✨ Features
- Serves **static HTML files** directly from the server directory  
- Handles **one HTTP request at a time** (single-threaded design)  
- Properly formats HTTP/1.1 responses, including headers:  
  - **Status Line** → `200 OK` or `404 Not Found`  
  - **Content-Type** → based on requested file  
  - **Server** → customizable server name  
  - **Connection** → specifies whether to keep alive or close  
- Sends the **entire response in a single transmission** (`send()` call)  
- Compatible with both **web browsers** and **command-line tools**  

---

## 🚀 Running the Server
1. Place an HTML file (e.g., `helloworld.html`) in the same directory as `webServer.py`.  
2. Start the server:  

```bash
python webServer.py
```
3. Open a browser and navigate to:
- http://127.0.0.1:8080/helloworld.html

4.The server will respond with:
- 200 OK and the file content if the file exists
- 404 Not Found if the requested resource is missing

## 💡 Learning Impact
- Gained practical experience with low-level network sockets in Python
- Learned the structure and flow of HTTP requests and responses
- Implemented error handling and resource validation
- Built a project that bridges the gap between theory (TCP/IP & HTTP protocols) and practical application (serving real web pages)
