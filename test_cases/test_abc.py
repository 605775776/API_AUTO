import unittest

class TestTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_abc(self):
        a = 1
        b = 1
        self.assertEqual(a, b)