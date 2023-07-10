# URLs Extractor

Extract URLs from a website.

## Installation Instructions

```sh
$ git clone https://github.com/ilhamrzr/url-extractor
$ cd url-extractor
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 extract-url.py
```

## Usage

```sh
python3 extract-url.py -h
```

```console
usage: extract-url.py [-h] [-u URL] [-em EXTENSIONS] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Website URL
  -em EXTENSIONS, --extensions EXTENSIONS
                        File extensions to extract (comma-separated)
  -o OUTPUT, --output OUTPUT
                        Output file path (in .txt format)
```

## Running

Basic

```sh
python3 extract-url.py -u https://example.com/
```

with extension

```sh
python3 extract-url.py -u https://example.com/ -em js,css
```

or

```sh
python3 extract-url.py -u https://example.com/ -em js,css -o result.txt
```

## How to use

[https://youtu.be/5Nygz0-jCOc](https://youtu.be/5Nygz0-jCOc)