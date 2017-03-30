from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

libs = [s.replace('-l', '') for s in "-lavfilter -lavformat -lavcodec -lswresample -lswscale -lavutil -ldl -ldl  -lm -llzma -lz -lm".split()]

#libs = [s.replace('-l', '') for s in "-lavfilter -lavformat -lavcodec -lswresample -lswscale -lavutil -ldl -ldl  -lm -llzma -lz -lswresample-ffmpeg -lm -lavutil-ffmpeg".split()]


ext = Extension('muxing_py', [
    'muxing.c',
    'muxing_py.pyx'
], libraries=libs, include_path=[numpy.get_include()])

setup(ext_modules=cythonize([ext]))






#soursefiles = ['muxing_g.so', 'muxing_py.pyx']

#extensions = [Extension('muxing_py', soursefiles, libraries=libs)]

#setup(ext_modules = cythonize(extensions))
