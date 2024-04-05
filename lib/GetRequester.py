import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        try:
            json_data = json.loads(self.get_response_body())
        except json.JSONDecodeError:
            json_data = None
        return json_data
