import pytest
import tidyid


@pytest.mark.parametrize('x', range(1000))
def test_int_to_tid(x):
    tidyid.int_to_tid(x)
    
