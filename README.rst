django-tooltips
===============

Manageable bootstrap tooltips

Requirements
------------

-  Django
-  Bootstrap
-  jQuery

Installation
------------

Install the app via pip:

::

   $ pip install django-tooltips

Add ``tooltips`` to ``INSTALLED_APPS``:

.. code:: python

   INSTALLED_APPS = (
       ...
       'tooltips',
       ...
   )

Add the processor to your ``TEMPLATE_CONTEXT_PROCESSORS``:

.. code:: python

   TEMPLATE_CONTEXT_PROCESSORS = (
       ...
       'tooltips.processors.tooltips',
   )

Include this in your templates (eg, ``base.html``):

::

   {% include "tooltips/tooltips.html" %}

And run the migrations:

::

       $ manage.py migrate tooltips

Now, whenever you add a tooltip via the admin, it will appear on your
pages just after the element you provided via the javascript selector:

Preview
-------

Clientside:

.. figure:: https://raw.github.com/akennedy90/django-tooltips/master/preview.png
   :alt: Client-side

   Client-side

Admin:

.. figure:: https://raw.github.com/akennedy90/django-tooltips/master/admin.png
   :alt: Admin

   Admin

Caveats
-------

As the selectors are regular jQuery selectors, try to keep your search
scope to a minimum for better performance. The URL field must be exact,
including the trailing slash.