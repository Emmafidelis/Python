from pathlib import Path
from time import ctime
import shutil

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"
shutil.copy(source, target)
print(path.read_text())
path.write_text()
print(ctime(path.stat().st_ctime))
path.exists()
path.mkdir()
path.rmdir()
path.rename("init.txt")
path.unlink()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)

