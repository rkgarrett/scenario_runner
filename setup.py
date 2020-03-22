import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='srunner',
     version='0.9.8',
     scripts=['scenario_runner.py', 'manual_control.py'],
     author="Carla Team",
     author_email="carla.simulator@gmail.com",
     description="The package in order to use scenarios for CARLA",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/rkgarrett/scenario_runner",
     packages=setuptools.find_packages(),
     install_requires=[
        'xmlschema==1.0.18',
        'py_trees==0.8.3',
        'numpy>=1.16',
        'networkx==2.2',
        'Shapely',
        'psutil'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 ) 
