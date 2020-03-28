from copy import copy

import pytest

from django_enhanced_settings.settings import ConfigValue, Settings

global_vars = {
    'TEST_1': ConfigValue(None, lambda s: s, str, {}, {
        'key': 'TEST_1',
        'default': None,
        'required': False,
        'cache_ttl': -1,
    }),
    'TEST_2': 'test value 2',
    '__name__': 'test name',
    'random_var': 'test random value',
}


def test_prefix():
    prefix_global_vars = copy(global_vars)
    settings = Settings('', suffix_underscore=False)
    settings._config._cache_value('TEST_1', 'value 1', -1)

    prefix_global_vars = copy(global_vars)

    with pytest.raises(ValueError):
        settings.dir(prefix_global_vars)

    prefix_global_vars['_TEST_1'] = copy(global_vars['TEST_1'])
    del prefix_global_vars['TEST_1']
    prefix_global_vars['_TEST_1']._config = settings._config
    prefix_global_vars['_TEST_2'] = copy(global_vars['TEST_2'])
    del prefix_global_vars['TEST_2']

    with pytest.raises(ValueError):
        settings.dir(prefix_global_vars)

    prefix_global_vars['TEST_2'] = copy(global_vars['TEST_2'])
    del prefix_global_vars['_TEST_2']
    prefix_global_vars['TEST_1'] = 'test value 1 1'

    with pytest.raises(ValueError):
        settings.dir(prefix_global_vars)

    del prefix_global_vars['TEST_1']

    dir_prefix = settings.dir(prefix_global_vars)
    assert set(dir_prefix) == {'TEST_1', 'TEST_2'}
    assert settings.getattr('TEST_1', prefix_global_vars) == 'value 1'
    with pytest.raises(AttributeError):
        settings.getattr(prefix_global_vars, '_TEST_1')


def test_suffix():
    suffix_global_vars = copy(global_vars)
    settings = Settings('', suffix_underscore=True)
    settings._config._cache_value('TEST_1', 'value 1', -1)

    suffix_global_vars = copy(global_vars)

    with pytest.raises(ValueError):
        settings.dir(suffix_global_vars)

    suffix_global_vars['TEST_1_'] = copy(global_vars['TEST_1'])
    del suffix_global_vars['TEST_1']
    suffix_global_vars['TEST_1_']._config = settings._config
    suffix_global_vars['TEST_2_'] = copy(global_vars['TEST_2'])
    del suffix_global_vars['TEST_2']

    with pytest.raises(ValueError):
        settings.dir(suffix_global_vars)

    suffix_global_vars['TEST_2'] = copy(global_vars['TEST_2'])
    del suffix_global_vars['TEST_2_']
    suffix_global_vars['TEST_1'] = 'test value 1 1'

    with pytest.raises(ValueError):
        settings.dir(suffix_global_vars)

    del suffix_global_vars['TEST_1']

    dir_prefix = settings.dir(suffix_global_vars)
    assert set(dir_prefix) == {'TEST_1', 'TEST_2'}
    assert settings.getattr('TEST_1', suffix_global_vars) == 'value 1'
    with pytest.raises(AttributeError):
        settings.getattr(suffix_global_vars, '_TEST_1')
