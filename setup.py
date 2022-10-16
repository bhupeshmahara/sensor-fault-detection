from setuptools import find_packages, setup
from typing import List

# this function will return the list of requirements
def get_requirements()->List[str]:

    requirement_list:List[str] = []
    """
    write a code to read requirements.txt file and append each requirement in requirement_list
    """
    return requirement_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Bhupesh Mahara",
    author_eamil = "bhupeshmahara@gmail.com",
    packages = find_packages(),
    install_require = get_requirements() # from requirements.txt file
)
