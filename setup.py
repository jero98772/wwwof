try:

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
    except:
        install_pip=str("sudo pip install -U urllib3 tensorflow opencv-python  numpy flask psycopg2 keras" )
        subprocess.run(install_pip , shell=True)
    import tensorflow
except:
    print("run to install setup you need install dependes can install automatic pip install subprocess.run  and run again python3 setup.py")