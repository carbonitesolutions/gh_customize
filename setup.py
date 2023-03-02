from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gh_customize/__init__.py
from gh_customize import __version__ as version

setup(
	name="gh_customize",
	version=version,
	description="Customized reports and configurations",
	author="Carbonite Solutions Limited",
	author_email="admin@carbonitesolutions.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
