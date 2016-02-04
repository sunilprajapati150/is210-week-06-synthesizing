####################
IS 210 Assignment 06
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========

In this assignment, we'll look at two practical examples of using lists to
achieve a real-world objective.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

You've been tasked with organizing a party. There are a large number of
families attending with each family to receive its own table. A table may only
seat a set number of people, so families in excess of that number will need to
be split across multiple tables but **will not** be combined with members of
other families.

Create a function that can analyze arbitrary lists of families and return
a total headcount for your caterer as well as a total number of tables
needed.

Specifications
^^^^^^^^^^^^^^

1.  Create a module named ``task_01.py``

2.  Create a function called ``get_party_stats()`` that takes two parameters:

    1.  ``families``, a list of families which are, themselves, lists of
        members, eg:

        .. code:: python

            [['Angel', 'Michael', 'Samuel'], ['Jennifer', 'James']]

    2.  ``table_size``, the maximum number of seats at each table, defaults
        to six (6)

4.  Loop through your list with the ``for`` loop and count not only the
    total number of attendees but *also* the number of tables necessary to
    seat all the guests.

    Remember that, at this party, families are being anti-social and will not
    be seated with other families.

5.  Return the results in a tuple:

    1.  total number of guests

    2.  total number of tables

.. hint::

    If you're stumped on how to count the number of tables because Python's
    integer division can't account for fractions, consider the following:

    .. code:: python

        -(-x // y)

    The floor division operator ``//`` always floors a division but if we
    invert the numerator prior to division then invert it again after floor
    division we've effectively created a pseudo-ceiling division without having
    to resort to using the ``math`` module!
    
.. warning::

    Neither of these tasks require a counter to use it. Counters are not an
    inherent part of loops.

Examples
^^^^^^^^

.. code:: pycon

    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
    (6, 4)

.. hint::

    Use our simulator in the data module to try random party sizes with your
    code.

    .. code:: pycon

        >>> import data
        >>> data.get_party_list()

Task 02
-------

Imagine that you've been tasked with setting up appointments with a large
client base. You have a system that capture the client name and the time of
their appointments but you'd like to send a reminder e-mail blast to each
client.

For our final exercise this week, we'll be preparing some data as though we
were about to send automated e-mails. With lists and a basic ``for`` loop,
there's little we can't accomplish!

Specifications
^^^^^^^^^^^^^^

1.  Create a new module named ``task_02.py``

2.  Create a function named ``prepare_email()`` that takes one argument:

    1.  ``appointments``, A list of two-item tuples with the client's name
        and their appointment time as members:

        .. code:: python::

        [('Wiley', 'Monday, March 16, 2015 05:16PM'), ...]

3.  Use a ``for`` loop and ``.format()`` to create a new list with just the
    client's email body. The body of the email should use the following
    formatting string:

    .. code:: python::

        'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    Return your new list.

.. warning::

    You'll be tempted to re-define your above format string inside your ``for``
    loop but that would be a violation of our DRY principle since it would
    continually be re-created. Define the base string outside the loop and
    just use it as a variable inside when you create your output.

Examples
^^^^^^^^

.. code:: pycon

    >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
    ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
    'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ ./runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
