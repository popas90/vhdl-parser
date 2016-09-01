#!/bin/bash
cd /usr/local/lib
wget http://www.antlr.org/download/antlr-4.5.3-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH"
