![](https://dubpy8abnqmkw.cloudfront.net/images/feeds/clark_lp/logos/wantedly.png)

# Coding challenge Wantedly

This repository contains the code necessary to build a web app where a user can list his/her skills on a profile page and recommend skills to other users.

## Index

- [Tools used](#tools-used).
- [How does it work?](#how-it-works).
  - [Basic commands](#basic-commands).
  - [First steps](#first-steps).
  - [Inside the program](#inside-program).
  - [Access as an admin](#access-admin).
- [Aims achieved](#aims-achieved).
- [Future work](#future-work).
- [Heroku link](#heroku-link).

### Tools used

- **Django 1.9**: High-level Python Web framework that encourages rapid development and clean, pragmatic design.

- **Python 2.7.12**

### How does it work?

Throughout the next sections, the necessary steps in order to launch the program are explained.

#### Basic commands

- In order to run the program, in the workspace we do:

<pre><code>python manage.py runserver</code></pre>

- If we update the file models.py, before running the upper command, we have to:

<pre><code>
python manage.py makemigrations
python manage.py migrate
</code></pre>

#### First steps

After launching the program, access to the next web page so as to see your program running:

http://127.0.0.1:8000/

Through this link, it is possible to login or register as a user.

#### Inside the program

Once we have logged in the program, there are three main windows:

- **Main Page**: Default web page in which you can access to the other two webs.

- **Profile Page**: It shows all your data: General information and skills you have (With the number of likes that other people have liked). It is possible to complete your profile including your name and age. Furthermore, this web allows the possibility to enter new skills.

- **Users Page**: This web includes the different users in the system, their skills and the number of likes for each one of their skills. It also allows to press like to their skills.

To see all this web pages without the necessity of creating a new user, you can login with:

<pre>
Username: test
Password: admindb
</pre>

#### Access as an admin

It is possible to access to the database as a root by putting the web address shown below. In this web, it is possible to edit freely all the database.

http://127.0.0.1:8000/admin

The username and password of the current root is:

<pre>
Username: admin
Password: wantedly
</pre>

In order to create a new superuser throughout the terminal, this command has to be launched:

<pre><code>
python manage.py createsuperuser
</code></pre>

### Aims achieved

- Database created with the users and skills.
- Possibility of register users and login them.
- Different displays (Main, profile and users page) for different functionalities.
- Possibility of adding in your profile new skills.
- Possibility of pressing like to others skills.

### Future work

- Possibility of deleting skills.
- Ordering the skills based on the number of likes.
- Allowing the users only to press one like for each one of the skills of the other users.
- Asking for profile images for each one of the users.
- Improve the web interface.

## Heroku link

Heroku is a cloud platform as a service (PaaS) supporting several programming languages (Java, Node.js, Scala, Clojure, Python, PHP, and Go) that is used as a web application deployment model. For this reason, Heroku is said to be a polyglot platform as it lets the developer build, run and scale applications in a similar manner across all the languages.

In the next link, it is possible to find this project on such platform.

https://wantedlycodechallenge.herokuapp.com/
