import re
from nose.tools import assert_equals

EMAIL_REGEXP = r'[\S.]+@[\S.]+'


def multiply(x, y):
    return (x*y)


class TestDummy:

    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")

    def setup(self):
        print ("TestDummy:setup() before each test method")

    def teardown(self):
        print ("TestDummy:teardown() after each test method")

    def test_numbers_3_4(self):
        assert multiply(3, 4) == 12

    def test_strings_a_3(self):
        assert multiply('a', 3) == 'aaa'

    def test_numbers_5_6(self):
        print 'test_numbers_5_6()  <====================== actual test code'
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print 'test_strings_b_2()  <====================== actual test code'
        assert_equals(multiply('b', 2), 'bb')

    def test_email_regexp(self):
        # a regular e-mail address should match
        assert re.match(EMAIL_REGEXP, 'test@nowhere.com')

        # no domain should fail
        assert not re.match(EMAIL_REGEXP, 'test@')
