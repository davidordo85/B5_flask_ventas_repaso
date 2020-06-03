import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase):
    def test_server_is_on(self):
        loquemedevuelve = self.client.get("/")
        self.assertEqual(loquemedevuelve.status_code, 200)
        


if __name__== '__main__':
    unittest.main()
       