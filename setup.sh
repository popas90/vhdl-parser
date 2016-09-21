#!/bin/bash

if [ "$#" -eq "0" ]; then
  echo "Setting up ANTLR in default location /usr/local/lib ..."
  cd /usr/local/lib
  wget http://www.antlr.org/download/antlr-4.5.3-complete.jar
  export CLASSPATH=".:/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH"
  echo "OK"
else
  case "$1" in
    -l|--local)
      echo "Setting up ANTLR in $(pwd)/lib ..."
      [ -d "lib" ] || mkdir lib
      chown $USER -R lib/
      cd lib
      wget http://www.antlr.org/download/antlr-4.5.3-complete.jar
      export CLASSPATH=".:$(pwd)/lib/antlr-4.5.3-complete.jar:$CLASSPATH"
      echo "OK"
      ;;
    *)
      echo "Invalid usage: setup.sh [-l|--local]"
      ;;
  esac
fi
