#!/bin/bash
rm antlr_generated
mkdir antlr_generated
mkdir antlr_generated/java
mkdir antlr_generated/python
java -jar /usr/local/lib/antlr-4.5.3-complete.jar vhdl.g4 -o antlr_generated/java
javac antlr_generated/java/*.java
java -jar /usr/local/lib/antlr-4.5.3-complete.jar -Dlanguage=Python3 vhdl.g4 -o antlr_generated/python
