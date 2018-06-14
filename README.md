# Command-Line Parsing Libraries
Comparing Argparse, Docopt and Click libraries.

Compares each library for implementing the following features:

* Commands <code>hello</code> and <code>goodbye</code>
* Arguments <code>name</code>
* Options/Flags <code>--greetings=<str></code> and <code>--caps</code>

Additional features:

* Version Printing <code>-v</code> or <code>--version</code>
* Automated Help Messages
* Error Handling


### Set-up for Usage

* Install [python3](https://www.python.org)
* Install and setup [Virtual
  Envrionment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and [Virtual environment
  wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
* Install Required Dependancies
        <code>$ pip install -r requirements.txt</code>  

Run Script:
        <code>$ python3 [file].py [command] [options] NAME</code>


#### Basic usage
<mark>Shell</mark>
<pre>
$ python3 [file].py hello Kyle
Hello, Kyle!

$ python3 [file].py goodbye Kyle
Goodbye, Kyle!
</pre>
#### Usage w/Options (Flags)
<pre>
$ python [file].py hello --greeting=Wazzup Kyle
Whazzup, Kyle!

$ python [file].py goodbye --greeting=Later Kyle
Later, Kyle!

$ python [file].py hello --caps Kyle
HELLO, KYLE!

$ python [file].py hello --greeting=Wazzup --caps Kyle
WAZZUP, KYLE!
</pre>

##### Atribution
[Tutorial](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)By [Kyle
Purdon](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/#author)




