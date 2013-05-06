import unittest

from robotnik.util import string_version_compare


# {'status': True, 'type': 'updated'}
# {'status': False, 'type': 'minor_outdated'}
# {'status': False, 'type': 'major_outdated'}
class StringVersionComparisonTest(unittest.TestCase):

    def test_simple_compare_should_be_updated(self):
        result = string_version_compare('>=2.1.0', '2.2.0')
        self.assertEqual(result, {'status': True, 'type': 'updated'})

    def test_simple_compare_should_be_major_outdated(self):
        result = string_version_compare('>=2.1.0', '1.2.0')
        self.assertEqual(result, {'status': False, 'type': 'major_outdated'})

    def test_simple_compare_should_be_minor_outdated(self):
        result = string_version_compare('>=2.1.0', '2.0.0')
        self.assertEqual(result, {'status': False, 'type': 'minor_outdated'})

    def test_complex_compare_should_be_updated(self):
        result = string_version_compare('>=2.1.0,<=2.2.0', '2.2.0')
        self.assertEqual(result, {'status': True, 'type': 'updated'})

    def test_complex_compare_should_be_major_outdated(self):
        result = string_version_compare('>=2.1.0,<=3.2.0', '4.2.0')
        self.assertEqual(result, {'status': False, 'type': 'major_outdated'})

    def test_complex_compare_should_be_minor_outdated(self):
        result = string_version_compare('>=2.1.0,<2.2.0', '2.3.0')
        self.assertEqual(result, {'status': False, 'type': 'minor_outdated'})

if __name__ == '__main__':
    unittest.main()
