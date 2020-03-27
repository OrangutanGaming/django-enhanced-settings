import time

from django_enhanced_settings import Settings


def test_cache():
    settings = Settings('')
    config = settings._config
    config._cache_value('TEST_1', 'value 1', 0)
    assert config._check_cache('TEST_1') is None
    config._cache_value('TEST_2', 'value 2', -1)
    assert config._check_cache('TEST_2') is 'value 2'
    config._cache_value('TEST_3', 'value 3', 0.1)
    assert config._check_cache('TEST_3') is 'value 3'
    time.sleep(0.1)
    assert config._check_cache('TEST_3') is None
