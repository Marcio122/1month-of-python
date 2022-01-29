import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #Tests for 'name_function.py'
    def test_first_last_name(self):
        #Do names like Marcio Jeovety work?
        formatted_name = get_formatted_name('marcio', 'jeovety')
        self.assertEqual(formatted_name, 'Marcio Jeovety')

if __name__ == '__main__':
    unittest.main()