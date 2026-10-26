"""
CS 412 Lab 0 Unit tests for Students

When running locally, you will need to pip install the gradescope
packages in order for this to run.

  pip install gradescope_utils

This test verifies that the name of the file/assignment is correct
and also runs the example data provided in the lab.  To run these tests
  py
"""


import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from io import StringIO
from unittest.mock import patch

from cs412_lab0_a import main as lab0_main

class TestFiles(unittest.TestCase):

    @weight(1)
    def test_t1_submitted_files(self):
        """Check submitted files"""
        missing_files = check_submitted_files(['cs412_lab0_a.py'], base='.')
        for path in missing_files:
            print(' Missing {0}'.format(path))
        self.assertEqual(len(missing_files), 0, 'Missing some required files!')
        print('\nAll required files submitted!')
    

    
    @weight(4)
    @number("1.2")
    @patch('sys.stdout', new_callable=StringIO)
    def test_t2a_pa_example_1(self, mock_out):
        """Case 1 from write up"""
        with patch('sys.stdin', new = StringIO(
            """5
dog ogday
cat atcay
pig igpay
froot ootfray
loops oopslay
atcay ittenkay oopslay""")):
            lab0_main()
        self.assertEqual(mock_out.getvalue(),
            'cat ??? loops \n')


    @weight(5)
    @number("1.3")
    @patch('sys.stdout', new_callable=StringIO)
    def test_t2a_pa_example_2(self, mock_out):
        """Case 1 from write up"""
        large_file = open('lab0_t1_in.txt')
        large_file_data = large_file.read()
        large_file.close()

        with patch('sys.stdin', new = StringIO(large_file_data)):
            lab0_main()
        large_exp_file = open('lab0_t1_exp.txt')
        large_exp_file_data = large_exp_file.read()
        large_exp_file.close()
        self.assertEqual(mock_out.getvalue(),
            large_exp_file_data)
