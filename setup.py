try:
#dont working
    import subprocess
    try:
        import time
        import psycopg2, psycopg2.extras
        from flask_sqlalchemy import SQLAlchemy
        from flask import Flask, render_template, request, flash, redirect 
        import urllib.request
        import numpy as np
        import tensorflow as tf
        import cv2
        import os
        from tensorflow.python.keras import backend as K
        import tensorflow
    except:
        install_pip=str("sudo pip install -U urllib3 tensorflow opencv-python  numpy Flask psycopg2 keras flask_sqlalchemy" )
        subprocess.run(install_pip , shell=True)
except:
    print("run to install setup you need install dependes can install automatic pip install subprocess.run  and run again python3 setup.py")
"""


from setuptools import setup, find_packages

setup(
    name='wwwof',
    version='1.3',
    license='GPLv3',
    author_email='jero98772@protonmail.com',
    author='jero98772',
    description='proyects about fish',
    url='http://127.0.0.1:5000/',
    packages=find_packages(),
    install_requires=['urllib3 == 1.25.7', 'tensorflow == 2.0.0', 'opencv-python==4.1.2 ', 'numpy==1.18.0', 'Flask==1.1.1', 'psycopg2==2.8.4' ,'keras==2.3.1,' 'flask_sqlalchemy==2.4.1','subprocess.run==17.1.1'],
    include_package_data=True,
      zip_safe=False
)
"""