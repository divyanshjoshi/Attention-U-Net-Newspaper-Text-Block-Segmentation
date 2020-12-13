from setuptools import setup, find_packages
from codecs import open

__version__ = '0.0.1'

# Get the long description from the README file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# Get the dependencies and installs
with open('requirements.txt', encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

# install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
# dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

install_requires = [x.strip() for x in all_reqs]

setup(
    name='citlab_python_util',
    version=__version__,
    description='Python utility functions for different kind of tasks.',
    long_description=long_description,
    url='https://github.com/CITlabRostock/citlab-python-util',
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    package_data={'citlab_python_util': ['parser/xml/page/*.xsd']},
    license='Apache License 2.0',
    author='CITlab',
    author_email='max.weidemann@uni-rostock.de, bastian.laasch@uni-rostock.de, johannes.michael@uni-rostock.de',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
