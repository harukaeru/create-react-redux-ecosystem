from setuptools import setup, find_packages

setup(
    name='create-react-redux-ecosystem',
    version='0.0.1',
    py_modules=['rrcreate_assets.create'],
    entry_points={
        "console_scripts": ['rrcreate=rrcreate_assets.create:main']
    },
    packages=['rrcreate_assets'],
    include_package_data=True
)
