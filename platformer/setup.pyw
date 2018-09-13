#!python27
import pygame as pg
import random
from settings import *
from sprites import *
from main import *
from  distutils.core import setup
import py2exe



setup(console=['main.py, sprites.py, settings.py'])