# fs

## Usage

```sh
pip install setuptools
pip install "git+https://github.com/zyjared/kit-python.git#egg=zyjared-fs&subdirectory=pkgs/fs"
```

```python
from fs import matches_path, rm_path, clean_directory
from pathlib import Path

rm_path(Path('test'))

is_matched: bool = matches_path(Path('test'), [r'.*test\.py'])

removed: list[Path] = clean_directory('test', include=[r'.*test\.py'], ignore=[r'\.git'])
```

## Author

Author: Jared Zhang
Email: zyjared@outlook.com

Github: https://github.com/zyjared/kit-python
