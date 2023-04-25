from unittest import TestCase


def print_function():
    print("Hi Python")


class Test(TestCase):
    def test_print_function(self):
        from io import StringIO
        import sys

        console_output = StringIO()
        sys.stdout = console_output

        print_function()

        sys.stdout = sys.__stdout__

        xy = console_output.getvalue()

        self.assertEqual(xy.strip(), "Hi Python")
