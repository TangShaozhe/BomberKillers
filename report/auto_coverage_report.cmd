coverage run ../test/test_Game.py
coverage report -m
coverage html -d coverage-report
cd coverage-report
del /f .gitignore
pause