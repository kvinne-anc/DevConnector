from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_kvinneDPST9", #the name that will be installed via pip
    version="1.0",
    author= "A.C. Kvinne"
    author_email="kvinne.anc@gmail.com", 
    description="A test package"
    long_description=long_description,
    long_description_content_type="text/markdown", # required if license is 'MIT'
    url="https://github.com/kvinne-anc/lambdata_kvinneDPST9"
    #keywords= "Lambda, draft, practice, helper, functions, prime mumbers, prime, python, basic"
    packages=find_packages() #[my_lambdata] 

)