# Doctest flags/directives - most common examples
import doctest


def example_ellipsis():
    """
    ELLIPSIS - replaces ... with any text
    
    Without flag (FAILS):
    >>> object()  # doctest: +SKIP
    <object object at 0x...>
    
    With +ELLIPSIS flag:
    >>> object()  # doctest: +ELLIPSIS
    <object object at 0x...>
    """
    ...


def example_normalize_whitespace():
    """
    NORMALIZE_WHITESPACE - ignores extra spaces/tabs
    
    Without flag (FAILS):
    >>> print("Hello    World")  # doctest: +SKIP
    Hello World
    
    With +NORMALIZE_WHITESPACE:
    >>> print("Hello    World")  # doctest: +NORMALIZE_WHITESPACE  
    Hello World
    """
    ...


def example_ignore_exception_detail():
    """
    IGNORE_EXCEPTION_DETAIL - ignores exception message details
    
    Without flag (FAILS - exact message required):
    >>> 1/0  # doctest: +SKIP
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    
    With +IGNORE_EXCEPTION_DETAIL:
    >>> 1/0  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ZeroDivisionError: ---any message here---
    """
    ...


def example_dont_accept_blankline():
    """
    DONT_ACCEPT_BLANKLINE - treats <BLANKLINE> literally

    Normal behavior (blank line):
    >>> print("Line1\\n\\nLine2")
    Line1
    <BLANKLINE>
    Line2

    With +DONT_ACCEPT_BLANKLINE:
    >>> print("Line1\\n\\nLine2")  # doctest: +DONT_ACCEPT_BLANKLINE +SKIP
    Line1
    <BLANKLINE>
    Line2
    """
    ...

def example_multiple_flags():
    """
    Multiple flags can be combined
    
    >>> import uuid
    >>> "   " + str(uuid.uuid4()) + "     "  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    '...-...-...-...-...'
    """
    ...
