

def write_inner_nonlocal():
    """
    Python 3.x introduced the ``nonlocal`` directive. It resolves the problem of accessing an immutable variable
    created in the outer scope.
    """
    x = 1

    def foo():
        nonlocal x
        x = 2
        print('inner: {}'.format(x))
    print('outer before: {}'.format(x))
    foo()
    print('outer after: {}'.format(x))


def write_inner_attr():
    """
    Mutable variables are writable as expected from the inner scope.
    In Python 2.x this was the only way of writing to a variable in the outer scope.
    """
    x = dict()
    x['val'] = 1

    def foo():
        x['val'] = 2
        print('inner: {}'.format(x['val']))

    print('outer before: {}'.format(x['val']))
    foo()
    print('outer after: {}'.format(x['val']))


def write_inner():
    """
    An immutable variable *is overwritten* when assigned from the inner scope.
    Doesn't work as you would expect.
    """
    x = 1

    def foo():
        x = 2
        print('inner: {}'.format(x))

    print('outer before: {}'.format(x))
    foo()
    print('outer after: {}'.format(x))


def read_inner():
    """
    An immutable variable *is* readble from the inner scope.
    Works as expected.
    """
    x = 1

    def foo():
        print('inner: {}'.format(x))
    print('outer: {}'.format(x))
    foo()


tests = [read_inner, write_inner, write_inner_attr, write_inner_nonlocal]
hr = '\n' + ' ' * 4 + '-' * 40

if __name__ == '__main__':
    for test in tests:
        print(hr)
        print(test.__doc__[1:])
        test()
