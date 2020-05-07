from setuptools import setup
import os

setup(
    name = 'clow',
    packages = ['clow'],
    version = '0.5',
    license = 'MIT',
    description = 'Clow Language',
    author = 'Yuri Rapoport',
    author_email = 'yuri.rapoport@gmail.com',
    url = 'https://github.com/yrapop01/clow',
    download_url = 'https://github.com/yrapop01/clow/archive/v_05.tar.gz',
    keywords = ['STATIC', 'TYPES', 'TYPING', 'INFERENCE'],
    install_requires = ['typehint'],
    classifiers = [
      'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
      'Intended Audience :: Developers', 
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
    ]
)
