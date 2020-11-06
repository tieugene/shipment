# Shipment

General purpose file storage with addition functionality for shipping documents archiving.

## Features
- Shipping documents have attributes to filter and sort:
  - Own organization
  - Partner
  - Document (shipping) date
  - Document type (orders, bills, invoices etc)
- Bulk uploading documents
- Uploading document type restriction (PDF only)

## Requires
- Python 3.x (python3)
- Django 3.0+ (python3-django)
- Python-file-magic (python3-file-magic)
- Django-compatible RDB backend (~~SQLite,~~ MariaDB, PostgreSQL etc)
- python3-mod_wsgi (for wsgi)

## Installation

Platform: Fedora 33, Apache 2.4, wsgi, sqlite3 db backend

Shortcuts:

Part | Variable | Path
-----|----------|------
Code | APPDIR   | /mnt/shares/www/shipment/
Data | MEDIADIR | /mnt/shares/media/shipment/
DB   | DBPATH   | /mnt/shares/db/sqlite/shipment/db.sqlit3

### 1. Get code:

```
git clone https://github.com/tieugene/shipment.git $APPDIR
chown -R apache:apache $APPDIR
```

### 2. Create other storages:

```
sudo mkdir -p $MEDIADIR
sudo chown apache:apache $MEDIADIR
sudo mkdir -p $DBPATH
sudo chown apache:apache $DBPATH
```

### 3. Prepare environment:

```
cp $APPDIR/local_setting.py.sample $APPDIR/local_settings.py
```

### 4. Prepare db etc:

```
# create db
./manage.py migrate
# create admin
./manage.py createsuperuser --username root --email root@example.com --noinput
# echo "password" | ./manage.py changepassword root
# mk i18n
./manage.py compilemessages
# add admin static (static/README)
# ln -s ...
# load initial data (option):
# ./manage.py loaddata ...
```

### 6. Prepare Apache:

```
sudo ln -s $APPDIR/shipment.conf /etc/httpd/conf.d/shipment.conf
```

### X. Let's go:

```
sudo systemctl restart httpd
xdg-open http://localhost/shipment/
```
