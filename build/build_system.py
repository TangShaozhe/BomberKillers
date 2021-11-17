import sys
import os
import subprocess
import time

def check_Py_Version():
    print("the python Version should be at least 3.6")
    print("Here is your version :")
    os.system("py -V")
    

def install_pip():
    
    try:
        if os.system("python -m pip install --upgrade pip") != 0:
            raise Exception('Have problem when installing pip')
    except Exception as e:
        print(e)
        print("plz try to solve it!")


def install_pip_plugin():
    try:
        if os.system("pip install flake8 flake8-html coverage pytest pygame") != 0:
            raise Exception('Have problem when installing pip plugin')
    except Exception as e:
        print(e)
        print("plz try to solve it!")

def Lint_with_flake8():
    try:
        if os.system("flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics") != 0:
            raise Exception('Have problem when Linting')
    except Exception as e:
        print(e)
        print("plz try to solve it!")
    try:
        if os.system("cd ..&&flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --format=html --htmldir=report/flake-report") != 0:
            raise Exception('Have problem when Linting')
    except Exception as e:
        print(e)
        print("plz try to solve it!")

def coverage_with_report():
    try:
        if os.system("cd ..&&cd report&&coverage run ../test/test_Game.py&&coverage html -d coverage-report") != 0:
            raise Exception('Have problem when coverage with report')
    except Exception as e:
        print(e)
        print("plz try to solve it!")

def test_with_pytest():
    try:
        if os.system("cd ..&&cd test && pytest") != 0:
            raise Exception('Have problem when pytest')
    except Exception as e:
        print(e)
        print("plz try to solve it!")
    
check_Py_Version()
time.sleep(0.5)
install_pip()
time.sleep(0.5)
install_pip_plugin()
time.sleep(0.5)
Lint_with_flake8()
time.sleep(1)
coverage_with_report()
time.sleep(0.5)
test_with_pytest()

print("Eveything is good to go")