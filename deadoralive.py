import requests
import urllib3
import sys
import argparse


settings = {
    "scope" : "scope.txt",
    "scheme" : "http://",
    "port" : 80,
    "timeout" : 0.1
}

if (len(sys.argv) > 1):
    console_mode = True
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--scope', type=str,
                        help='file with scope')
    parser.add_argument('--scheme', type=str,
                        help='uri scheme', default="http://")
    parser.add_argument('--port','-p', type=str,
                        help='port to connect', default=80)
    parser.add_argument('--timeout', type=float,
                        help='timeout', default=0.2)

    args = parser.parse_args()
    if(not args.scope):
        print("'--scope' was omited")
        exit(-1)
    settings["scope"] = args.scope
    settings["scheme"] = args.scheme
    settings["port"] = args.port
    settings["timeout"] = args.timeout



def check_url(host, scheme, port=80, timeout=0.2):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = scheme + host + ":" + str(port)
        res = requests.get(url, timeout=timeout, verify=False)
        print(url)
    except Exception as ex:
        # print("ex" + ex)
        return


def run_checker(settings):
    content = open(settings["scope"]).read()
    scope = content.split("\n")
    for host in scope:
        check_url(host, settings["scheme"], settings["port"], settings["timeout"])

run_checker(settings)
