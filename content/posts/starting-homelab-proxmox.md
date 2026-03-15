+++
title = "Starting a Homelab with Proxmox"
author = ["fenix"]
publishDate = 2021-07-04
draft = true
+++

The Beginning

So if you hadn't heard of the idea of a "homelab", let me give you the quick run down of what is a "homelab". Basically, a homelab is a collection of technologies (hardware and software) that you install, maintain, and configure in your home. Imagine a datacenter in your home or an electronics lab can also be a homelab. At the heart of the homelab movement is the idea of tinkering and learning.

Inspired by the idea of tinkering and learning I went down the path of building my own homelab. Luckily you don't need a lot to started, older hardware can be a great start for beginners. That's were my trusty old Dell Xeon workstation comes in. I was gifted this Dell Xeon workstation from a former client and I used it as a Ubuntu workstation for many years. It is a great machine and despite its age work like a champ. Unfortunately, it's loud and does not meet the "Wife Approval Factor". To keep my wife and to start a new journey for this Dell, I decided to turn into my Proxmox machine!
The Homelab

Now what is Proxmox?

Proxmox is Type 1 Hypervisor that you can install on your own hardware. It allows you to run multiple Virtual Machines and Linux Containers (LXC). This is how I'm going be able to run various technologies in my home. Proxmox is a great hypervisor, it's user friendly and built on a stable Debian base. I'm quite comfortable on Debian based distros, so going with Proxmox was a no-brainer.
The Services

In order to stay a bit organized I made a list of services/technologies I wanted to run on my homelab. Below are the services I currently have installed.

> File server
> Plex server
> Syncthing
> Git server
> Home Assistant
> GNS3 VM
