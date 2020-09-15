# google_keep_exporter

This is a google keep API based ( https://github.com/kiwiz/gkeepapi ) Exporter which downloads all your google keep notes and stores then in a local file. You just need to enter your User Id and password and the data will be exported to the target file.


Dependency:

 `pip install gkeepapi`


To run, open directory and :

`python export.py`



If you encounter NeedBrowser error during login,

* You have to open the following link with lynx (an Internet text browser): https://accounts.google.com/b/0/DisplayUnlockCaptcha
* Authenticate with your google account credentials


