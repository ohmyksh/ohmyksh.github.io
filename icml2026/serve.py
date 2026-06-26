#!/usr/bin/env python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

ALLOWED = {"/", "/index.html", "/coex.html", "/coex-guide.html", "/explore-seoul.html", "/other-tips.html", "/socials.html", "/workshops.html", "/must-visit.html", "/fonts.css", "/source.json"}
ALLOWED_PREFIX = "/img/"

class RestrictedHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0]
        if path not in ALLOWED and not path.startswith(ALLOWED_PREFIX):
            self.send_error(403)
            return
        super().do_GET()

    def log_message(self, fmt, *args):
        pass  # silence logs

os.chdir(os.path.dirname(os.path.abspath(__file__)))
HTTPServer(("", 9124), RestrictedHandler).serve_forever()
