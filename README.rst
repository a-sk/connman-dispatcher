Description
===========
Another project generation tool based on templates.

Install
=======
    pip install templet [--user]

Config
======

Configuration file path:

    ~/.config/templet/config.json

Configuration example
=====================

.. code-block:: javascript

    {
    "templates": {
        "$PATH": ["path/to/common/templates/folder"]
        "test": "path/to/template/in/different/folder"
        }
    }
