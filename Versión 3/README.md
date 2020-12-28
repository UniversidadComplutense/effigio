Introduction
========
This version of effigio is made to be hosted in a web site. Effigio is a development based on obs.ninja to share your camera and desktop in various ways.


Develop instructions
=====

Modify the EffigioOnline.py with the modifications. You can try them with, for instance, with

	python3 EffigioOnline.py 5 0
	
To make this work online, you need EffigioPyodide.py. That's what will be executed online. It uses an import to integrate EffigioOnline.py. Nevertheless, there are a few lines to capture parameters from the web that will not work on the terminal. More instructions, in the code.

To create the executable for online version, run 

	sh createPythonForWeb.sh

This will take EffigioOnline.py, will cut the part before the "main" header, will paste it instead of the "import Effigio" part in EffigioOnline.py, and the result will be copied into a file "web.py" which is what you actually need.

Once done, you can try launching a web server in the same folder where these files are

	python3 -m http.server
	
Then, launch the browser for http://localhost:8000/EffigioOnline.html

Once you see the GUI, type the number of invites you want and press the button. You will receive three files:

* A json file for configuring OBS-Studio
* A csv file with the URL for invites
* A .tex file with custom invitations that can be rendered using LUALATEX into a printable pdf

Deploy instructions
===============

To make this available online, you only need a basic web server somewhere. The necessary files are:

* EffigioOnline.html
* web.py

The code is run on the client side, so there is no overload for the server, aside of the payload transfer implied by these files which is  minimal. 

Demo 
=====

There is a demo hosted in [https://universidadcomplutense.github.io/effigio/](https://universidadcomplutense.github.io/effigio/)




