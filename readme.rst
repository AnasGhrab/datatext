========
DaTaText
========

DaTaText (*still a draft...*) is a Django-python3 app manage digital texts from manuscripts, mainly as a catalogue and critical editions in the TEI format.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "datatext" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'datatext',
    )

3. Run `python manage.py makemigrations` then `python manage.py migrate` to create datatext models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled).


Contact
=======

Homepage: http://anas.ghrab.tn

Email:

 * Anas Ghrab <anas.ghrab@gmail.com>

License
=======

The MIT License (MIT)

Copyright (c) 2015 Anas Ghrab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.