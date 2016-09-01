#!/bin/bash
rm antlr_generated
mkdir antlr_generated
mkdir antlr_generated/java
mkdir antlr_generated/python
antlr4 vhdl.g4 -o antlr_generated/java
javac antlr_generated/java/*.java
antlr4 -Dlanguage=Python3 vhdl.g4 -o antlr_generated/python
