#!/bin/bash
set -o errexit

if [ "$#" -eq "0" ]; then
  antlrpath="/usr/local"
else
  case "$1" in
    -l|--local)
      antlrpath="$(pwd)"
      ;;
    *)
      echo "Invalid usage: build.sh [-l|--local]"
      ;;
  esac
fi

printf 'Creating folder tree...'
if [ -d "generated" ]; then
  rm -rdf generated/
fi
mkdir generated
mkdir generated/java
printf 'OK\n'
printf 'Generating Java lexer and parser...'
java -jar "$antlrpath/lib/antlr-4.5.3-complete.jar" Vhdl.g4 -visitor -o generated/java
printf 'OK\n'
printf 'Compiling Java lexer and parser...'
javac -classpath "$antlrpath/lib/antlr-4.5.3-complete.jar" generated/java/*.java
printf 'OK\n'
printf 'Generating Python3 lexer and parser...'
java -jar "$antlrpath/lib/antlr-4.5.3-complete.jar" -Dlanguage=Python3 Vhdl.g4 -visitor -o generated
printf 'OK\n'
chown $USER -R generated/
cd generated
touch __init__.py
