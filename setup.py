from distutils.core import setup
from setuptools import setup

setup(
    name = 'yippi',
    packages = ['yippi'], # this must be the same as the name above
    version = '0.0.1b4',
    description = 'an e621 API wrapper for Python.',
    long_description = open('README.rst').read(),
    long_description_content_type='text/x-rst',
    license = 'MIT',
    author = 'Rendy Arya Kemal',
    author_email = 'rendyarya22@gmail.com',
    url = 'https://github.com/Rendyindo/yippi', # use the URL to the github repo
    classifiers = [
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords = ['yippi', 'e621', 'API'], # arbitrary keywords
    python_requires = '>=3',
)
