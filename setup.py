from setuptools import setup, find_packages

setup(
    name='django-sentry',
    version='1.13.5-a',
    description='A simple fork of django-sentry for django 1.5.*'
    long_description='A simple fork of django-sentry for django 1.5.*',
    author='Josue Ttito',
    author_email='josue@inka-labs.com',
    url='http://github.com',
    license='BSD',
    packages=find_packages(exclude=('docs',)),
    include_package_data=True,
    keywords='django 1.5 sentry',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
    ],
    install_requires=[
        'Django',
    ],
)

