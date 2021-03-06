**To add a user to an IAM group**

The following ``add-user-to-group`` commmand adds an IAM user named ``Bob`` to the IAM group named ``Admins``::

  aws iam add-user-to-group --user-name Bob --group-name Admins

Output::

  {
      "ResponseMetadata": {
          "RequestId": "b9cd3e32-4a54-11e2-8110-65075b2814da"
      }
  }    

For more information, see `Adding Users to and Removing Users from a Group`_ in the *Using IAM* guide.

.. _Adding Users to and Removing Users from a Group: http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_AddOrRemoveUsersFromGroup.html

