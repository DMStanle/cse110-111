import pytest

from fit import calculate_bmr, get_daily_calories, read_file, celebrities



def test_calculate_bmr():
    assert calculate_bmr('M', 160, 72, 24) == 1935
    assert calculate_bmr('F', 120, 68, 21 ) == 1359

def test_get_daily_calories():
    assert get_daily_calories(1754.4, 'GAIN', 1) == 2712.3
    assert get_daily_calories(1359, 'LOSE', 2) == 1568.625




pytest.main(["-v", "--tb=line", "-rN", __file__])