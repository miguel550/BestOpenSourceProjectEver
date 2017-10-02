import unittest
import sys
import os
sys.path.append('..')
from driver import main


class TestMainMethods(unittest.TestCase):
    """Unit testing for BestOpenSourceProjectEver"""

    def test_main(self):
        """Main unit test to test main function"""
        main_test_file = "test_main.txt"
        main.setup(main_test_file)

        with open(main_test_file) as my_file:
            content = my_file.readlines()

        content = [x.strip() for x in content]
        self.assertEqual(content[0], "Hello World :D")

        os.remove(main_test_file)


if __name__ == '__main__':
    unittest.main()
