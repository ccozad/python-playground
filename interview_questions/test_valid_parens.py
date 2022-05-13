import time
from valid_parens import is_valid_parens

def test_balanced():
    s1 = '[](){}'
    s2 = '[({})]'
    s3 = '[[]](({{}}))'

    assert is_valid_parens(s1)
    assert is_valid_parens(s2)
    assert is_valid_parens(s3)

def test_closing_no_opening():
    s1 = '[]()}'
    s2 = '[{})]'
    s3 = '[]](({{}}))'

    assert not is_valid_parens(s1)
    assert not is_valid_parens(s2)
    assert not is_valid_parens(s3)

def test_wrong_closing():
    s1 = '(][)[}'
    s2 = '[({]})'
    s3 = '[[}](({{}}))'

    assert not is_valid_parens(s1)
    assert not is_valid_parens(s2)
    assert not is_valid_parens(s3)

def test_opening_no_closing():
    s1 = '[({'
    s2 = '[({'
    s3 = '[[(({{'

    assert not is_valid_parens(s1)
    assert not is_valid_parens(s2)
    assert not is_valid_parens(s3)