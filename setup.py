from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.11'
DESCRIPTION = 'Web Security Assessment Tool'

# Setting up
setup(
    name="WebSecProbe",
    version=VERSION,
    author="Spyboy",
    author_email="contact@spyboy.in",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/spyboy-productions/WebSecProbe/",
    Homepage="https://github.com/spyboy-productions/WebSecProbe/",
    Repository="https://github.com/spyboy-productions/WebSecProbe/",
    license="MIT",
    install_requires=['requests', 'tabulate'],
    keywords=['HTTP-Request-Analysis', 'bypass-403', 'Header-Injection', 'Historical-Analysis', 'Payload-Variations', 'Vulnerability-Assessment'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
    'console_scripts': [
        'WebSecProbe = WebSecProbe.main:main',
    ],
},    
)
