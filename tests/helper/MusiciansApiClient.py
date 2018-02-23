import requests


class MusiciansApiClient:
    def __init__(self):
        self.base_url = "http://reqres.in"

    def create_musician(self, create_musician_request_model):
        url = self.base_url + "/api/musician"
        return requests.post(url, data=create_musician_request_model)
