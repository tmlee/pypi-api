from setuptools import setup

setup(name='PyPi-API',
    version='0.1',
    description='Easily access PyPI package data through Python',
    url='http://github.com/tmlee/pypi-api',
    author='TM Lee',
    author_email='tmlee.ltm@gmail.com',
    license='MIT',
    packages=['pypi_api'],
    install_requires=[
        'requests',
        'json'
    ],
    zip_safe=False)