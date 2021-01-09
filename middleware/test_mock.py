import unittest
from mock import Mock


class TestMock(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mock(self):

        add = Mock(return_value=8)
        self.assertEqual(7,add(3,4))