# codeforward - File Monitoring, Concatenation, and Uploading Scripts

This project contains Python scripts for monitoring specific file types in a directory, concatenating their contents into a single HTML file, and uploading this file to an SFTP server every 10 seconds. Additionally, the scripts host the HTML file on a local HTTP server.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Python libraries: `os`, `paramiko`, `schedule`, `http.server`, `socketserver`, `threading`

You can install the required Python libraries using pip:

```bash
pip install paramiko schedule
```

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/vocabotics/codeforward.git
```

## Running the Scripts

Run the file monitor and uploader script:

```bash
python monitorftp.py
```

In a separate terminal, run the HTTP server script:

```bash
python http_server.py
```

## Testing

See [Test Document: VB-FORWARDER-003](link-to-test-document) for details on how to test the scripts.

## Authors

- Jon Ross

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3 model that helped generate these scripts.
```
