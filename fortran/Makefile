#CAMB Makefile

#Set FISHER=Y to compile bispectrum fisher matrix code
FISHER=

#Edit for your compiler
#Note there are many old ifort versions, some of which behave oddly


#Intel , -openmp toggles mutli-processor:
#note version 10.0 gives wrong result for lensed when compiled with -openmp [fixed in 10.1]
compiler_ver = $(shell gfortran -dumpversion 2>&1)
COMPILER = gfortran
F90C     = gfortran
COMMON_FFLAGS = -MMD -cpp -ffree-line-length-none -fno-underscoring -fmax-errors=4 -fopenmp
# Using -ffast-math causes differences between Debug and Release configurations.
FFLAGS = -O3 $(COMMON_FFLAGS)
DEBUGFLAGS = -g -fbacktrace -ffpe-trap=invalid,overflow,zero -fbounds-check $(COMMON_FFLAGS)
SFFLAGS =  -shared -fPIC
MODOUT =  -J$(OUTPUT_DIR)
SMODOUT = -J$(DLL_DIR)


## This is flag is passed to the Fortran compiler allowing it to link C++ if required (not usually):
ifneq ($(FISHER),)
F90CRLINK = -lblas -llapack
endif


#Settings for building camb_fits
#Location of FITSIO and name of library
FITSDIR       ?= /usr/local/lib
FITSLIB       = cfitsio
#Location of HEALPIX for building camb_fits
HEALPIXDIR    ?= /usr/local/healpix

ifneq ($(FISHER),)
FFLAGS += -DFISHER
EXTCAMBFILES = Matrix_utils.o
else
EXTCAMBFILES =
endif

include ./Makefile_main
