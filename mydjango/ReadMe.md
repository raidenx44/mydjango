Commands Used

python manage.py makemigrations
python manage.py makemigrations myblog
python manage.py migrate

It woud create tables from your model to database set in settings (sql-lite)

#you can create many admins as you want
python manage.py createsuperuser 
user: admin
pass: 12345

http://localhost:8000/blog/
http://localhost:8000/blog-admin/



### Using Pre templated Admin Panel
in your admin.py - import the model then
admin.site.register(<your desired model>)
Go to:
http://localhost:8000/admin
use admin credential
