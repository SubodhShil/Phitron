> # ```Django``` 

## ```Request response model```

Types of request: These 4 types also known as CRUD operations.
1. **GET** or **REQUEST**: To get existing data that saved in the database on request process. We make request through URL's.
2. **POST** or **CREATE**: To add new data to the database.
3. **UPDATE**: To change or update existing data.
4. **DELETE**: To remove data from database.

&nbsp;
- Django follows MVT (Model View Template) pattern.
  - **Model**: The data we want to present, usually data from a website.
  - **View**: A request handler the returns the relevant template and content - based on the request from the user. 
  - **Template**: Template is the frontend files that sent to user on request as response. 

- Django called a **'batteries included framework'** because it shiped with various features, lessen developer hardship.


## ```Django file structure```

**Synchronous workflow**: একটি কাজ শেষ না হওয়া পর্যন্ত আরেকটি কাজ শুরু হবে না ।   
**Asynchrounous workflow**: দুইটি বা তার বেশি কাজ একসাথে করতে পারে । 

### **```Project vs Application```**
একটি project অনেকগুলো application এর সমন্বয়ে তৈরি হয় । Application হলো একটি project এর ছোট অংশ এবং application project ছাড়া চলতে পারে না । 

models.py file মূলত database তৈরি করার জন্য ব্যবহার করা হয় । 
views.py file টিতে logic গুলো লেখা থাকে । 

## ```Django Installation and other commands```
1. Globally 
2. Virtual environment
   1. Command: **```python -m venv room```**.
   2. A folder **"room"** just created in the current directory, go inside the folder and from that directory create a django project using this command: **```django-admin startproject demo```**.
   3. Go to the recently created project namely **"demo"** and run the django application using this command: **```python manage.py runserver```**.
   4. For creating a project: ```django-admin startproject project_name```
   5. For creating an application: ```django-admin startapp app_name```  
  Caution: যখন নতুন django project বানানো হয় তখন views.py file থাকে না, এটা manually create করে নিতে হয় । 


যখন user কোন url hit করে বা request করে তখন মূলত request টি views এর মধ্যে url এর জন্য responsible বা url এর জন্য logic গুলো যে function টিতে লেখা আছে সেখানে trigger করবে । 

## Working with apps 
একটি নতুন app create করার পর সেটাকে project এ use করার জন্য অবশ্যই settings.py file এর ভিতরের INSTALLED_APPS list টিতে app এর নামটি লিখে দিতে হবে । 

