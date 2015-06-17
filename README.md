python-fullstack-python
=======================

This repo is an example of a "full stack" python application. Things this involves:

* Frontend (nginx)
* JS App (Ember)
* Simple Python API (Django + Django Rest Framework)
* DB (Postgres)

Requirements:
-------------

* A Mac (I'm sad too)
* Boot2Docker
* Docker
* docker-compose
* jq
* Command line familiarity

```bash
$ alias fig=docker-compose
```

How to Run:
-----------

```bash
$ fig up python
```

Now see if the API is working:

```bash
$ $ curl -s http://192.168.59.103:8000/api/random_number/ | jq .
{
  "value": "94"
}
```

We also have Nginx setup as a frontend, let's try this out. Navigate to [http://192.168.59.103:7000/api/random_number](http://192.168.59.103:7000/api/random_number)

If you get a nice Django Rest Framework page with a random number, it worked!

TODO:
-----

 - [x] Setup Django Project
 - [x] Setup Nginx
 - [ ] Ember App
 - [ ] Setup Postgres
