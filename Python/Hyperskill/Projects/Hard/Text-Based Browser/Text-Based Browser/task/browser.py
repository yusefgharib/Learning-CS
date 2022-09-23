import os, sys, re, requests
from bs4 import BeautifulSoup
from colorama import Fore


class Browser:
    def __init__(self):
        self.visited, self.file_name, self.folder_name = [], None, sys.argv[1]

    def create_folder(self):
        if not os.access(self.folder_name, os.F_OK):
            os.makedirs(self.folder_name)

    def create_file(self, content):
        with open(f"{self.folder_name}/{self.file_name}", "wb") as f:
            f.write(content)

    def check_files(self):
        if os.access(f'{self.folder_name}/{self.file_name}', os.F_OK):
            with open(f'{self.folder_name}/{self.file_name}', "rb") as f:
                return print(f.read().decode("utf-8"))
        return False

    def get_url(self):
        url_ = input()
        self.file_name = url_.replace(".com", "") if url_.endswith('.com') \
            else url_.replace(".org", "")
        self.visited.append(self.file_name) if url_ != "back" and url_ != "exit" else 0
        return url_

    def back(self):
        if len(self.visited) > 1:
            with open(f'{self.folder_name}/{self.visited[-2]}', "r") as f:
                print(f.read())


def main():
    browser = Browser()
    while True:
        browser.create_folder()
        url = browser.get_url()
        if re.search(r"[.]...?$", url):
            url = 'https://' + url if not url.startswith('https://') else url
            if not browser.check_files():
                soup = BeautifulSoup(requests.get(url).content, "html.parser").body.descendants
                tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "a", "ul", "ol", "li"]
                content = ''
                for descendant in soup:
                    if descendant.name in tags:
                        if descendant.name == 'a':
                            content += Fore.BLUE + descendant.get_text()
                        else:
                            content += descendant.get_text()
                browser.create_file(content.encode('utf-8'))
                print(content)
        else:
            exit() if url == 'exit' else browser.back() if url == 'back' \
                else print("Incorrect URL")


if __name__ == "__main__":
    main()
