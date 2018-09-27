import os
import runpy
from setuptools import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))
about = runpy.run_path(os.path.join(base_dir, 'geomstats', '__about__.py'))

setup(name='geomstats',
      version=about['__version__'],
      install_requires=about['install_requires'],
      extras_require=about['extras_require'],
      description='Geometric statistics on manifolds',
      url='XXX',
      author='XXX',
      author_email='XXX',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
