# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
    name='buca',
    version='0.0.2',
    author='Baptiste Fontaine',
    author_email='b@ptistefontaine.fr',
    py_modules=['buca'],
    url='https://github.com/bfontaine/buca',
    license='MIT License',
    description='Blank random words in a text',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts':[
            'buca = buca:main'
        ]
    },
)
