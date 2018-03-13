#!/usr/bin/zsh
 g++ `pkg-config --cflags opencv` $1 `pkg-config --libs opencv` -o $2
