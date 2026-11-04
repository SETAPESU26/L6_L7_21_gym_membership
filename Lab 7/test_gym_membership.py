from hypothesis import given, strategies as st
from gym_membership import parse_plan, calculate_bmi, average_workout

@given(st.text() | st.none())
def test_parse_plan_no_crash(s):

@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):

@given(st.text() | st.none())
def test_average_workout_no_crash(s):
