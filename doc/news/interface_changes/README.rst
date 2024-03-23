Interface Changes
=================

Add news fragments for interface changes (e.g. xml changes) to this directory.
The format should be ``<JIRA TICKET>.<COMPONENT>.rst``, where ``<COMPONENT>`` is the name of the component in lowercase.
For example, a news fragment for a change in the ``ATAOS`` component under ticket DM-12345 would be ``DM-12345.ataos.rst``.

If you have ``towncrier`` installed in your environment you can use:

.. code-block::

   towncrier create interface_changes/<JIRA_TICKET>.<TYPE>.rst

