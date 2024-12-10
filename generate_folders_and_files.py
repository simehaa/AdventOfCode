import sys
from pathlib import Path

year = int(sys.argv[1])
assert year > 2014 and int(year) < 2100
year = Path(f"{year:4d}")
year.mkdir(parents=True, exist_ok=True)
for i in range(1, 26):
    day_path = year / f"{i:02d}"
    day_path.mkdir(parents=True, exist_ok=True)
    (day_path / "test.txt").touch(exist_ok=True)
