#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

from Manager import QueueClient
from Task import Task


class Proxy(BaseHTTPRequestHandler):
    """
    A simple HTTP proxy server that handles GET and POST requests.

    GET requests retrieve tasks from the task queue and return them as JSON responses.
    POST requests receive JSON-encoded tasks, process them, and put the results into the result queue.

    Attributes:
    - client: An instance of QueueClient for communication with the task and result queues.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor initializing the Proxy instance and its QueueClient.
        """
        self.client = QueueClient()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """
        Handles GET requests by sending a JSON response containing a task from the task queue.
        """
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        task = self.client.tasks.get()
        self.wfile.write(bytes(task.to_json(), "utf-8"))

    def do_POST(self):
        """
        Handles POST requests by processing JSON-encoded tasks, putting results into the result queue,
        and sending a JSON response with a status message.
        """
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content_length = int(self.headers.get("content-length"))
        content = self.rfile.read(content_length)
        task = Task.from_json(content.decode())
        self.client.results.put(task)
        self.wfile.write(bytes(dumps({"status": "ok"}), "utf-8"))


def run(server_class=HTTPServer, handler_class=Proxy):
    """
    Runs the HTTP server with the specified server and handler classes.

    Args:
    - server_class: The class for the HTTP server (default is HTTPServer).
    - handler_class: The class for the request handler (default is Proxy).

    The server is set to listen on localhost at port 8000 and serves forever.
    """
    server_address = ("localhost", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
