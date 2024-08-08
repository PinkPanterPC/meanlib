from setuptools import setup, find_packages

setup(
    name="meanlib",
    version="1.0.0",
    author="Tobia Petrolini",
    description="A Python package for calculating simple and weighted means, featuring classes for dynamic updates and sliding window functionality.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PinkPantherPC/meanlib.git",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'meanlib = meanlib.__main__:main',
        ],
    },
    keywords=['mean', 'average', 'weighted mean', 'weighted average', 'rolling mean' 'rolling average',
              'geometric mean', 'harmonic mean', 'rolling geometric mean', 'rolling harmonic mean',
              'geometri average', 'harmonic average', 'rolling geometric average', 'rolling harmonic average']
)
