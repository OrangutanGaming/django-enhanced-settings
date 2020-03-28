import pytest

from django_enhanced_settings import Settings
from django_enhanced_settings.settings import CachedConfigValue


def test_settings_cache():
    settings = Settings('')
    config = settings._config
    config._cache_value('TEST_1', 'value 1', 0)
    assert config._check_cache('TEST_1') is None
    config._cache_value('TEST_2', 'value 2', -1)
    assert config._check_cache('TEST_2') is 'value 2'
    config._cache_value('TEST_3', 'value 3', 0.1)
    assert config._check_cache('TEST_3') is 'value 3'
    config._cache['TEST_3'].cache_end = 1
    assert config._check_cache('TEST_3') is None
    with pytest.raises(ValueError):
        config._cache_value('TEST_4', 'value 4', -2)


def test_cached_config_value():
    assert CachedConfigValue('', '', 0).expired is True
    assert CachedConfigValue('', '', -1).expired is False
