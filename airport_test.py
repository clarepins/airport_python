from helper import *
from airport import Airport
from random import Random

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()

    def test_land(self):
        """
        Test that airport can land a plane
        """
        self.airport.land('plane')
        self.assertEqual(self.airport.planes, ['plane'])

    def test_take_off(self):
        """
        Test airport can take off a plane
        """
        self.airport.land('plane1')
        self.airport.land('plane2')
        self.airport.take_off('plane1')
        self.assertEqual(self.airport.planes, ['plane2'])

    def test_stormy(self):
        """
        Weather can be stormy
        """
        self.airport.stormy = MagicMock(return_value=True)
        self.assertEqual(self.airport.stormy(), True)

    def test_sunny(self):
        """
        Weather can be sunny
        """
        self.airport.stormy = MagicMock(return_value=False)
        self.assertEqual(self.airport.stormy(), False)

    def test_cant_land_when_stormy(self):
        """
        Plane can't land when _stormy
        """
        self.airport.stormy = MagicMock(return_value=True)
        with self.assertRaises(Exception):
            self.airport.land('plane')

if __name__ == '__main__':
    unittest.main()
