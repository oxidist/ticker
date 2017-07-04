try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Abdul Aleem',
    'url': 'https://github.com/OfficialOxide/',
    'download_url': 'Where to download it.',
    'author_email': 'developer.abdulaleem@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ticker'],
    'scripts': [],
    'name': 'name'
}

setup(**config)
