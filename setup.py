from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in concesiones/__init__.py
from concesiones import __version__ as version

setup(
	name='concesiones',
	version=version,
	description='Referente a concesiones',
	author='Marco Bohorquez',
	author_email='antoniob@overskull.pe',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
