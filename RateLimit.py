import requests
import argparse
import random

class RateLimitTest:
    def __init__(self, args):
        self.args = args

    def banner(self):
        print("[*] [Rate Limit Test Template | By Afrizal F.A - R&D incrustwerush.org]\n")

    def useragent(self):
        arr = [
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
            "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"
        ]
        return random.choice(arr)

    def headersSet(self):
        return {
            "User-Agent": self.useragent()
        }

    def payloadSet(self, data):
        return data
    
    def checkRequest(self, headers, payload):
        try:
            r = requests.Session()
            resp = r.get(self.args.url, headers=headers, data=payload)
            return resp.text
        except Exception as e:
            return f"Request Error: {e}"

    def looper(self):
        try:
            with open(self.args.wordlist, "r") as file:
                for line in file:
                    word = line.strip()
                    response = self.checkRequest(self.headersSet(), self.payloadSet({"word": word}))
                    print(f"[*] Word: {word}\n[*] Response: {response}\n{'-'*50}")
        except Exception as e:
            print(f"[-] Error: {e}")

if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("-x", "--url", required=True, help="Target URL")
    arg.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    args = arg.parse_args()

    print("[*] [Start Testing]")

    App = RateLimitTest(args)
    App.banner()
    App.looper()
