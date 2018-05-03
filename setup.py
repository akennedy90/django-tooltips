#!/usr/bin/env python
from setuptools import setup

try:
    description = open("README.rst").read()
except IOError:
    description = ''

setup(
    name='django-tooltips',
    version='1.1.6',
    description='Django manageable Bootstrap Tooltips',
    long_description=description,
    author='Sander van de Graaf',
    author_email='mail@svdgraaf.nl',
    maintainer='Aaron Kennedy',
    maintainer_email='kennedy@postpro.net',
    url='https://github.com/akennedy90/django-tooltips',
    packages=['tooltips', 'tooltips.migrations'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
    ],
    zip_safe=False,
)