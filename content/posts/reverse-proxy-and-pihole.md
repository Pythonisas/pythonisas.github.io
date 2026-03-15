+++
title = "Using a Reverse Proxy and Pi-Hole"
author = ["fenix"]
date = 2022-10-20T06:37:00+02:00
publishDate = 2022-10-20
draft = true
+++

I recently setup NGINX Proxy Manager to help manage all of my self-hosted services. How did I do this? I installed NGINX Proxy Manager in a LXC container in my Proxmox server. I then configured several of my services to route to their respective IP addresses and ports. In NGINX Proxy Manager you can assign local domain name to your services. I chose to go with something simple like `example.home`. Once I finished configuring NGINX Proxy Manager I moved over to configure my Pi-Hole server. I run the latest version of Pi-Hole on a Raspberry Pi 4 B+ which works fantastic. In my Pi-Hole I simply added some new DNS record to match my NGINX configurations.


## Example of my Pi-Hole DNSMASQ Settings {#example-of-my-pi-hole-dnsmasq-settings}


### A Record: `proxy.homeserver.home` --&gt; `10.0.11.1000` {#a-record-proxy-dot-homeserver-dot-home-10-dot-0-dot-11-dot-1000}


### CNAME Record: `proxmox.home` --&gt; `proxy.homeserver.home` {#cname-record-proxmox-dot-home-proxy-dot-homeserver-dot-home}


### CNAME Record: `plex.home` --&gt; `proxy.homeserver.home` {#cname-record-plex-dot-home-proxy-dot-homeserver-dot-home}

Since I am using Pi-Hole as my DNS server I need to have the custom domains I setup in NPM (NGINX Proxy Manager) to route traffic correctly. I start by setting up an `A Record` of my NPM custom domain to point to the IP of NPM. Doing so will ensure that all traffic that goes to that IP gets routed only to NPM. Any traffic that NPM then reads it can then route to the proper service. Next, I make CNAME  records of all the services I have running with custom domains. Now here I state that any request to my custom domains be routed to the A record of my NPM. The reason I need to do this is because traffic needs to route NPM so NPM can decide how to serve up the service. That after all is the job of a reverse proxy.

And that's it! Once I have all settings in place I can start using my custom domains on my local LAN. This make so much easier to reach my local services instead of memorizing IP addresses. In the future I look forward to setting up some local SSL certificates to secure my local custom domains with SSL.
