import pytest
from password_checker import main

def test_branch_2():
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1