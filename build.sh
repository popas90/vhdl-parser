#!/bin/bash
printf 'Creating folder tree...'
if [ -d "generated" ]; then
  rm -rdf generated/
fi
mkdir generated
mkdir generated/java
printf 'Done\n'
printf 'Generating Java lexer and parser...'
java -jar /usr/local/lib/antlr-4.5.3-complete.jar Vhdl.g4 -visitor -o generated/java
printf 'Done\n'
printf 'Compiling Java lexer and parser...'
javac -classpath /usr/local/lib/antlr-4.5.3-complete.jar generated/java/*.java
printf 'Done\n'
printf 'Generating Python3 lexer and parser...'
java -jar /usr/local/lib/antlr-4.5.3-complete.jar -Dlanguage=Python3 Vhdl.g4 -visitor -o generated
printf 'Done\n'
chown $USER -R generated/
cd generated
touch __init__.py
