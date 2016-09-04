# vhdl-parser
ANTLR-based VHDL parser.

### Development setup:
  This is the simplest way to get the project up and running:
  - make sure you have python3.5, virtualenvwrapper and JDK available
  - create a new virtualenv using python3.5:
    `$ mkproject -p python3.5 vhdl-parser`
  - now, clone the repo in that new folder
  - install requirements:
    `$ pip install -r requirements.txt`
  - run `setup.sh` - it will download and set up ANTLR
  - edit .bashrc to add aliases for ANTLR and TestRig - add the following lines:
    `export CLASSPATH=".:/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH"`
    `alias antlr4='java -jar /usr/local/lib/antlr-4.5.3-complete.jar'`
    `alias grun='java org.antlr.v4.gui.TestRig'`
  - then, source bash:
    `$ . ~/.bashrc`
  - new commands `antlr4` and `grun` are now available
