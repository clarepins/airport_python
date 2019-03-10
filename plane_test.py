import unittest
from plane import Plane

class TestPlane(unittest.TestCase):

    def test_plane(self):
        """
        Test that a plane can be created
        """
        plane = Plane()
        self.assertIsInstance(plane, Plane)

if __name__ == '__main__':
    unittest.main()
