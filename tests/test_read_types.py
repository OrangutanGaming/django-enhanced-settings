from django_enhanced_settings import read_types


def test_read_str():
    assert read_types.read_str('abc') == 'abc'
