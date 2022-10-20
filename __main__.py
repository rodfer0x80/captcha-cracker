import sys

from src import *

def run_txt():
    txt_cracker = TxtCracker()
    txt_cracker.runme()
    return 0


def run_img():
    img_cracker = ImgCracker()
    img_cracker.runme()
    return0


def main():
    argc = len(sys.argv)
    if argc != 2:
        sys.stdout.write(f"Usage ./sys.argv[0] <MODE::txt/img>\n")
        return -1
    mode = sys.argv[1]
    if mode == "txt":
        run_txt()
    elif mode == "img":
        run_img()
    else:
        sys.stdout.write(f"Usage ./sys.argv[0] <MODE::txt/img>\n")
        return -2
    return 0


if __name__ == '__main__':
    sys.exit(main())
