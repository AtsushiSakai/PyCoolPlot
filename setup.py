from setuptools import setup, find_packages

# read README
try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    readme = open('README.md').read()

setup(
    name="PyCoolPlot",
    version="0.0.3",
    url="https://github.com/AtsushiSakai/PyCoolPlot",
    author="Atsushi Sakai",
    author_email="asakai.amsl@gmail.com",
    maintainer='Atsushi Sakai',
    maintainer_email='asakai.amsl@gmail.com',
    description=("A cool plotting module in Python"),
    long_description=readme,
    license="MIT",
    keywords="python plot matplotlib",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
    ],
)
