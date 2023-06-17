# VB-FORWARDER-001: Python Scripts for File Monitoring, Concatenation, and Uploading

## 1. Python Version

The scripts should be compatible with Python 3.6 and above.

## 2. Libraries

The following Python libraries are required:

- `os`: This is a built-in Python library, so no installation is required. It's used for interacting with the operating system, such as reading the list of files in a directory.

- `paramiko`: This library is used for SSH and SFTP connections. It can be installed via pip with `pip install paramiko`.

- `schedule`: This library is used to schedule tasks to run at regular intervals. It can be installed via pip with `pip install schedule`.

- `http.server` and `socketserver`: These are built-in Python libraries used to create a simple HTTP server.

- `threading`: This is a built-in Python library used to run the server in a separate thread.

## 3. File Types

The scripts monitor files with the extensions `.txt`, `.py`, `.css`, `.js`, and `.json`.

## 4. Credentials File

The scripts require a text file named `credentials.txt` that contains the SFTP server address, username, and password on separate lines.

## 5. Output File

The scripts create or update a file named `latestcode.html` that contains the contents of all monitored files.

## 6. SFTP Server

The scripts upload `latestcode.html` to an SFTP server. The server address and login credentials are read from `credentials.txt`.

## 7. HTTP Server

The scripts start a simple HTTP server on port 8000 that serves the files in the current directory.

## 8. Error Handling

The scripts handle errors that may occur when connecting to the SFTP server or uploading the file. If an error occurs, an error message is printed to the console.

## 9. Logging

The scripts log a message to the console each time the file is successfully uploaded to the SFTP server.

## 10. Execution

The scripts run indefinitely until stopped by the user. The `latestcode.html` file is updated and uploaded to the SFTP server every 10 seconds.
