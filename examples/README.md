Example HOWTO
=============

The examples in this folder demonstrate various functionalities of the API, perimarily to retrieve various data from a running MediaWiki installation.

In order to run these examples "out of the box" you need to provide a valid configuration file. To do this create a copy of "constants.local.example.json" and name it "constants.local.json". Provide the following keys:

* `url`: (required) A valid URL that points to the MediaWiki root directory. This root directory is the directory that contains the file `index.php`.
* `user`: (required) The user name to use during login. (You don't need to provide a password.)
* `pwd`: (optional) The password for this user. (If you don't specify a password - because you might not want to store it for security reasons - you will be queried for the password on program start.)
* `someOtherUser`: (required) Some other user name for login. (Some examples require two separate user accounts.)
* `someOtherUserPwd`: (optional) The password for the other user. (If you don't specify a password - because you might not want to store it for security reasons - you will be queried for the password on program start.)








