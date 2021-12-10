from setuptools import setup, find_packages

setup(
    name='BomberKillers',
    version='0.0.1',
    author="Sun Yilong",
    author_email='sunjerry@yahoo.com',
    packages=find_packages('source'),
    package_dir={'': 'source'},
	py_modules=["main","object","settings","yonghu","yonghu2"],
    url='https://github.com/Tang634724712/BomberKillers',
    keywords='python game',
    install_requires=[
          'pygame',
      ],

)