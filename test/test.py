"""
Tests ClickRunnerTestCase
"""
from __future__ import print_function

import click
from click_tester import ClickRunnerTestCase


@click.command()
@click.option('--raise-err/--no-raise-err', default=False)
def my_command(raise_err):
    if raise_err:
        print('about to throw')
        raise RuntimeError('EXPECTED EXPLODE!')
    print('test_output')


class TestCLI(ClickRunnerTestCase):
    def test_command_execution(self):
        result = self.expect_invoke_success(my_command)
        self.assertEqual(result.output, 'test_output\n')

    def test_regex_match_output(self):
        self.expect_invoke_success(my_command, None, r'^\w+_\w+$')

    def test_print_unexpected_exception_and_traceback(self):
        # Purposeful raise of error to test that traceback is printed and result.exception is raised
        self.assertRaises(RuntimeError, self.expect_invoke_success, my_command, ['--raise-err'])

    def test_command_raises_expected_error(self):
        result = self.expect_invoke_raises_error(my_command, ['--raise-err'],
                                                 RuntimeError, r'about to throw')
        self.assertEqual(result.output, 'about to throw\n')
