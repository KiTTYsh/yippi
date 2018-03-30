.. currentmodule:: yippi

Getting Started
===============

Requirements
----------------
* Python 3

Installing
-----------

To install, just clone the repository and type this command below under root of project: ::

> $ pip install .

Example Usage
------------------

Here's a very basic example of using Yippi, along with comment to help you understand.::

> import yippi # Imports yippi, of course.
>
> results = yippi.search(['girly', 'male', 'fox']) # Searches e621 with "girly male fox" as queries
> results[0].artist # Pick the first result from the list and show the artist.

But that's not the end! There are a lot of things you'll find here, have fun!