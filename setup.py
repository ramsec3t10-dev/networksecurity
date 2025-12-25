'''
The setup.py file is an essential part of packaging and distributing python projects.It is used by setuptools (or distutils in older Python versions) to define the configuration of your project, such as its metadata, dependencies, and more 
'''

from setuptools import find_packages,setup # find_packages goes and scans all the folders and the folders with __init__.py is itself considered as a package
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements

    """
    requirement_lst : List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read Lines from the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip() # to ignore empty spaces
                ##ignore empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('requirements.txt not found')
    
    return requirement_lst

print(get_requirements())  

setup(  #setting up meta data
      name = "Network_Security",
      version = "0.0.1",
      author = "Saint Ram",
      author_email = "rams.ec3t10@gct.ac.in",
      packages = find_packages(),
      install_requires = get_requirements()

)
