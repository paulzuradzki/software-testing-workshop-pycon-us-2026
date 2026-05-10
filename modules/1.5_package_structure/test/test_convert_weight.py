from converter.convert_weight import convert_lb_to_kg                                                
import pytest

def test_convert_lb_to_kg():
    # Arrange
    expected = 1
    # Act
    result = convert_lb_to_kg(2.2)
    # Assert
    assert result == pytest.approx(expected)