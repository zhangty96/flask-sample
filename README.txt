This is a flask structure that I like to use. There will be README’s in most of the directories explaining what they do.


This is designed with Ubuntu 12.04.4 in mind but should work on just about everything except Windows. You’re going to need Python and pip as well.

There’s a guide explains everything in more detail after the line of #####.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

TO RUN:

(if you don’t have it) apt-get install python-pip 
(if you don’t have it) pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python start_server.py

If you want it to stay on:
nohup python start_server.py &

To remove all README’s: 
find . -name “README.txt” -type f -delete


#####################################################################

If you got lost there, here’s an explanation:
(Anything with >>> and indented is code)

After you’ve cloned the repo, we need to set up some python stuff.

First we install a python package that helps us keep other packages organized.
>>>   pip install virtualenv

Then we make a virtual environment using the package we just installed. We can use this virtual python environment to install packages and run code without affecting our real python installation.
>>>   virtualenv venv    (venv can be replaced with whatever, this is just the name)

It should say some stuff about installing packages, that’s good. Next we need to activate that environment.
>>>   source venv/bin/activate

You should now see (venv) in front of your terminal prompt 

The required packages have been “frozen” into a file so that they can be installed all at once. To install all of the required packages to your virtual environment, run:
>>>   pip install -r requirements.txt

Pip is now installing all of the necessary packages. This shouldn’t take too long.
When that finishes, you’re ready to run the server!
>>>   python start_server.py

Running this file runs a tornado script (another python library) that continuously serves the website. Flask apps can be run on their own (python my_app.py) but this is used mostly for local development. I definitely recommend it for development; Flask has some really cool debug features!

To make it serve forever, use:
>>>   nohup python start_server.py &
where nohup tells the program not to “hang up” or quit, when you log off your ssh session, and & tells it to run in the background.

If you want to stop the program, press CTRL+c while it is running.
If you’ve made it run in the background, you’ll need to use 
>>>   pkill —f -n start_server.py

Happy coding!
