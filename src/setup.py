from distutils.core import setup

setup(
    name='latex2word',
    version='1.0',
    author='Gu-f',
    packages=['src/latex2word'],
    scripts=[],
    url='https://github.com/Gu-f/LatexToWord',
    license='LICENSE',
    description='A pure python library implemented by python3 for writing Latex formulas to word.',
    long_description=open('README.md', encoding="utf-8").read(),
    install_requires=[
        "mathml2omml~=0.0.2",
        "latex2mathml~=3.77.0",
        "lxml~=5.3.0"
    ],
)