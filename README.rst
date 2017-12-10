###########################
Banda ferdamana's home page
###########################

This is the site fro the Slovenian impov group **Banda ferdamana**.
If you are in Maribor, come check them out.

Developers
==========

This site uses Wagtail_ as a Django_ app, meaning the site is not 
built around Wagtail, but that Wagtail is just the CMS.

To run it localy follow these steps:

.. code:: shell

   # Clone the repository
   git clone https://github.com/dasdachs/bandaferdamana.git
   
   # Install the dependencies using pipenv
   # Make sure to have it installed
   # https://docs.pipenv.org/
   pipenv --three install
   
   # Create the models in the local database
   # Defaults to a sqlite database
   python manage.py migrate 
   # Create a admin or superuser
   python manage.py createsuperuser
   # Run the app
   python manage.py runserver

.. _Wagtail: https://wagtail.io/
.. _Django: https://www.djangoproject.com/ 
