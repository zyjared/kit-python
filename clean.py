from pathlib import Path
from pkgs.fs.zyjared.fs import clean_directory
from pkgs.color.zyjared.color import Color

if __name__ == '__main__':
    dirpath = Path(__file__).parent
    include = [
        r'.*tempCodeRunnerFile\.py',
        r'.*__pycache__',
        r'.*egg-info',
        r'.*build'
        ]
    ignore = [r'\.git', r'env',]

    removed = clean_directory(dirpath, include, ignore)

    pkg = Color("kit-python").blue().bold()
    tool = Color("clean").yellow()
    right = Color(" → ").green().to_str()

    state = Color("success").green() if len(
        removed) != 0 else Color("no files removed").magenta()

    print(f'\n{pkg} {tool} {right} {state}')

    if len(removed) != 0:
        prefix = Color("removed").magenta().to_str() + right
        for path in removed:
            print(f'    {prefix}{path}')
