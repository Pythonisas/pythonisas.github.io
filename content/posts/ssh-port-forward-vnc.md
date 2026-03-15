+++
title = "SSH Port Forward a VNC Connection"
author = ["fenix"]
publishDate = 2020-02-05
draft = true
+++

Recently I wanted to access a Virtual Machine I had created on my desktop from my laptop. I had access to the desktop via SSH but I wanted access to the virtual machine. To make things more interesting I wanted to access the VM(virtual machine) via a graphical interface.

So I figured out that I could use SSH to "port forward" the VNC connection from the desktop to my laptop. It's actually very easy and only requires a few basic SSH commands. All you have to know before hand is the IP addresses and ports of the application and what port you want to connect to locally.

Definitions:

pc-1: Is the computer you are connecting from, in this case the laptop.

pc-2: Is the computer you are connecting to, in this case the desktop with the VM.

So I use KVM to run the VM, so to get the VNC port from the running VM do the following.

```sh
sudo virsh dumpxml NameOfVM | grep vnc
```

You should see an output like this one.

> &lt;graphics type='vnc' port='5901' autoport='yes' listen='127.0.0.1'&gt;

This tells you that KVM is running vnc on port 5901 on address 127.0.0.1 (localhost) for this virtual machine. Now it's time to connect to the virtual machine from pc-1.

In pc-1 run the following command to create an SSH tunnel that port forward the VNC connection.

```sh
ssh user@pc-2 -L 5901:127.0.0.1:5901
```

What is is command doing?

> ssh user@pc-2 is establishing the SSH connection to pc-2 with the user "user". In your case, the user and IP address might be different e.g batman@10.10.0.1.
> -L 5901:127.0.0.1:5901 is telling SSH agent to create a tunnel using local port 5901 and bind it to the remote machine address 127.0.0.1 on port 5901. The address on the remote machine might be different so that's why we ran the virsh command to find it.

Now that the SSH tunnel is established connect to the VM via VNC. You can use any remote viewer software like Remmina, TightVNC, or even Remote Viewer (part of Virtual Machine Viewer). Simply connect with the following parameters.

```sh
vnc://localhost:5901
```

And the VNC connection should open up and start working. You can do everything you could locally via a remote VNC connection. Once you are done simply close the VNC connection and exit the SSH session.

In this tutorial I showed how to this in KVM but VirtualBox and VMware have their own methods of doing this. Simply search for "headless" virtual machine for each to find out how to accomplish the same procedure.

Congrats, you are now running a headless VM with a secure connection. SSH is cool tool that can do alot and if you combine it with other tools you can accomplish even more.
