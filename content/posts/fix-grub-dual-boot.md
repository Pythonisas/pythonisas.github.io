+++
title = "Fixing Grub on a Dual Boot"
author = ["fenix"]
publishDate = 2019-12-18
draft = true
+++

I recently decided to move my Ubuntu installation from my laptop to my desktop without having to reinstall. So basically all I wanted to do is move the SSD (which had Ubuntu 19.10 installed) in my laptop to my desktop. This process is not hard at all but in my case it was a little more complicated. I wanted to do a dual boot on my desktop computer with 2 different hard drives. One spinning disk hard drive will have a Windows 10 installation while the SSD from my laptop will have Ubuntu 19.10. Again I did not want to do any reinstall of Windows 10 or Ubuntu. So how can you accomplish this? Simple with the command update-grub.

First I removed the SSD in the laptop and installed it in my desktop. I ensured that it was on the first SATA port so it can be the first hard drive the system recognizes. Once installed I booted up the computer and Ubuntu booted up correctly. Ok, so now I knew Ubuntu worked fine on the desktop.

Next, I had to update grub inside of Ubuntu in order to add the Windows 10 disk to my boot order. Grub is actually pretty good at adding additional operating systems to the boot order. So turned off the computer ensured that my drives were in the correct SATA ports. After this step I ran into a small problem, Grub was not updating inside my Ubuntu installation. So I decided to boot into a Linux LiveUSB to help troubleshoot the errors.

Inside the LiveUSB Linux environment I used a chroot environment to reach my Ubuntu  19.10 installation. To do so simply follow these steps.

```sh
sudo mount /dev/sdaX /mnt

for i in /dev/ /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done

sudo chroot /mnt
```

Once in the chroot environment I ran update-grub and I still got an error. So I decided it would be best to simply reinstall grub. To do so simply run reinstall grub-pc (if you're on a efi system please use grub-efi-amd64). This command worked and prompted me to chose where I wanted to install grub. I chose on the main disk since this is where I wanted to have grub installed. Once that process was done, I rebooted the system and was prompted with a working grub boot screen with both operating systems showing up correctly.

Tip: If you want to customize your Grub boot screen you can do with the app Grub Customizer. Simply install it with sudo apt install grub-customizer. This allows you to add a background to Grub bootscreen, change the boot order, and much more.
