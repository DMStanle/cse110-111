from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Drew','Stanley') == 'Stanley; Drew'
    assert make_full_name('Stephen', 'Meiling') == 'Meiling; Stephen'
    assert make_full_name('Joshua', 'Howard') == 'Howard; Joshua'

def test_extract_family_name():
    assert extract_family_name('Stanley; Drew') == 'Stanley'
    assert extract_family_name('Meiling; Stephen') == 'Meiling'
    assert extract_family_name('Howard; Joshua') == 'Howard'

def test_extract_given_name():
    assert extract_given_name('Stanley; Drew') == 'Drew'
    assert extract_given_name('Meiling; Stephen') == 'Stephen'
    assert extract_given_name('Howard; Joshua') == 'Joshua'

pytest.main(['-v', '--tb=line', '-rN', __file__])