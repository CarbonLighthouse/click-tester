from __future__ import print_function

import sys
import traceback
from unittest import TestCase

from click.testing import CliRunner


class ClickRunnerTestCase(TestCase):

    def __init__(self, method_name):
        super(ClickRunnerTestCase, self).__init__(methodName=method_name)
        self.runner = CliRunner()

    def expect_invoke_success(self, cmd, opts=None, expected_output_regexp=None):
        result = self.runner.invoke(cmd, opts)

        if expected_output_regexp is not None:
            self.assertRegex(result.output, expected_output_regexp)
        elif result.output:
            print(result.output)

        if result.exception:
            traceback.print_tb(result.exc_info[2])
            raise result.exception

        self.assertEqual(result.exit_code, 0, msg=result.exc_info)

        return result

    def expect_invoke_raises_error(self, cmd, opts, exception_class=SystemExit,
                                   expected_output_regexp=None):
        result = self.runner.invoke(cmd, opts)

        self.assertFalse(result.exit_code == 0, 'expected non-zero exit code')
        self.assertIsInstance(result.exception, exception_class)

        if expected_output_regexp is not None:
            self.assertRegex(result.output, expected_output_regexp)

        return result

    def assertRegex(self, text, expected_regex):
        if sys.version_info < (3, 0):
            return self.assertRegexpMatches(text, expected_regex)

        return super(ClickRunnerTestCase, self).assertRegex(text, expected_regex)
