from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:         # Function to get requirements
    '''
    This function will return a list of requirements by reading the file paths
    '''
    requirements = []                                   # Initialize list for requirements
    with open(file_path, 'r') as file_obj:              # Open file at file_path
        requirements = file_obj.readlines()             # Read lines from file into list
                                                        # rempve /n from each line
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:                 # If hyphen-e-dot in requirements
            requirements.remove(HYPEN_E_DOT)             # Remove hyphen-e-dot
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Stavan',
author_email='stavan.sanyal@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)
