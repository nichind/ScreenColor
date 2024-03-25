from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='screencolor',
  version='1.0.0',
  author='nichind',
  author_email='nichinddev@gmail.com',
  description='Simple Python library to get average color of monitor(s)',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/nichind/ScreenColor',
  packages=find_packages(),
  install_requires=['colorthief', 'mss'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  project_urls={
    'Documentation': 'https://github.com/nichind/ScreenColor'
  },
  python_requires='>=3.7'
)