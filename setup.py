from setuptools import setup, find_packages
from pip._internal.req.req_file import parse_requirements
# from pip._internal.download import PipSession see https://github.com/blackducksoftware/synopsys-detect/pull/107
import locking

from os import path


class PipSession: {}

# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
dependency_links = []

# Inject requirements from requirements.txt into setup.py
requirements_file = parse_requirements(path.join('requirements', 'requirements.txt'), session=PipSession())
try:
    install_requires = [str(rf.req) for rf in requirements_file]
except:
    install_requires = [str(rf.requirement) for rf in requirements_file]

dependency_links = [str(rf.link) for rf in requirements_file if rf.link]

# Inject test requirements from requirements_test.txt into setup.py
requirements_test_file = parse_requirements(path.join('requirements', 'requirements_test.txt'), session=PipSession())
try:
    tests_require = [str(rf.req) for rf in requirements_test_file]
except:
    tests_require = [str(rf.requirement) for rf in requirements_test_file]

dependency_links += [str(rf.link) for rf in requirements_file if rf.link]


setup(
    name="django-db-locking",
    version=locking.__version__,
    url='https://github.com/vikingco/django-db-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo',
    author_email='operations@unleashed.be',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={'celery':  ["celery"] },
    tests_require=tests_require,
    dependency_links=dependency_links,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
