# djcra
Django :heart: create-react-app integration example

## how to run project

### In frontend development mode:
* set `FRONTEND_DEV = True` in `settings.py`
* run servers
```
$ REACT_APP_PUBLIC_URL=http://localhost:3000 npm start
$ python manage.py runserver
```

### In backend-only development mode:
* set `FRONTEND_DEV = False` in `settings.py`
* build static files
* run python server
```
$ npm run build
$ python manage.py runserver
```
### In production mode
* set `FRONTEND_DEV = False` in `settings.py`
* build static files
* collect static files
```
$ npm run build
$ python manage.py collectstatic
```
* deploy your django project [mdn guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

### In production with cdn
* update `STATIC_URL` and `FRONTEND_DEV` in `settings.py` file. 
```
STATIC_URL = 'http://cdn.mysite.com/static/'
FRONTEND_DEV = False
```
* build static file
```
REACT_APP_PUBLIC_URL=http://cdn.mysite.com npm run build
```

## the :broken_heart: parts
problems that need your help.

### hot reload problem
`http://localhost:8000/sockjs-node/` not found in django.

### images problem
CRA assets starts with `/static/`. so we need add `http://localhost:3000` before them.
```jsx
import logo from './logo.svg';
console.log(logo); // "/static/media/logo.5d5d9eef.svg"
<img src={(process.env.REACT_APP_PUBLIC_URL || '') + logo} alt="logo" />
```

## what happen until now

create react app named `cra-prj`
```
$ create-react-app cra-prj
```

create django project named djcra
```
$ django-admin startproject djcra
$ mv djcra django_prj
echo 'Django==1.10.5' > django_prj/requirements.txt
```

I add some files to projects