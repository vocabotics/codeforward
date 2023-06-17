################################################################################
# File Name: monitor.py
# Author: vocabotics - Jon Ross
# Twitter: @vocaboticsai
# Github: https://github.com/vocabotics/codeforward
# Date: 18/6/2023
################################################################################

import os
import time
import paramiko

def concatfiles():
    with open('latestcode.html', 'w') as outfile:
        for filename in os.listdir('.'):
            if filename.endswith(('.txt', '.py', '.css', '.js', '.json')):
                with open(filename) as infile:
                    outfile.write(f'<h2>File: {filename}</h2>\n')
                    outfile.write(f'<p>Modified: {time.ctime(os.path.getmtime(filename))}</p>\n')
                    outfile.write('<hr>\n')
                    outfile.write('<pre>\n')
                    outfile.write(infile.read())
                    outfile.write('</pre>\n')
                    outfile.write('<br><br>\n')

def upload_file():
    with open('credentials.txt', 'r') as f:
        server = f.readline().strip()
        username = f.readline().strip()
        password = f.readline().strip()

    try:
        transport = paramiko.Transport((server, 22))
        transport.connect(username=username, password=password)
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
        return
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
        return
    except paramiko.BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
        return
    except Exception as e:
        print("Operation error: %s" % e)
        return

    try:
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put('latestcode.html', './latestcode.html')  # replace with the correct path
        print("File successfully uploaded to %s" % server)
    except Exception as e:
        print("Failed to upload file: %s" % e)

    finally:
        sftp.close()
        transport.close()

if __name__ == "__main__":
    try:
        while True:
            concatfiles()  # update latestcode.html
            upload_file()  # upload the file to the SFTP server
            time.sleep(10)  # wait for 10 seconds
    except KeyboardInterrupt:
        print("Stopping...")
