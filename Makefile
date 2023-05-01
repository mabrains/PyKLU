# Simple C Wrapper Makefile. Provide routine for solving linear system.

default: all

CC = gcc
SS_VER = 7.0.1

LIBPATH = ./temp/SuiteSparse-$(SS_VER)/

INCLUDE = -I$(LIBPATH)/KLU/Include \
          -I$(LIBPATH)/AMD/Include \
          -I$(LIBPATH)/BTF/Include \
          -I$(LIBPATH)/COLAMD/Include \
          -I$(LIBPATH)/SuiteSparse_config

LIB = $(LIBPATH)/KLU/build/libklu.a \
      $(LIBPATH)/BTF/build/libbtf.a \
	  $(LIBPATH)/AMD/build/libamd.a \
      $(LIBPATH)/COLAMD/build/libcolamd.a

temp:
	mkdir temp

temp/$(SS_VER).tar.gz: temp
	wget -O ./temp/SuiteSparse.tar.gz https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/refs/tags/v$(SS_VER).tar.gz

.ONESHELL:
temp/SuiteSparse-$(SS_VER): temp/$(SS_VER).tar.gz
	cd ./temp/
	tar -zxvf SuiteSparse.tar.gz

.ONESHELL:
suite_sparse_build: temp/SuiteSparse-$(SS_VER)
	cd ./temp/SuiteSparse-$(SS_VER)
	make

pyKLU: pyklu.c suite_sparse_build
	$(CC) -shared pyklu.c $(LIB) $(INCLUDE) -o pyklu/libpyklu.so

all: pyKLU



