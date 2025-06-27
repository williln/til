# Create a new Python virtual environment/ pyenv cheat sheet

With: 

- pyenv 

See [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/#using-pyenv-to-install-python) for info on installing multiple versions of Python. 

When you need a new virtual environment with a specific Python version, you need to specify the path to that version of Python. With pyenv, it took me a second to figure that out. 

Run `pyenv which python` to get the current version of Python, and by extension, your pyenv path 

    $ pyenv which python 
    /Users/lacey/.pyenv/versions/3.7.6/bin/python
  
Move on with your life! 

    # Create a new virtual env
    pyenv virtualenv <python_version> <environment_name>
    
    # Activate the venv
    pyenv activate <environment_name>
    
    # Deactivate the vent
    pyenv deactivate 

If you're not sure which Python versions you have available to you, run 

    $ pyenv versions

And you will see a list of Python versions you have installed. 

If you want to see which Python versions you can install, run 

    $ pyenv install -l 

To install a version, run: 

    $ pyenv install {version} 
