from setuptools import setup, find_packages
import os

version = '0.6.4'

long_description = (
    open('README.rst').read()
    + '\n' +
#    'Contributors\n'
#    '============\n'
#    + '\n' +
    #open('CONTRIBUTORS.txt').read() Let's do that after somebody helped
    #+ '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.backtowork',
      version=version,
      description="A little event handler to notify you that zope is up and running",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Patrick Gerken',
      author_email='do3cc@do3.cc',
      url='http://github.com/collective/',
      license='BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.processlifetime',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
