#Airport in Python

I've translated the basic functionality from Ruby/Javascript to Python.
- Planes can land and take off.
- Parked planes are stored in 'planes'.
- Weather is randomly generated (and stubbed in tests).
- An excpetion is raised if plane tries to land when stormy.

Note:
- To allow mocks to work in tests, you need to run in Python version 3.
$ alias python='python3'

- To run tests from command line, run test files:
$ python ./spec/plane_test.py
$ python ./spec/airport_test.py

## Testing in python REPL:
$ python
from airport import Airport
from plane import Plane
airport = Airport()
plane = Plane()
airport.land(plane)
