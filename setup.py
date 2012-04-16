try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='echo-streamserver',
    version='0.1.0',
    author='Echo',
    author_email='solutions@aboutecho.com',
    packages=['streamserver'],
    scripts=[],
    url='http://pypi.python.org/pypi/echo-streamserver/',
    license='LICENSE.txt',
    description='Echo StreamServer API library.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 0.10.8",
    ],
)