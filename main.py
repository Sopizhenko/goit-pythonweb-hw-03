import mimetypes
import pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-Length"]))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {
            key: value for key, value in [el.split("=") for el in data_parse.split("&")]
        }
        self.save_form_data(data_dict)

        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == "/":
            self.send_html_file("./templates/index.html")
        elif pr_url.path == "/message":
            self.send_html_file("./templates/message.html")
        elif pr_url.path == "/read":
            self.show_data()
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file("./templates/error.html", 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())

    def save_form_data(self, form_data):
        file_path = "./storage/data.json"
        # Load data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Timestamp as key
        timestamp = datetime.now().isoformat()
        data[timestamp] = form_data

        # Save data
        with open(file_path, "w") as file:
            json.dump(data, file)

    def show_data(self):
        file_path = "./storage/data.json"
        # Load data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Render data
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("./templates/read.html")
        output = template.render(data=data)

        # Send response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(output.encode())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()
