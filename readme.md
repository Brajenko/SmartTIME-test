# Smart time test task

## Prerequisites
python^3.12

## Setup & run
```bash
pip install -r requirements.txt
python manage.py runserver
```

## Usage
### Admin panel
http://127.0.0.1:8000/admin
#### Admin creds
- Email: `admin@admin.com`
- Password: `admin`

### Non-admin creds
- Email: 3 emails, see admin panel
- Password: `password`

### API docs
http://127.0.0.1:8000/api/docs


## Testing
```bash
python manage.py test
```
