import unittest

from tests.helper.MusiciansApiClient import MusiciansApiClient


class TestForValidMusicians(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        request_model = {
            "name": "Ari",
            "surname": "Dinar",
            "band": "Noband",
            "age": 44,
            "albums": ["album1"],
            "instrument": "Guitar"
        }

        api_client = MusiciansApiClient()
        cls.response = api_client.create_musician(request_model)

    def test_it_should_return_201(self):
        self.assertEqual(self.response.status_code, 201)

    def test_name_should_be_true(self):
        body = self.response.json()
        self.assertEqual(body["name"], "Ari")

    def test_surname_should_be_true(self):
        body = self.response.json()
        self.assertEqual(body["surname"], "Dinar")

    def test_age_should_be_true(self):
        body = self.response.json()
        self.assertEqual(body["age"], 44)

    def test_albums_should_be_true(self):
        body = self.response.json()
        self.assertEqual(len(body["albums"]), 1)
        self.assertEqual(body["albums"][0], "album1")

    def test_instrument_should_be_true(self):
        body = self.response.json()
        self.assertEqual(body["instrument"], "Guitar")
