# server.py —— 一个最小的本地 API 服务，专门用来练 HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send(200, {"message": "欢迎", "method": "GET"})
        elif self.path == "/todos":
            self._send(
                200,
                {
                    "todos": [
                        {"id": 1, "title": "学 HTTP"},
                        {"id": 2, "title": "写项目"},
                    ]
                },
            )
        elif self.path == "/todos/1":
            self._send(200, {"id": 1, "title": "学 HTTP", "done": False})
        else:
            self._send(404, {"error": "not found", "path": self.path})

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(n).decode("utf-8")
        try:
            data = json.loads(raw) if raw else {}
        except Exception:
            return self._send(400, {"error": "invalid JSON"})
        if "title" not in data:
            return self._send(422, {"error": "title is required", "got": data})
        self._send(201, {"id": 3, "created": data})

    def log_message(self, fmt, *args):
        print(f"[{self.command}] {self.path} -> {args[1]}")


HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
