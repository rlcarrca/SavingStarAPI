import os
import pep8
import re
from nose.tools import assert_equals


class TestCodeFormat:

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

    def test_pep8_conformance(self):
        """Test that we conform to PEP8"""
        target = os.path.join(os.path.dirname(__file__), '..')
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files([target])
        assert_equals(result.total_errors, 0)
