from app.main import get_human_age


def test_if_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_exactly_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_at_second_year_boundaries() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_pets_have_different_conversion_rates() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_large_values_of_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
