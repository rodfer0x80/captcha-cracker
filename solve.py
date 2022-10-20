import os
import sys
import base64

import requests
from PIL import Image


if __name__ == '__main__':
    r = requests.get("http://challenge01.root-me.org/programmation/ch8/")
    s = r.text.split("src=")[-1].split(",")[1].split("\"")[0].encode("utf-8")
    with open("captcha.png", "wb") as fh:
            fh.write(base64.decodebytes(s))
    os.rename("captcha.png", "data/captcha.png")
    os.system("convert data/captcha.png data/captcha.gif")
    os.remove("data/captcha.png")
    os.system("python __main__.py txt")
    sys.exit(0)
