from click.testing import CliRunner
import traceback
from unittest import TestCase


class ClickRunnerTestCase(TestCase):

    def __init__(self, method_name):
        super(ClickRunnerTestCase, self).__init__(methodName=method_name)
        self.runner = CliRunner()

    def invoke_runner(self, cmd, opts):
        return self.runner.invoke(cmd, opts)

    def expect_invoke_success(self, cmd, opts, expected_output_regexp=None):
        result = self.invoke_runner(cmd, opts)

        if expected_output_regexp is not None:
            self.assertRegexpMatches(result.output, expected_output_regexp)
        elif result.output:
            print result.output

        if result.exception:
            traceback.print_tb(result.exc_info[2])
            raise result.exception

        self.assertEqual(result.exit_code, 0, msg=result.exc_info)

        return result

    def expect_invoke_raises_error(self, cmd, opts, exception_class=SystemExit,
                                   expected_output_regexp=None):
        result = self.invoke_runner(cmd, opts)

        self.assertFalse(result.exit_code == 0, 'expected non-zero exit code')
        self.assertIsInstance(result.exception, exception_class)

        if expected_output_regexp is not None:
            self.assertRegexpMatches(result.output, expected_output_regexp)

        return result
