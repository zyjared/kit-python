from pathlib import Path
# from pkgs.color.zyjared_color.constant import COLORS
from pkgs.fs.zyjared_fs import clean_directory
from pkgs.color.zyjared_color.color import Color

if __name__ == '__main__':

    a = Color.red('Hello World!')
    print(a)

    b = Color.bold('Hello World!').italic().underline().bg_blue()
    print(b)

    c = Color.red('Hello') + ' ' + Color.blue('World') + '!!!'
    print(c)

    d = Color('extend styles').extend(a)
    print(d)

    e = b.clean().red()
    print(e)

    types = ['bold', 'italic', 'underline', 'bg', 'dim',
             'blink', 'blink_fast', 'hidden', 'reverse']
    # for t in types:
    #     cato = Style(t).red().bold()
    #     print(f'{cato:<20}')
    #     for color in COLORS:
    #         text = getattr(Style('Hello World!'), color)()
    #         if t == 'bg':
    #             text = getattr(text, f'bg_{color}')()
    #         else:
    #             text = getattr(text, t)()

    #         c = str(Style(color).green())
    #         print(f'\t{c:<30} : {text}')
    files = ['1.py', '2.py']

    if not Path('test').exists():
        Path('test').mkdir()

    for file in files:
        filepath = Path('test', file)
        filepath.touch()
        print(f'Created {Color.green(filepath)}')

    # clean
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
