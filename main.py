try:
    import pywintypes
    import win32gui
    import win32con
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide , win32con.SW_HIDE)
    import ctypes
    import pickle
    import argparse
    import sys
    import requests
    import os
    import shutil
    import time
    import tempfile
    import urllib
    from itertools import count
    from urllib.parse import urlparse
except Exception as e:
    print(e.args)
    sys.exit()
def get_argv():
    try:
        parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Visualizza i comandi')
        parser.add_argument("-t", help="Ogni quanto modificare loo sfondo 1 - 2592000", default=5, dest="time", type=int)
        parser.add_argument("-u", help="Url per le api dell'immagine", dest="url", type=str)
        args = parser.parse_args()
        return args
    except Exception as e:
        print(e.args)
        sys.exit()
def get_file(url: str, folder: str, name: str, ext):
    try:
        if (folder != ''):
            if not os.path.exists(folder):
                os.makedirs(folder)
        with urllib.request.urlopen(url) as response:
            parsed_url_path = urllib.parse.urlparse(response.url).path
            filename = os.path.basename(parsed_url_path)
            file_extension = os.path.splitext(filename)
            file_ext = ext if (ext != None) else file_extension[1]
            with open(folder + name + file_ext, 'w+b') as f:
                shutil.copyfileobj(response, f)
        return name + file_ext
    except Exception as e:
        print(e.args)
        sys.exit()
def check_argv(argv):
    try:
        if (int(argv.time) < 1 or int(argv.time) > 2592000):
            print("Valore tempo non valido")
            sys.exit()
    except Exception as e:
        print(e.args)
        sys.exit()
    try:
        if (argv.url != None):
            result = urlparse(argv.url)
            response = requests.get(argv.url)
            if (not all([result.scheme, result.netloc]) or response.status_code != 200):
                print("URL non valido")
                sys.exit()
    except Exception as e:
        print(e.args)
        sys.exit()
def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        sys.exit()
def main():
    try:
        connected_to_internet()
    except Exception as e:
        print(e.args)
        sys.exit()
    try:
        argv = get_argv()
        check_argv(argv)
    except Exception as e:
        print(e.args)
        sys.exit()
    try:
        wait = int(argv.time)
        if (argv.url == None):
            url = 'https://picsum.photos/3840/2160'
        path_temp = tempfile.mkdtemp()
    except Exception as e:
        print(e.args)
        sys.exit()
    for i in count(0):
        try:
            SPI_SETDESKWALLPAPER = 20
            name_img = get_file(url, path_temp, 'bg', None)
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_temp + name_img, 3)
            if os.path.exists(path_temp + name_img):
                os.remove(path_temp + name_img)
            time.sleep(wait * 60)
        except Exception as e:
            print(e.args)
            shutil.rmtree(path_temp)
            sys.exit()
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e.args)
        sys.exit()
