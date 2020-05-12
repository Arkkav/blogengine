# Blog

### Technical requirement:
Create a blog with posts and tags with CRUD functionality.

### Implementation:
- framework Django
- class-based views (CBV), mixins usage
- pagination
- work with Django template language and forms, template inheritance
- restrict access to pages for administration
- simple search in titles and bodies of posts

### Main modules
- blogengine/blog/views.py - business logic module
- blogengine/blog/utils.py - mixins for views.py module
- blogengine/blog/models.py - DB models description
- blogengine/urls.py, blogengine/blog/urls.py - application URLs routing

### Deployment
git clone https://github.com/Arkkav/blogengine.git <br/>
cd ./blogengine <br/>
python3 -m venv ./env <br/>
. env/bin/activate<br/>
pip3 install -r requirements.txt <br/>
./manage.py runserver 5000 <br/>