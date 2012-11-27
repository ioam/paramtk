#!/usr/bin/env python

import sys
from distutils.core import setup


setup_args = {}

#############################################################################################
##### CEBALERT: copied from topographica; should be simplified

required = {'param':">=0.0.1",
            'PIL':">=1.1.6"}

packages_to_install = [required]
packages_to_state = [required]

setup_args = {}

if 'setuptools' in sys.modules:
    # support easy_install without depending on setuptools
    install_requires = []
    for package_list in packages_to_install:
        install_requires+=["%s%s"%(package,version) for package,version in package_list.items()]
    setup_args['install_requires']=install_requires
    setup_args['dependency_links']=["http://pypi.python.org/simple/"]
    setup_args['zip_safe']=False # CEBALERT: haven't checked for paramtk

for package_list in packages_to_state:
    requires = []
    requires+=["%s (%s)"%(package,version) for package,version in package_list.items()]
    setup_args['requires']=requires

#############################################################################################


setup_args.update(dict(
    name='paramtk',
    version='0.8',
    description='Optional Tkinter interface for Param',
    long_description=open('README.rst').read(),
    author= "IOAM",
    author_email= "developers@topographica.org",
    maintainer= "IOAM",
    maintainer_email= "developers@topographica.org",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='http://ioam.github.com/paramtk/',
    packages = ["paramtk"],

    package_data={
        # CB: These things are not data, but there's currently no
        # other mechanism in distutils/setuptools.
        'paramtk': ['tcl/snit-2.2.1/*.tcl',
                    'tcl/scrodget-2.1/*.tcl',
                    'tcl/tooltip-1.4/*.tcl'],
        },


    classifiers = [
        "License :: OSI Approved :: BSD License",
# (until packaging tested)
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
))


if __name__=="__main__":
    setup(**setup_args)
