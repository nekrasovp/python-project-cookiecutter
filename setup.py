from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.01'

setup(
    name='project', # TODO: rename. 
    version=_VERSION,
    description='An empty project base.',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"],
    url='https://github.com/..../....',  # TODO.
    download_url='https://github.com/.../.../tarball/{}'.format(_VERSION),  # TODO.
    author='Nekrasov Pavel',  # TODO.
    author_email='nekrasovp@gmail.com',  # TODO.
    packages=find_packages(include=['project*']),  # TODO.
    test_suite="testing",
    setup_requires=[],
    tests_require=[],
    include_package_data=True,
    license='TODO',  # TODO: set license string. 
    keywords='empty project TODO keywords'
)

