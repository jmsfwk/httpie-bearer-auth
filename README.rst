httpie-bearer-auth
==================

Bearer auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

Installation
------------

.. code-block:: bash

    $ pip install httpie-bearer-auth

You should now see ``bearer`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=bearer --auth=94a08da1fecbb6e8b46990538c7b50b2 example.org

License
-------

Copyright (c) 2016 The Guardian. Available under the MIT License.

Copyright (c) 2021 James Fenwick.
