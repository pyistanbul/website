# Python Istanbul Website

[![Build Status](https://travis-ci.org/pyistanbul/website.png?branch=master)](https://travis-ci.org/pyistanbul/website)

## Installation in this!!

```sh
$ git clone https://github.com/pyistanbul/website.git
$ cd website/
$ pipenv install
$ pipenv shell
$ cp pyist/settings_local.py.dist pyist/settings_local.py
$ python manage.py migrate
$ python manage.py runserver
$ open http://127.0.0.1:8000/
```

To run all unit tests:

```sh
$ python manage.py test -v2
```

### License

Copyright © 2013 Python Istanbul

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.
