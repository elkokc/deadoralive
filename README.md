# deadoralive
Script to define alive hosts on early stage of pentest. 

# Installation & Usage
```
git clone https://github.com/elkokc/deadoralive.git
cd deadoralive
pip install requests
python3 deadoralive.py --scope <FILE>
```

Options
-------
```
usage: deadoralive.py [-h] [--scope SCOPE] [--scheme SCHEME] [--port PORT]
                      [--timeout TIMEOUT]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  --scope SCOPE         file with scope
  --scheme SCHEME       uri scheme
  --port PORT, -p PORT  port to connect
  --timeout TIMEOUT     timeout
  ```
