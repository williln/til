# Create a new Python virtual environment 

With: 

- virtualenvwrapper 
- pyenv 

See [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/#using-pyenv-to-install-python) for info on installing multiple versions of Python. See this [StackOverflow](https://stackoverflow.com/questions/73898903/how-do-i-get-pyenv-to-display-the-executable-path-for-an-installed-version) for info on how to get the path to your python. 

When you need a new virtual environment with a specific Python version, you need to specify the path to that version of Python. With pyenv, it took me a second to figure that out. 

Run `pyenv which python` to get the current version of Python, and by extension, your pyenv path 

    $ pyenv which python 
    /Users/lacey/.pyenv/versions/3.7.6/bin/python

  
Replace `3.7.6` with whichever version of Python you have installed when you run the command to make the new virtualenv.

    $ mkvirtualenv -p /Users/lacey/.pyenv/versions/3.10.4/bin/python venv-name 
    $ (venv-name) 
  
Move on with your life! 
