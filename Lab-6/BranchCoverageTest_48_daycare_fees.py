
import pytest

from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status,
)


# Extra hours fee: validation and age-group branches

def test_unknown_age_group():
    with pytest.raises(ValueError):
        extra_hours_fee("school", 30, False)


def test_negative_hours():
    with pytest.raises(ValueError):
        extra_hours_fee("infant", -1, False)


def test_infant_within_included_hours():
    assert extra_hours_fee("infant", 20, False) == 0


def test_toddler_within_included_hours():
    assert extra_hours_fee("toddler", 25, False) == 0


def test_preschool_within_included_hours():
    assert extra_hours_fee("preschool", 30, False) == 0


def test_infant_extra_hours():
    assert extra_hours_fee("infant", 25, False) == 70


def test_infant_more_than_twenty_extra_hours():
    assert extra_hours_fee("infant", 45, False) == 550


def test_toddler_sibling_extra_hours():
    assert extra_hours_fee("toddler", 35, True) == 45


def test_preschool_more_than_twenty_extra_hours():
    assert extra_hours_fee("preschool", 55, False) == 350


def test_infant_sibling_does_not_add_included_hours():
    assert extra_hours_fee("infant", 25, True) == 70


# Enrolment: both outcomes of each decision

def test_enrolment_pending_immunisation_old_enough():
    assert enrolment_allowed(12, 0, True) is True


def test_enrolment_pending_immunisation_too_young():
    assert enrolment_allowed(11, 5, True) is False


def test_enrolment_child_below_minimum_age():
    assert enrolment_allowed(5, 2, False) is False


def test_enrolment_child_at_minimum_age_without_vacancy():
    assert enrolment_allowed(6, 0, False) is False


def test_enrolment_child_at_minimum_age_with_vacancy():
    assert enrolment_allowed(6, 1, False) is True


# Pickup: aftercare, Friday and status branches

def test_regular_weekday_on_time():
    assert pickup_status(10, False, False) == "on_time"


def test_regular_weekday_late():
    assert pickup_status(9, False, False) == "late"


def test_regular_weekday_overdue():
    assert pickup_status(-6, False, False) == "overdue"


def test_regular_friday_on_time():
    assert pickup_status(20, False, True) == "on_time"


def test_regular_friday_late():
    assert pickup_status(10, False, True) == "late"


def test_aftercare_weekday_on_time():
    assert pickup_status(20, True, False) == "on_time"


def test_aftercare_weekday_late():
    assert pickup_status(19, True, False) == "late"


def test_aftercare_friday_overdue():
    assert pickup_status(14, True, True) == "overdue"


def test_aftercare_friday_on_time():
    assert pickup_status(30, True, True) == "on_time"


def test_aftercare_friday_late():
    assert pickup_status(15, True, True) == "late"
