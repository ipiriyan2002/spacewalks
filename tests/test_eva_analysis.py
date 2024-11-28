import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_float2():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20") 
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)

    
def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result


@pytest.mark.parametrize("input_value, expected_result", [
    ("User One; User Two; User Three;", 3),
    ("User One;", 1),
])
def test_calculate_crew_size1(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical input strings
    """

    assert calculate_crew_size(input_value) == expected_result


def test_calculate_crew_size2():
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical input strings
    """

    input_value = ""

    assert calculate_crew_size(input_value) is None