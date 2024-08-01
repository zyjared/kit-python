from pathlib import Path
from pkgs.color.zyjared_color.core.constant import _COLORS
from pkgs.fs.zyjared_fs import clean_directory
from pkgs.color.zyjared_color import Color
from time import time


def funcname(func, name):
    if func.__name__ == '<lambda>':
        return name

    return func.__name__


def test_color():

    types = ['bold', 'italic', 'underline', 'bg', 'dim',
             'blink', 'blink_fast', 'hidden', 'reverse']
    for t in types:
        cato = Color(t).red().bold()
        print(f'{cato:<20}')
        for color in _COLORS:
            text = getattr(Color('Hello World!'), color)()
            if t == 'bg':
                text = getattr(text, f'bg_{color}')()
            else:
                text = getattr(text, t)()

            c = str(Color(color).green())
            print(f'\t{c:<30} : {text}')


def test_clean():
    files = ['1.py', '2.py']

    if not Path('test').exists():
        Path('test').mkdir()

    for file in files:
        filepath = Path('test', file)
        filepath.touch()
        print(f'Created {Color.green(filepath)}')

    dirpath = Path(__file__).parent
    include = [
        r'.*tempCodeRunnerFile\.py',
        r'.*__pycache__',
        r'.*egg-info',
        r'.*build',
        r'.*dist',
        r'.*\\out',
        r'.*test\\.*\.py',
    ]
    ignore = [r'\.git', r'env',]

    removed = clean_directory(dirpath, include, ignore)

    pkg = Color.blue("kit-python").bold()
    tool = Color.yellow("clean").yellow()
    right = Color.green(" → ")

    state = Color.green("success") if len(
        removed) != 0 else Color.magenta("no files removed")

    print(f'\n{pkg} {tool} {right} {state}')

    if len(removed) != 0:
        prefix = Color.magenta("removed") + right
        for path in removed:
            print(f'    {prefix}{path}')


def test_bytes(count):
    style = bytearray([31, 32, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ba = bytearray()
    for i in range(count):
        ba.extend(style)
        ba.extend('Hello World!'.encode())

    res = ba.decode()
    return res


def test_str(count):
    style = {
        'fg': 31,
        'bg': 32,
        'bold': 1,
        'dim': 2,
        'italic': 3,
        'underline': 4,
        'blink': 5,
        'blink_fast': 6,
        'reverse': 7,
        'hidden': 8,
    }
    s = ''
    for i in range(count):
        vs = [f'{v}' for v in style.values()]
        vs.append('Hello World!')
        s = ''.join(vs)

    res = s
    return res


def perfomance_test(func1, func2, count=100):
    dic = {}

    time_start = time()

    for i in range(count):
        func1()

    time_end = time()

    dic[funcname(func1, 'func1')] = time_end - time_start

    time_start = time()

    for i in range(count):
        func2()

    time_end = time()

    dic[funcname(func2, 'func2')] = time_end - time_start

    return dic


def test_perfomance():
    for i in range(100):
        res = perfomance_test(
            lambda: test_str(1),
            lambda: test_bytes(2),
            1000
        )

        fun1_msg = Color(f'{round(res['func1'] * 1000, 3)}ms')
        fun2_msg = Color(f'{round(res['func2'] * 1000, 3)}ms')

        if res['func1'] > res['func2']:
            fun1_msg.red()
            fun2_msg.green()
        elif res['func1'] < res['func2']:
            fun1_msg.green()
            fun2_msg.red()
        else:
            fun1_msg.cyan()
            fun2_msg.cyan()

        print(f'{i:>3} -> str: {fun1_msg:>20} | bytes: {fun2_msg:>20}')


if __name__ == '__main__':
    test_color()
    # test_clean()
    # test_perfomance()
    # print(Color.red('Hello World!'))
