
import pytest

def test_fyll():
    glass = Glass(10)
    assert glass.innhold == 0
    glass.fyll(2)
    assert glass.innhold == 2
    glass.fyll(8)
    assert glass.innhold == 10
    glass.fyll(2)
    assert glass.innhold == 10
    glass.fyll(-2)
    assert glass.innhold == 8
    
def test_tøm():
    glass = Glass(10)
    glass.fyll(10)
    flass.tøm(2)
    assert glass.innhold == 8
    
