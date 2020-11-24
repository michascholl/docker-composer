from pathlib import Path
from subprocess import run

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.mark.parametrize("dir", ("src", "tests"))
def test_black(dir_name: str, request: FixtureRequest):
    # adjust base_dir if test file is moved.
    base_dir = Path(request.fspath.dirname).parent
    proc = run(("black", "--check", base_dir / dir_name))
    assert proc.returncode == 0, ("black is not happy with", dir_name)
