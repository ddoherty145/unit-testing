import pytest
from extract_position import extract_position


class TestExtractPosition:
    """Test suite for extract_position function."""
    
    def test_extract_position_with_valid_position(self):
        """Test extracting position from valid update message."""
        line = '|update| the positron location in the particle accelerator is x:21.432'
        result = extract_position(line)
        assert result == '21.432'
    
    def test_extract_position_with_error_message(self):
        """Test that error messages return None."""
        line = '|error| numerical calculations could not converge.'
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_with_debug_message(self):
        """Test that debug messages return None."""
        line = '|debug| checking particle trajectory'
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_with_empty_string(self):
        """Test that empty string returns None."""
        line = ''
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_without_x_marker(self):
        """Test line without 'x:' marker returns None."""
        line = '|update| general status message'
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_with_integer_coordinate(self):
        """Test extracting integer position."""
        line = '|info| particle at x:42'
        result = extract_position(line)
        assert result == '42'
    
    def test_extract_position_with_negative_coordinate(self):
        """Test extracting negative position."""
        line = '|update| position x:-15.5'
        result = extract_position(line)
        assert result == '-15.5'
    
    def test_extract_position_with_multiple_colons(self):
        """Test line with multiple colons."""
        line = '|update| time:12:34 position x:100.5'
        result = extract_position(line)
        assert result == '100.5'
    
    def test_extract_position_debug_in_middle(self):
        """Test that 'debug' anywhere in line triggers None."""
        line = 'particle debugger position x:50'
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_error_in_middle(self):
        """Test that 'error' anywhere in line triggers None."""
        line = 'error-free measurement x:30.5'
        result = extract_position(line)
        assert result is None
    
    def test_extract_position_with_whitespace_after_x(self):
        """Test position extraction with various whitespace."""
        line = '|update| location x:  100.25 meters'
        result = extract_position(line)
        assert result == '  100.25 meters'
    
    def test_extract_position_x_at_end(self):
        """Test when x: is at the very end."""
        line = 'measurement x:'
        result = extract_position(line)
        assert result == ''
    
    def test_extract_position_case_sensitive_debug(self):
        """Test that 'DEBUG' (uppercase) doesn't trigger None (case-sensitive)."""
        line = '|UPDATE| DEBUG MODE OFF x:123'
        result = extract_position(line)
        # Current implementation is case-sensitive, so this should extract
        assert result == '123'
    
    def test_extract_position_with_scientific_notation(self):
        """Test extracting position in scientific notation."""
        line = '|update| precise position x:1.23e-5'
        result = extract_position(line)
        assert result == '1.23e-5'
    
    def test_extract_position_none_input(self):
        """Test that None input is handled (will raise TypeError in current implementation)."""
        # This will actually fail with current implementation
        # showing a bug that should be fixed
        with pytest.raises(TypeError):
            extract_position(None)

