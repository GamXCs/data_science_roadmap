import pathlib
import urllib.request

# program to retrieve the Titanic dataset using pathlib and urllib.request

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dest = pathlib.Path("data/raw/titanic.csv")
dest.parent.mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(url, dest)
print(f"Saved to {dest}  ({dest.stat().st_size:,} bytes)")
