# BRIDGEWELL_4szan8_Q3

## Run the server

In Flask environment, simply execute
```
python run_server.py
```
The server will run on `http://127.0.0.1:5000/`

## Get multiply product

Request by URL `http://127.0.0.1:5000/<int>/<int>`
For example, a request `http://127.0.0.1:5000/3/4` returns `12` on resulting page

## Exceptions

If incorrect request is given, such as `http://127.0.0.1:5000/3/a`, 
it can not be found (404 error), and the resulting page will shows 
allowed URLs automatically:
```
The requested URL can not be found.
Only these URL rules are allowed:
['/', '/static/<path:filename>', '/<int:multiplier>/<int:multiplicand>']
```