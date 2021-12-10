from setuptools import setup, find_packages

setup(
    name='BomberKillers',
    version='0.0.3',
    author="Sun Yilong,Tang Shaozhe,Li Zhipeng,Ramzan Muhammad",
    author_email='bcfogs@inf.elte.hu,qs4oz8@inf.elte.hu,g31r6t@inf.elte.hu,pn8uom@inf.elte.hu',
    packages=find_packages('source'),
    package_dir={'': 'source'},
	py_modules=["main","object","settings","yonghu","yonghu2"],
    url='https://github.com/Tang634724712/BomberKillers',
    keywords='python game',
    install_requires=[
          'pygame',
      ],

)
