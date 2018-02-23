import unittest

from tests.helper.MusiciansApiClient import MusiciansApiClient


class TestForInvalidMusician(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        request_model = {
            "name": 4,
            "surname": 5
        }

        api_client = MusiciansApiClient()
        cls.response = api_client.create_musician(request_model)

    def test_it_should_return_bad_request(self):
        self.assertEqual(self.response.status_code, 400)


