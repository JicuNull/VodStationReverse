import unittest
import os
from client.vodafone_client import VodafoneClient as Client


class VodafoneClientTest(unittest.TestCase):

    PASS = os.environ.get('PASSWORD')

    def test_login(self):
        client = Client()
        self.assertTrue(client.login(self.PASS).success())

    def test_firewall(self):
        client = Client()
        client.login(self.PASS)
        self.assertTrue(client.toggle_firewall(True))


if __name__ == '__main__':
    unittest.main()
