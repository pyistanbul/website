# Python Istanbul Website

[![Build Status](https://travis-ci.org/pyistanbul/website.png?branch=master)](https://travis-ci.org/pyistanbul/website)

## Installation

```sh
öncelikle repomuzu local makinemize kopyalıyoruz
$ git clone https://github.com/pyistanbul/website.git
cd komutu sayesinde klonladığımız klasör içerisine giriyoruz
$ cd website/
çalışmalarımızın izole bir şekilde kalması için virtualenv kullanarak kendi çalışma ortamızı oluşturuyoruz
$ virtualenv venv
source yada . komutu ile oluşturduğumuz çalışma ortamımızı aktive ediyoruz
$ . venv/bin/activate
pip python paket yöneticisi ile conf/requirments.txt dosyası içerisinde bulunan projenin bağımlılıklarını kuruyoruz
$ pip install -r conf/requirements.txt 
settings_local.py dosyasına erişim sağlayabilmek istiyoruz bu nedenle .dist uzantısından kurtulmak için cp komutundan faydalanıyoruz
$ cp pyist/settings_local.py.dist pyist/settings_local.py
veritabanı modellerimizi migrate komutu ile gerçekleştirmiş oluyoruz
$ python manage.py migrate
runserver komutu ile projemizi local makinede çalıştırmış oluyoruz
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
