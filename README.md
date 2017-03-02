# djcra
Django :heart: create-react-app integration example

## cdn demo

we use `http://localhost:8080` as our cdn in this example

## how to run cdn example

* we updated `STATIC_URL` and `FRONTEND_DEV` in `settings.py` file. 
```
STATIC_URL = 'http://localhost:8080/static/'
FRONTEND_DEV = False
```
* build static file
```
REACT_APP_PUBLIC_URL=http://localhost:8080 npm run build
```
run servers 

```
$ python manage.py runserver
$ http-server build
```
I use [http-server](https://www.npmjs.com/package/http-server) as  cdn server in this demo 


### logs
http-server:
```
[Thu Mar 02 2017 17:44:25 GMT+0330 (IRST)] "GET /static/css/main.9a0fe4f1.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
[Thu Mar 02 2017 17:44:25 GMT+0330 (IRST)] "GET /static/js/main.1f1f0e76.js" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
[Thu Mar 02 2017 17:44:25 GMT+0330 (IRST)] "GET /static/media/logo.5d5d9eef.svg" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
```
django log:
```
[02/Mar/2017 14:14:25] "GET / HTTP/1.1" 200 467
```
