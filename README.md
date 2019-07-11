# PythonMultiDB-Website
webapp with using more than one models on diferent databases on MySQL

First Attempt to show how we can develop in Python a two database web app. It automatically understands which one to use based on app name.

MySQL 8.0
Python 3.7

<h3>Additional</h3>
in order to get this work you need to do the following:
1. Run on MySQL these two commands: create database animal_data; create database person_data;
2. Run on python cmd: manage.py migrate --database=persons manage.py migrate --database=animals
