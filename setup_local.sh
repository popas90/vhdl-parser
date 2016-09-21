#!/bin/bash
[ -d "lib" ] || mkdir lib
chown $USER -R lib/
cd lib
wget http://www.antlr.org/download/antlr-4.5.3-complete.jar
export CLASSPATH=".:$(pwd)/lib/antlr-4.5.3-complete.jar:$CLASSPATH"
