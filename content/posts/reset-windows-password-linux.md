+++
title = "Reset Windows Password with Linux"
author = ["fenix"]
publishDate = 2019-07-15
draft = true
+++

Ever needed to reset your Windows password but forgot to make a Windows Reset Password disk? If so, you can easily reset a Windows Users password with a Live Linux USB. Let's see just how easy it is to so.

If you don't a Live Linux USB go ahead an create one. This tutorial is Ubuntu based so any Ubuntu flavor will work. And you will need a working internet connection to download software.
Start the computer and boot into the Live Linux environment.
Once in the Live Linux environment make sure you connect to the internet and open a terminal.
You will need to install tool called chntpw. So ahead and run the following command to install chntpw apt-get install chntpw
Once installed you will have to mount the hard drive that has Windows installed. There are many ways of doing this but you can use the File Manager (Nautilus in Ubuntu) to make things easy.
Once you have the Windows Harddrive mounted go to the following directory _windowsHarddrive/Windows/System32/config_
Now that you are at the correct directory, right click and chose Open With
Terminal Here.
In the terminal simply type the following command to interact with chntpwsudo chntpw SAM
Now you are editing the Administrator user if you would like to edit another user use this command.sudo chntpw -u USERYOUWANTTOEDIT SAM
After you've chosen your user it's time to reset their password. Simply type 1 in ther User Edit Menu. And then chose y when prompted to Write hive
files
Then to quit type q and this will exit chntpw
Close the terminal and restart your computer making sure to remove the Live Linux USB.
You should boot into Windows desktop directly without any login. Be sure to add a new password!

Congratulations you have successfully reset your Windows with Linux! And that's it!
