import pytest
import math
from calculate_grades import calculate_stat, print_stat
from io import StringIO
import sys


class TestCalculateStat:
    """Test suite for calculate_stat function."""
    
    def test_calculate_stat_normal_case(self):
        """Test with a normal list of grades."""
        grades = [85, 90, 78, 92, 88]
        mean, sd = calculate_stat(grades)
        
        assert math.isclose(mean, 86.6)
        assert math.isclose(sd, 4.9193495504995, rel_tol=1e-5)
    
    def test_calculate_stat_all_same_grades(self):
        """Test when all grades are identical (sd should be 0)."""
        grades = [80, 80, 80, 80, 80]
        mean, sd = calculate_stat(grades)
        
        assert math.isclose(mean, 80.0)
        assert math.isclose(sd, 0.0)
    
    def test_calculate_stat_two_grades(self):
        """Test with minimum reasonable input (2 grades)."""
        grades = [70, 90]
        mean, sd = calculate_stat(grades)
        
        assert math.isclose(mean, 80.0)
        assert math.isclose(sd, 10.0)
    
    def test_calculate_stat_single_grade(self):
        """Test with a single grade (sd should be 0)."""
        grades = [95]
        mean, sd = calculate_stat(grades)
        
        assert mean == 95.0
        assert sd == 0.0
    
    def test_calculate_stat_with_zero_grades(self):
        """Test that includes zero as a valid grade."""
        grades = [0, 50, 100]
        mean, sd = calculate_stat(grades)
        
        assert math.isclose(mean, 50.0)
        assert math.isclose(sd, 40.824829046386, rel_tol=1e-5)
    
    def test_calculate_stat_empty_list_raises_error(self):
        """Test that empty list raises ZeroDivisionError."""
        grades = []
        with pytest.raises(ZeroDivisionError):
            calculate_stat(grades)
    
    def test_calculate_stat_large_dataset(self):
        """Test with a larger dataset."""
        grades = [75, 80, 85, 90, 95, 100, 65, 70, 88, 92]
        mean, sd = calculate_stat(grades)
        
        assert math.isclose(mean, 84.0)
        assert math.isclose(sd, 10.954451150103, rel_tol=1e-5)


class TestPrintStat:
    """Test suite for print_stat function."""
    
    def test_print_stat_output(self):
        """Test that print_stat produces correct output format."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stat(86.6, 4.919)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        assert '****** Grade Statistics ******' in output
        assert "The grades's mean is: 86.6" in output
        assert 'The population standard deviation of grades is:  4.919' in output
        assert '****** END ******' in output
    
    def test_print_stat_rounding(self):
        """Test that standard deviation is rounded to 3 decimal places."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stat(85.5, 4.123456789)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        assert '4.123' in output
    
    def test_print_stat_zero_values(self):
        """Test printing with zero mean and sd."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stat(0.0, 0.0)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        assert 'mean is: 0.0' in output
        assert 'standard deviation of grades is:  0.0' in output