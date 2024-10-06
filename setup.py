from setuptools import setup, find_packages

setup(
    name='startercli',
    version='0.1',
    py_modules=['startercli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        new-site=startercli:setup_new_site
    ''',
)
