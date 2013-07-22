collective.fundraising.core
===========================

Core modules for Collective Fundraising, an open source and feature rich fundraising system for non-profits built on the Plone CMS.

This is still heavily under development.  Do not use on production sites!!!

Run the buildout and run the unit tests:

$ git clone https://github.com/jlantz/collective.fundraising.core.git
$ cd collective.fundraising.core
$ python bootstrap.py
$ bin/buildout
$ bin/test

A few seconds after running bin/test you should see Firefox pop open and run through the test scenarios.  The output in the terminal from bin/test will tell you where you can find the report.html file from the robot framework tests.
