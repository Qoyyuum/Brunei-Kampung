from setuptools import find_packages, setup

setup(
	name='Tulus',
	version='1.0.0',
	packages=find_packages(),
	description="Tulus API built with Flask",
	include_package_data=True,
	zip_safe=False,
	author="Abdul Qoyyuum",
	install_requires=[
		'flask'
	]
)