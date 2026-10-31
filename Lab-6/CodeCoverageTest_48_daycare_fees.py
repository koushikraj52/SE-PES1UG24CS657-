
import pytest

from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status,
)


# Extra hours fee tests

def test_within_included_hours():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_unknown_age_group():
    with pytest.raises(ValueError):
        extra_hours_fee("school", 30, False)


def test_negative_hours():
    with pytest.raises(ValueError):
        extra_hours_fee("infant", -1, False)


def test_infant_extra_hours():
    assert extra_hours_fee("infant", 25, False) == 70


def test_infant_high_extra_hours():
    assert extra_hours_fee("infant", 45, False) == 550


def test_toddler_sibling_discount():
    assert extra_hours_fee("toddler", 35, True) == 45


def test_preschool_high_extra_hours():
    assert extra_hours_fee("preschool", 55, False) == 350


# Enrolment tests

def test_enrolment_allowed():
    assert enrolment_allowed(24, 2, False) is True


def test_immunisation_pending_and_old_enough():
    assert enrolment_allowed(12, 0, True) is True


def test_immunisation_pending_and_too_young():
    assert enrolment_allowed(10, 2, True) is False


def test_child_too_young():
    assert enrolment_allowed(5, 2, False) is False


def test_no_vacancies():
    assert enrolment_allowed(24, 0, False) is False


# Pickup status tests

def test_pickup_on_time():
    assert pickup_status(25, False, False) == "on_time"


def test_pickup_late():
    assert pickup_status(5, False, False) == "late"


def test_pickup_overdue():
    assert pickup_status(-6, False, False) == "overdue"


def test_aftercare_friday_on_time():
    assert pickup_status(30, True, True) == "on_time"


def test_aftercare_friday_late():
    assert pickup_status(20, True, True) == "late"


def test_aftercare_friday_overdue():
    assert pickup_status(5, True, True) == "overdue"
