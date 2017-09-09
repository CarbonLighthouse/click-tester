# click-tester

Provides utilities for testing command line tools built with [Pocoo Click library](http://click.pocoo.org/6/).

### Install

```
pip install click-tester
```

### ClickRunnerTestCase

A `unittest.TestCase` subclass which provides convenience methods for testing click commands.
Handles and displays errors, traceback information and command output.

```python
import click
from click_tester import ClickRunnerTestCase


@click.command()
@click.option('--noun')
def hello(noun):
    print('hello ' + noun + '!')


class TestHelloCmd(ClickRunnerTestCase):
    def test_message(self):
        self.expect_invoke_success(my_command,
                                   ['--noun=world'],
                                   r'^hello world!')
```
