#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '0.0.1'

setup(name='bitshares',
      version=VERSION,
      description='Python library for bitshares',
      long_description=open('README.md').read(),
      download_url='https://github.com/xeroc/python-bitshares/tarball/' + VERSION,
      author='Fabian Schuh',
      author_email='<Fabian@BitShares.eu>',
      maintainer='Fabian Schuh',
      maintainer_email='<Fabian@BitShares.eu>',
      url='http://www.github.com/xeroc/python-bitshares',
      keywords=['bitshares', 'library', 'api', 'rpc'],
      packages=[
          "bitshares",
          "bitsharesapi",
          "bitsharesbase",
          "bitsharesdeprecated"
      ],
      classifiers=['License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Financial and Insurance Industry',
                   'Topic :: Office/Business :: Financial',
                   ],
      install_requires=["graphenelib>=0.4.6",
                        "websockets==2.0",
                        ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      include_package_data=True,
      )
