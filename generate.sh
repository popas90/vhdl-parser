#!/bin/bash
printf 'Creating folder tree...'
rm -r antlr_generated
mkdir antlr_generated
mkdir antlr_generated/java
mkdir antlr_generated/python
printf 'Done\n'
printf 'Generating Java lexer and parser...'
java -jar /usr/local/lib/antlr-4.5.3-complete.jar vhdl.g4 -o antlr_generated/java
printf 'Done\n'
printf 'Compiling Java lexer and parser...'
javac -classpath /usr/local/lib/antlr-4.5.3-complete.jar antlr_generated/java/*.java
printf 'Done\n'
printf 'Generating Python3 lexer and parser...'
java -jar /usr/local/lib/antlr-4.5.3-complete.jar -Dlanguage=Python3 vhdl.g4 -o antlr_generated/python
printf 'Done\n'
