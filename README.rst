Yippi!  |Documentation Status| |Build Status|
=============================================

Yippi is an e621 API wrapper for Python, to make everyone's life
simplier.

Requirements
============

-  Python 3.x
-  urllib
-  json

Installation
============

Clone this repository, and type this down

.. code:: bash

    $ pip install -e .

Example
=======

.. code:: python

    results = yippi.search(['girly', 'male', 'fox']) # Searches e621 with "girly male fox" as query
    results[0].file_url # Get the image/file's URL

`Full Documentation`_

.. |Documentation Status| image:: https://readthedocs.org/projects/yippi/badge/?version=latest
   :target: http://yippi.readthedocs.io/en/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/Rendyindo/yippi.svg?branch=master
   :target: https://travis-ci.org/Rendyindo/yippi
.. Full Documentation:: https://yippidocs.rorre.me/