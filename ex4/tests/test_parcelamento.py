import pytest
from parcelamento import parcela

def test_parcelamento():
    assert parcela(100.0, 1) == 100.0
    assert parcela(100.0, 3) == 33.33
    assert parcela(100.0, 4) == 25.5
    assert parcela(100.0, 12) == 9.83
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100.0, 0)
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100.0, 13)