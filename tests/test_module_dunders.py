from copy import copy

import pytest

from django_enhanced_settings.settings import ConfigValue, Settings

global_vars = {'TEST_1': ConfigValue(None, lambda s: s, str, {}, {
    'key': 'TEST_1',
    'default': None,
    'required': False,
    'cache_ttl': -1,
})}


def test_prefix():
    prefix_global_vars = copy(global_vars)
    settings = Settings('', suffix_underscore=False)
    settings._config._cache_value('TEST_1', 'value 1', -1)
    prefix_global_vars = {f'_{k}': prefix_global_vars[k] for k in prefix_global_vars}
    for k in prefix_global_vars:
        prefix_global_vars[k]._config = settings._config
    dir_prefix = settings.dir(prefix_global_vars)
    assert dir_prefix == ['TEST_1']
    assert settings.getattr(prefix_global_vars, 'TEST_1') == 'value 1'
    with pytest.raises(AttributeError):
        settings.getattr(prefix_global_vars, '_TEST_1')


def test_suffix():
    suffix_global_vars = copy(global_vars)
    settings = Settings('', suffix_underscore=True)
    settings._config._cache_value('TEST_1', 'value 1', -1)
    suffix_global_vars = {f'{k}_': suffix_global_vars[k] for k in suffix_global_vars}
    for k in suffix_global_vars:
        suffix_global_vars[k]._config = settings._config
    dir_prefix = settings.dir(suffix_global_vars)
    assert dir_prefix == ['TEST_1']
    assert settings.getattr(suffix_global_vars, 'TEST_1') == 'value 1'
    with pytest.raises(AttributeError):
        settings.getattr(suffix_global_vars, 'TEST_1_')
