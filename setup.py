from setuptools import find_packages,setup

def get_requirments(file_path):
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n', " ") for req in requirments]

        if '-e. ' in requirments:
            requirments.remove('-e. ')


setup(
    name='mlproject',
    author='jossel',
    packages=find_packages(),
    install_requires = get_requirments('requirments.txt')

)