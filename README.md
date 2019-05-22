# Instruction for running test 


## Clone repository

Use this command
```commandline
git clone https://github.com/Ksen4ik/Python-Project.git
```

#### Notes

- Please, make sure your ```Chrome browser's version is 74```
- ```Chromedriver's version``` in the repository is ```74```. If you're using another version of Chrome, [here is the link](http://chromedriver.chromium.org/) for download another chromedriver, according to your Chrome browser's version and just replace file.


## Install Python

Here is the [link](https://www.python.org/downloads/) for install Python 3.6


## Install pip

Use [pip](https://pip.pypa.io/en/latest/installing/) to run our commands. 

## Install and run venv
- Setup [venv](https://docs.python.org/3/library/venv.html) for run our files and activate it via command
```commandline
source venv/bin/activate
```

## Set python path

- After ```"$PYTHONPATH=..."``` you should set path to downloaded project

```commandline
export PYTHONPATH="$PYTHONPATH:/home/kbelotserkovets/Documents/Python-Project/"

```

## Install required packages

- Open Terminal\cmd from ```Python-Project``` folder
- Type:
```commandline
pip install -r requirements.txt
```




## Run via IDE

- Open ```test_login_page.py``` file in any [JetBrains IDE](https://www.jetbrains.com/). In my case, I'm using [PyCharm](https://www.jetbrains.com/pycharm/?fromMenu)
- Run this file by clicking ```Shift + F10```


## Run via Terminal  from ```Python-Project``` (Linux/Mac)

```commandline
python test_login_page.py 
```

## Run via cmd from ```Python-Project``` (Windows)

```commandline
python3 test_login_page.py
```






 