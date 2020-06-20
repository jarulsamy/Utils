.PHONY: help debug release
DEFAULT: release

help:
	@echo "make help"
	@echo "    View this help"
	@echo "make debug"
	@echo "    Debug with debug flags"
	@echo "make"
	@echo "    Default compilation, no debug flags"
	@echo ""

debug:
	g++ main.cpp -o main.o -DDEBUG

release:
	g++ main.cpp -o main.o
