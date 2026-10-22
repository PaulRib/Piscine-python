def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which function
    (item) is true. If function is None, return the items that are true.
    """
    if function is None:
        for i in iterable:
            if i:
                yield i
    else:
        for i in iterable:
            if function(i):
                yield i
