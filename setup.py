from distutils.core import setup

setup(
    name='Maze',
    version='0.1.0',
    author='John Lenz',
    author_email='lenz@math.uic.edu',
    packages=['maze'],
    url='http://www.math.uic.edu/~lenz/s13.m275',
    description='Maze storage, generation, and solving code',
    install_requires=[
        "numpy",
    ],
)
