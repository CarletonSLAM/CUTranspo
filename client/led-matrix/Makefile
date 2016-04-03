\CXXFLAGS=-Wall -O3 -g
OBJECTS=display-text.o
BINARIES=led-matrix display-text
ALL_BINARIES=$(BINARIES)

# Where our library resides. It is split between includes and the binary
# library in lib
RGB_INCDIR=include
RGB_LIBDIR=lib
RGB_LIBRARY_NAME=rgbmatrix
RGB_LIBRARY=$(RGB_LIBDIR)/lib$(RGB_LIBRARY_NAME).a
LDFLAGS+=-L$(RGB_LIBDIR) -l$(RGB_LIBRARY_NAME) -lrt -lm -lpthread

PYTHON_LIB_DIR=python

# Imagemagic flags, only needed if actually compiled.
MAGICK_CXXFLAGS=`GraphicsMagick++-config --cppflags --cxxflags`
MAGICK_LDFLAGS=`GraphicsMagick++-config --ldflags --libs`

all : $(BINARIES)

$(RGB_LIBRARY): FORCE
	$(MAKE) -C $(RGB_LIBDIR)

led-matrix : demo-main.o $(RGB_LIBRARY)
	$(CXX) $(CXXFLAGS) demo-main.o -o $@ $(LDFLAGS)

display-text : display-text.o $(RGB_LIBRARY)
	$(CXX) $(CXXFLAGS) display-text.o -o $@ $(LDFLAGS)

%.o : %.cc
	$(CXX) -I$(RGB_INCDIR) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJECTS) $(ALL_BINARIES)
	$(MAKE) -C lib clean
	$(MAKE) -C $(PYTHON_LIB_DIR) clean

build-python: $(RGB_LIBRARY)
	$(MAKE) -C $(PYTHON_LIB_DIR) build

install-python: build-python
	$(MAKE) -C $(PYTHON_LIB_DIR) install

FORCE:
.PHONY: FORCE
