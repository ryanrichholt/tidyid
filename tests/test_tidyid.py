import pytest
import tidyid


def test_int_to_tid_0():
    with pytest.raises(TypeError):
        tidyid.int_to_tid(0)


@pytest.mark.parametrize('x', range(1, 1000))
def test_int_to_tid(x):
    tidyid.int_to_tid(x)
    
