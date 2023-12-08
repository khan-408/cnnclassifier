import setuptools


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.1'
REPO_NAME = 'cnnclassifier'
AUTHOR_NAME = 'khan-408'
AUTHOR_EMAIL = 'aqleemkhan408@gmail.com'
SRC_REPO = 'cnnclassifier'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description= 'This is a Convulational Nerual Network based Classifier.',
    long_description= long_description,
    long_description_content_type = 'text/markdown',
    url = f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls = {
        'bug_tracker': f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)
