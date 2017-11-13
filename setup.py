from setuptools import setup


setup(name='Luibeal',
      version='0.0',
      description='Recurrent NN based decline curve framework to learn events',
      author='Philipp S. Lang',
      author_email='plang@slb.com',
      download_url='https://github.com/plang85/decline_curves_2pointOooh.git',
      install_requires=[], # environment.yml
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Engineers',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=['luibeal'])