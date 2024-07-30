import unittest
from unittest import TestCase
import requests


class TestYandex(TestCase):
    def setUp(self) -> None:
        self.headers = {
            'Authorization': 'OAuth y0_AgAAAAB1YoTFAADLWwAAAAEMDS3HAAB-g53FRipF-5EhjG2e1SK6FxSh1Q'
        }

    def tearDown(self):
        params = {'path': 'Image'}
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                   params=params,
                                   headers=self.headers)

    def test_create_folder_201(self):
        params = {
            'path': 'Image'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_create_folder_409(self):
        params = {
            'path': 'Image'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        self.assertEqual(response.status_code, 409)

    def test_create_folder_400(self):
        params = {
            'path': '//Image/'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        self.assertEqual(response.status_code, 404)