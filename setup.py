from setuptools import setup, find_packages
setup(
    name='wwwof',
    version='3.0.0',
    license='GPLv3',
    author_email='jero98772@protonmail.com',
    author='jero98772',
    description='wwwof , word wide web of fishes is a webpage with web interface for drawfishtank , divepc, calcuph,curapeces and others ',
    url='https://jero98772.pythonanywhere.com/',
    packages=find_packages(),
    install_requires=['Flask', 'tensorflow', 'numpy', 'opencv-python', 'removebg'],
    include_package_data=True,
    )
print(" _ __   ___ | |_ ___  ___ ")
print("| '_ \ / _ \| __/ _ \/ __|")
print("| | | | (_) | ||  __/\__ \ ")
print("|_| |_|\___/ \__\___||___/")
print("\n\n","PLEASE UPDATE PIP with (if needed):","\n\n","> pip intsall -U pip")
print("\n\n","SOME COMONS ERRORS of installing","\n\n","> tensorflow version == 1.14.0 \n> conda enviroment for tensorflow ")
#print("tensorflow not required in general , curapeces need tensorflow")