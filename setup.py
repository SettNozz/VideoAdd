from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

libs = [s.replace('-l', '') for s in "-lavfilter -lavformat -lavcodec -lswresample -lswscale -lavutil -ldl -ldl  -lm -llzma -lz -lswresample-ffmpeg -lm -lavutil-ffmpeg".split()]

soursefiles = ['muxing_g.so', 'muxing_py.pyx']

extensions = [Extension('muxing_py', soursefiles, libraries=libs)]

setup(ext_models = cythonize(extensions))
