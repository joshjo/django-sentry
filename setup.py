from setuptools import setup, find_packages

setup(
    name='django-sentry',
    version='1.13.5-a',
    description='A simple fork of django-sentry for django 1.5.*',
    long_description='A simple fork of django-sentry for django 1.5.*',
    author='Josue Ttito',
    author_email='josue@inka-labs.com',
    url='https://github.com/joshjo/django-sentry',
    license='BSD',
#    packages=find_packages(exclude=('docs',)),
    include_package_data=True,
    keywords='django 1.5 sentry',
    classifiers=[
    ],
    install_requires=[
        'Django',
    ],
)

