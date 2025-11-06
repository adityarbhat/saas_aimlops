from http.server import BaseHTTPRequestHandler
from openai import OpenAI  # type: ignore

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = OpenAI()
        prompt = [{"role": "user", "content": "Come up with a new business idea for AI Agents"}]
        response = client.chat.completions.create(model="gpt-4", messages=prompt)
        idea = response.choices[0].message.content

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(idea.encode())
        return