#!/usr/bin/env python
from setuptools import setup, find_packages


def install():
    required = []
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        for req in requirements:
            p = req.split('==')
            required.append(p[0])
    desc = ''
    setup(
        name='navertrans',
        version='0.1',
        description=desc,
        long_description=desc,
        author='Seongrok Kim',
        author_email='max_sungrok@naver.com',
        url='https://github.com/LearningnRunning/k_translator',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Education',
            'Intended Audience :: End Users/Desktop',
            'License :: Freeware',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Topic :: Education',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
        ],
        packages=find_packages(),
        install_requires=required,
    )


if __name__ == "__main__":
    install()
