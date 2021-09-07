from os import path
from setuptools import setup, find_packages

curdir = path.abspath(path.dirname(__file__))
with open(path.join(curdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

name = 'blmarkdown'
version = '1.0'
description = 'Bear Au Jus Learning Markdown (blmarkdown) is a tool used to help you documenting your learning history in rich and flavored markdown.'
url = 'https://github.com/bearaujus/blmarkdown'
author = 'Bear Au Jus - ジュースとくま'
author_email = 'haryobagasasyafah6@gmail.com'

list_classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Natural Language :: English',
    'Topic :: Utilities',
]

list_install_requirements = [
    'markdown',
    'datetime'
]

list_keywords = [
    'blmarkdown',
    'bearaujus learning markdown',
    'bearaujus markdown',
    'bearaujus learning',
    'bearaujus',
    'learning',
    'markdown',
    'github learning history documentation using python',
    'python',
    'markdown generator',
    'github',
    'documenting learning history'
]

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=url,
    author=author,
    author_email=author_email,
    license='MIT',
    classifiers=list_classifiers,
    keywords=list_keywords,
    packages=find_packages(),
    install_requires=list_install_requirements
)
