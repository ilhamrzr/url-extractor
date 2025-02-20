import argparse
import requests
import warnings
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from termcolor import colored

warnings.simplefilter('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

def detect_scheme(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        test_url = "https://" + url
        try:
            response = requests.head(test_url, timeout=3, allow_redirects=True, verify=False)
            if response.status_code < 400:
                return test_url
        except requests.RequestException:
            pass
        return "http://" + url
    return url
def extract_urls(url, extensions=None):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(colored(f"ERROR: Gagal mengakses {url}. Pesan: {e}", "red"))
        return []
        
    soup = BeautifulSoup(response.content, 'html.parser')

    base_url = response.url
    urls = []
    for element in soup.find_all(['a', 'img', 'script', 'link']):
        url = element.get('src') or element.get('href')
        if url:
            parsed_url = urlparse(url)
            file_ext = parsed_url.path.split('.')[-1]

            if extensions is None or file_ext in extensions:
                absolute_url = urljoin(base_url, url)
                urls.append(absolute_url)

    return urls


def print_banner():
    banner = r"""
  _   _ ___ _      ___     _               _           
 | | | | _ \ |    | __|_ _| |_ _ _ __ _ __| |_ ___ _ _ 
 | |_| |   / |__  | _|\ \ /  _| '_/ _` / _|  _/ _ \ '_|
  \___/|_|_\____| |___/_\_\\__|_| \__,_\__|\__\___/_|
                        # Coded by Ilham | @ilhamrzr
"""
    print(colored(banner, 'cyan'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, help='Website URL')
    parser.add_argument('-em', '--extensions', type=str,
                        help='File extensions to extract (comma-separated)')
    parser.add_argument('-o', '--output', type=str,
                        help='Output file path (in .txt format)')

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
    else:
        print_banner()

        website_url = detect_scheme(args.url)
        print(colored(f"Scanning: {website_url}", "yellow"))
        file_extensions = args.extensions.split(
            ',') if args.extensions else None

        urls = extract_urls(website_url, file_extensions)

        if args.output:
            with open(args.output, 'w') as f:
                for url in urls:
                    f.write(url + '\n')
            print('The extracted URLs have been saved in the file:',
                  colored(args.output, 'green'))
        else:
            for url in urls:
                print(url)
