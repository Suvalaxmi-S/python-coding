import pytest
from list import largest  # Replace 'your_module' with the name of your Python file without the .py extension

def test_largest():
    items = ['apple', 'cucumber', 'grapes']
    assert largest(items) == 'cucumber'

    items = ['cat', 'dog', 'elephant']
    assert largest(items) == 'elephant'

    items = ['short', 'longer', 'longest']
    assert largest(items) == 'longest'

    items = ['a', 'bb', 'ccc']
    assert largest(items) == 'ccc'

    items = []
    assert largest(items) == ''

if __name__ == '__main__':
    pytest.main()
