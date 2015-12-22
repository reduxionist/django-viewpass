import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='django-viewpass',
        version='1.0',
        packages=['viewpass'],
        include_package_data=True,
        license='GPL',  # example license
        description='A Django app to provide access to protected resources via URL tokens.',
        long_description=README,
        url='https://github.com/joelburton/viewpass.git',
        author='Joel Burton',
        author_email='joel@joelburton.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GPL License',  # example license
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            # Replace these appropriately if you are stuck on Python 2.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
