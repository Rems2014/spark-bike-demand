"""Download only the expected data files from UCI; standard library only."""
from pathlib import Path
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

URL = 'https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip'
target = Path(__file__).resolve().parents[1] / 'data/raw'
target.mkdir(parents=True, exist_ok=True)
with urlopen(URL, timeout=60) as response:
    archive = response.read()
with ZipFile(BytesIO(archive)) as z:
    for name in ('hour.csv', 'day.csv', 'Readme.txt'):
        (target / name).write_bytes(z.read(name))
print(f'Downloaded public UCI data to {target}')
