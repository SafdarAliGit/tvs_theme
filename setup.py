from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tvs_theme/__init__.py
from tvs_theme import __version__ as version

setup(
	name="tvs_theme",
	version=version,
	description="App for TVS.",
	author="TVS",
	author_email="work.nasirkhan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
