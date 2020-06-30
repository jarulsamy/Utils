# Rewrite-History

A simple CLI tool to spoof the days git commits occur. Don't ask why I needed this :smile:.

`rewrite.sh` is a simpler version that shouldn't really be used anymore.

## Usage

Run with:

```
$ ./rewrite.py
```
>By default this uses ZSH. It can be switched using the `-s` flag.

View the builtin help with:
```
$ ./rewrite.py -h
usage: rewrite.py [-h] [-t TIMESTAMP] [-s SHELL] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -t TIMESTAMP, --timestamp TIMESTAMP
                        Custom timestamp.
  -s SHELL, --shell SHELL
                        Custom shell
  -c, --color           Enable color shell
```

