from setuptools import setup, find_packages

setup(
    name="PyCoolPlot",
    version="0.0.1",
    author="Atsushi Sakai",
    author_email="asakai.amsl@gmail.com",
    maintainer='Atsushi Sakai',
    maintainer_email='asakai.amsl@gmail.com',
    description=("A cool plotting module in Python"),
    long_description=readme,
    packages=find_packages(),
    license="MIT",
    keywords="python plot matplotlib",
    url="https://github.com/AtsushiSakai/PyCoolPlot",
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
