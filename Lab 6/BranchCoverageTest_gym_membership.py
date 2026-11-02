"""Lab 6 - Branch coverage tests for gym_membership.py
Every decision is exercised for both its True and False outcome,
including boundary values."""
import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ---------- membership_cost: validation ----------
def test_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_too_young_raises():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_minimum_age_boundary_allowed():
    # age == 14 is NOT too young
    assert membership_cost("monthly", 14, False, False) == 1500


# ---------- membership_cost: age / student discounts ----------
def test_senior_discount_boundary():
    # age == 60 gets 25% off: 1500 - 375
    assert membership_cost("monthly", 60, False, False) == 1125


def test_just_below_senior_no_discount():
    assert membership_cost("monthly", 59, False, False) == 1500


def test_student_discount():
    # 1500 - 150
    assert membership_cost("monthly", 20, True, False) == 1350


def test_non_student_no_discount():
    assert membership_cost("quarterly", 20, False, False) == 4000


def test_senior_student_gets_only_senior_discount():
    # elif: senior discount wins, student discount is skipped
    assert membership_cost("monthly", 65, True, False) == 1125


# ---------- membership_cost: trainer add-on ----------
def test_trainer_monthly():
    # 1500 + 2000, no yearly rebate
    assert membership_cost("monthly", 30, False, True) == 3500


def test_trainer_yearly_rebate():
    # 12000 + 2000 - 500
    assert membership_cost("yearly", 30, False, True) == 13500


def test_yearly_without_trainer():
    assert membership_cost("yearly", 30, False, False) == 12000


def test_quarterly_student_with_trainer():
    # 4000 - 400 + 2000
    assert membership_cost("quarterly", 20, True, True) == 5600


# ---------- can_enter ----------
def test_can_enter():
    assert can_enter(10, True, False, "M") is True


def test_inactive_plan_cannot_enter():
    assert can_enter(10, False, False, "M") is False


def test_too_early():
    assert can_enter(4, True, False, "M") is False


def test_too_late():
    assert can_enter(23, True, False, "M") is False


def test_opening_hour_boundaries_allowed():
    assert can_enter(5, True, False, "M") is True
    assert can_enter(22, True, False, "M") is True


def test_women_only_slot_female_allowed():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male_denied():
    assert can_enter(10, True, True, "M") is False


# ---------- bmi_category ----------
def test_invalid_height_zero():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_invalid_height_negative():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, -1.7)


def test_bmi_underweight():
    assert bmi_category(45, 1.75) == "underweight"


def test_bmi_normal_lower_boundary():
    # BMI exactly 18.5 is normal
    assert bmi_category(18.5, 1.0) == "normal"


def test_bmi_normal():
    assert bmi_category(65, 1.75) == "normal"


def test_bmi_overweight_lower_boundary():
    # BMI exactly 25 is overweight
    assert bmi_category(25, 1.0) == "overweight"


def test_bmi_overweight():
    assert bmi_category(80, 1.75) == "overweight"


def test_bmi_obese_boundary():
    # BMI exactly 30 is obese
    assert bmi_category(30, 1.0) == "obese"


def test_bmi_obese():
    assert bmi_category(100, 1.75) == "obese"
