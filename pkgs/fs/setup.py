import os
from setuptools import setup, find_namespace_packages

_PY_VERSION = '3.11'


setup(
    name='zyjared-fs',
    version='0.1.1',
    packages=find_namespace_packages(include=['zyjared_fs', 'zyjared_fs.*']),
    install_requires=[],
    author='Jared Zhang',
    author_email='zyjared@outlook.com',
    description='simple tools for file or path',
    long_description=open('README.md').read(
    ) if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/zyjared/kit-python',
    classifiers=[
        f'Programming Language :: Python :: {_PY_VERSION}',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=f'>={_PY_VERSION}',
)
