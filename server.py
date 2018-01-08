from http.server import SimpleHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import shutil
import posixpath
import os
import argparse
import sys
import urllib
import html
import io
import subprocess
from string import Template

def get_markdown():
    markdown = None

    if shutil.which("pd"):
        markdown = lambda x: subprocess.run(
            ["pd", "-f", "markdown", "-t", "html"],
            input = x.encode("utf-8"),
            stdout = subprocess.PIPE).stdout.decode("utf-8")

        else:
            try:
                import markdown2
                _md_extras = [
                    "code-friendly",
                    "fenced-code-blocks",
                    "footnotes",
                    "header-ids"]
                markdown = markdown2.Markdown(extras = _md_extras).convert

            except ImportError:
                pass

            if markdown is None:
                css = ""
                if os.path.isfile("css.css"): #need to rename
                    css = open("css.css").read() #need to rename
                elif os.path.isfile(os.path.expanduser("~/.css.css")):
                    css = open(os.path.expanduser("~/.css.css"))
                return css

def cli():
    parser = argparse.ArgumentParser(
        description="derp",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('dir', help="folder to server", nargs='?', default=os.getcwd())

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(args.dir, " is not a valid dir")
    os.chdir(args.dir)