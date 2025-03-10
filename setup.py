from setuptools import setup, find_packages

setup(
    name='django-searchable-list-filter',
    version='0.1.0',
    description='Django admin filter with search for list_filter',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Radis',
    author_email='radis.ramisovich@gmail.com',
    url='https://github.com/tuhbiev/django-searchable-list-filter',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
