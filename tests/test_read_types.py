import pytest

from django_enhanced_settings import read_types


def test_read_str():
    assert read_types.read_str('abc') == 'abc'
    with pytest.raises(ValueError, match=r".+ str"):
        read_types.read_str(123)
    assert read_types.read_str('123') == '123'
    with pytest.raises(ValueError, match=r".+ str"):
        read_types.read_str(['123'])
    with pytest.raises(ValueError, match=r".+ str"):
        read_types.read_str(None)


def test_read_bool():
    assert read_types.read_bool(True) is True
    assert read_types.read_bool(False) is False
    assert read_types.read_bool(0) is False
    assert read_types.read_bool(1) is True
    assert read_types.read_bool('f') is False
    assert read_types.read_bool('t') is True
    with pytest.raises(ValueError, match=r".+ bool"):
        read_types.read_bool(2)
    with pytest.raises(ValueError, match=r".+ bool"):
        read_types.read_bool(-1)
    with pytest.raises(ValueError, match=r".+ bool"):
        read_types.read_bool(None)


def test_read_list():
    assert read_types.read_list(['1', '2', '3']) == ['1', '2', '3']
    assert read_types.read_list([1, 2, 3]) == [1, 2, 3]
    with pytest.raises(ValueError, match=r".+ list"):
        read_types.read_list(2)
    assert read_types.read_list([]) == []
    with pytest.raises(ValueError, match=r".+ list"):
        read_types.read_list('123')
    with pytest.raises(ValueError, match=r".+ list"):
        read_types.read_list('1;')
    with pytest.raises(ValueError, match=r".+ list"):
        read_types.read_list(';', ';')
    with pytest.raises(ValueError, match=r".+ list"):
        read_types.read_list(';1', ';')
    assert read_types.read_list('1;', ';') == ['1']
    assert read_types.read_list('1;2', ';') == ['1', '2']
    assert read_types.read_list('a;2;c', ';') == ['a', '2', 'c']
    assert read_types.read_list('1,b,3', ',') == ['1', 'b', '3']
    assert read_types.read_list(';', ',') == [';']
