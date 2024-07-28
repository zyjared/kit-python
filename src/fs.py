"""
文件相关工具

Author: Jared Zhang
Email: zyjared@outlook.com

Github: https://github.com/zyjared/kit-python
"""

from typing import Pattern
from pathlib import Path
import re


def matches_path(path: Path, match: list[Pattern]):
    """
    检查路径是否匹配
    """
    if len(match) == 0:
        return False

    path_str = str(path)
    for pattern in match:
        if pattern.match(path_str):
            return True

    return False


def rm_path(path: Path):
    """
    删除文件或目录
    """
    if path.is_dir():
        for child in path.iterdir():
            rm_path(child)
        path.rmdir()
    else:
        path.unlink()


def clean_directory_recursive(dirpath: Path, include: list[Pattern], ignore: list[Pattern] = None, removed: list[Path] = [], root: Path = None):
    """
    递归删除目录下相匹配的文件或目录

    匹配规则:
        - 匹配 include 列表中的任意一个, 不包括 ignore 列表中的任意一个
        - 如果 root 为   None, 目标字符串为文件名
        - 如果 root 不为 None, 目标字符串为相对于 root 的相对路径
    """
    for path in dirpath.iterdir():
        relpath = path.relative_to(root if root is not None else dirpath)

        if ignore is not None and matches_path(relpath, ignore):
            continue

        if matches_path(relpath, include):
            rm_path(path)
            removed.append(relpath)

        if path.is_dir():
            clean_directory_recursive(path, include, ignore, removed)

    return removed


def clean_directory(dirpath: str | Path, include: list[str], ignore: list[str] = None):
    """
    递归删除目录下相匹配的文件或目录
    """
    if isinstance(dirpath, str):
        dirpath = Path(dirpath)

    if not dirpath.is_dir():
        raise ValueError(f'{dirpath} is not a directory')

    if not include:
        raise ValueError('include list cannot be empty')

    return clean_directory_recursive(
        dirpath,
        [re.compile(p) for p in include],
        [re.compile(p) for p in ignore] if ignore else None,
        [],
        root=dirpath
    )


if __name__ == '__main__':
    import sys

    if (len(sys.argv) < 3):
        print('Usage: python clean.py <dirpath> <include> [ignore]')
        exit(1)

    dirpath = sys.argv[1]
    include = sys.argv[2].split(',')
    ignore = sys.argv[3].split(',') if len(sys.argv) > 3 else None

    removed = clean_directory(dirpath, include, ignore)

    for path in removed:
        print(f'Removed: {path}')
