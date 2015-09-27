import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-datatext',
    version='0.1',
    packages=['datatext'],
    include_package_data=True,
    license='MIT License',
    description='A Django app to manage sources-texts and critical editions (mainly arabic).',
    long_description=README,
    url='http://anas.ghrab.tn/',
    author='Anas Ghrab',
    author_email='anas.ghrab@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Researchers in Digital Humanities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Digital Humanities',
    ],
)