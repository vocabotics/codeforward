# Design Document: VB-FORWARDER-002

## 1. Introduction

This document provides a high-level design overview of the Python scripts for file monitoring, concatenation, and uploading (VB-FORWARDER-002). The scripts are designed to monitor specific file types in a directory, concatenate their contents into a single HTML file, and upload this file to an SFTP server every 10 seconds. Additionally, the scripts host the HTML file on a local HTTP server.

## 2. System Overview

The system is composed of two main components:

1. **File Monitor and Uploader:** This component monitors the directory for specific file types (`.txt`, `.py`, `.css`, `.js`, `.json`), concatenates their contents into an HTML file (`latestcode.html`), and uploads this file to an SFTP server every 10 seconds.

2. **HTTP Server:** This component hosts the `latestcode.html` file on a local HTTP server, making it accessible via a web browser.

## 3. Detailed Design

### 3.1 File Monitor and Uploader

This component is implemented as a Python script that uses the `os`, `paramiko`, and `schedule` libraries. The script performs the following steps:

1. Reads the SFTP server address and login credentials from a text file (`credentials.txt`).

2. Monitors the directory for specific file types.

3. Concatenates the contents of the monitored files into an HTML file. Each file's contents are preceded by a summary that includes the file's name and modification date/time.

4. Uploads the HTML file to the SFTP server.

5. Repeats steps 2-4 every 10 seconds.

Error handling is implemented to handle errors that may occur when connecting to the SFTP server or uploading the file. If an error occurs, an error message is printed to the console.

### 3.2 HTTP Server

This component is implemented as a Python script that uses the `http.server`, `socketserver`, and `threading` libraries. The script starts a simple HTTP server on port 8000 that serves the files in the current directory. The server runs in a separate thread, so it doesn't block the rest of the script.

## 4. Future Enhancements

Possible future enhancements for the system include:

1. Adding support for more file types.

2. Allowing the user to configure the directory to be monitored, the SFTP server details, and the HTTP server port via a configuration file or command-line arguments.

3. Implementing a user interface for viewing the `latestcode.html` file in a more user-friendly format.

4. Adding support for secure FTP (FTPS) or other file transfer protocols.

5. Improving error handling and logging.

## 5. Conclusion

The Python scripts for file monitoring, concatenation, and uploading provide a simple and efficient solution for automatically updating and uploading an HTML file that contains the contents of specific file types in a directory. The system is flexible and can be easily extended or modified to meet different requirements.
