Recording Changes
=================
 
This directory contains "news fragments" which are small, structured text files that contain information about changes or updates that will be included in the release notes. 
These fragments are used to automatically generate changelogs or release notes.
They can be written as restructured text format or plain text.

Each file should be named like ``<JIRA TICKET>.<TYPE>.rst``.
Note we adopted the ``rst`` format, the same used for documentation throught the project.

For "package level" changes (e.g. not component interface updates) the ``<TYPE>`` should be one of:

* ``feature``: A new feature
* ``bugfix``: A bug fix.
* ``perf``: A performance enhancement.
* ``doc``: A documentation improvement.
* ``removal``: A deprecation or removal of API.
* ``misc``: Other minor changes and/or additions

For interface changes the ``<TYPE>`` should be the name of the CSC in lowercase and the file should be created in the ``interface_changes/`` directory.

For example, if you are adding a new feature to the ts-xml python library under ticket DM-12345, you would create a file named ``DM-12345.feature.rst`` in this directory.
However, if you are updating the xml file for a component, say the ``ATAOS``, you would use ``doc/news/interface_changes/DM-12345.ataos.rst``.
If you are updating more than one CSC interface in the same ticket, you should create one individual file for each CSC following the format above.

If you have ``towncrier`` installed in your environment you can use:

.. code-block:: bash

   $ towncrier create <JIRA_TICKET>.<TYPE>.rst

for package level changes or,

.. code-block:: bash

   $ towncrier create interface_changes/<JIRA_TICKET>.<TYPE>.rst

for interface changes.

Each developer now has to create the news fragments for the changes they have made on their own branches, instead of adding them to the release notes directly.
The news fragments are then automatically integrated into the release notes by ``towncrier``.
This is done only at release time by the person in charge of the release and should not be done by developers/contributors when making their changes.

You can test how the content will be integrated into the release notes by running ``towncrier build --draft --version=vX.Y.Z``. 
Note that you have to run it from the root repository directory (i.e. the ``ts_xml``).

In order to update the release notes file for real, the person responsible for releasing the package should run:

.. code-block:: bash

   $ towncrier build --version=vX.Y.Z


.. note::

   When running towncrier to build the changelog, you may be prompted to confirm the deletion of fragments. 
   Make sure the news fragments are deleted whenever you make a release.

Note that ``towncrier`` can be installed from PyPI or conda-forge.
However, you do not need to install it to create a news fragment, only if you are doing the release.

