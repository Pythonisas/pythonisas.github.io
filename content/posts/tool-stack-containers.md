+++
title = "My Cybersecurity Tools Stack: Containers"
date = 2026-01-12T05:46:00-06:00
publishDate = 2026-01-12
draft = false
+++

## Portable, Reusable Containers. {#portable-reusable-containers-dot}

I enjoy creating a bunch of containers for various uses. The best part is I can create a container to fit my workflow. So my tool stack become malleable and manageable. I can create, rebuild, and destroy containers as my needs require. Granted disk space and time are always a concern. But I resolve that by being intentional with my tool stack.


## Day to Day Toolbox Container {#day-to-day-toolbox-container}

I use Fedora Linux as my workstation OS on a daily basis. Fedora has a cool project called **Toolbx** (Toolbox) built-in. Think of it as a tightly integrated Podman container on the Fedora host. Or if you come from the Microsoft world, think of it as WSL (but better 🤓). Here's the `Containerfile` to create my day to day Toolbx container.

```cfg
# Start from the official Fedora Toolbox Image
FROM registry.fedoraproject.org/fedora-toolbox:42

# Add Microsoft Powershell Repo
RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc && \
    curl -s https://packages.microsoft.com/config/rhel/9/prod.repo | tee /etc/yum.repos.d/microsoft.repo

# Install All Tools
RUN dnf --assumeyes install \
    nmap \
    telnet \
    wireshark-cli \
    powershell \
    nc \
    bind-utils \
    yara && \
    dnf clean all

RUN dnf clean all

# Ensure the image is recognized by Toolbx
LABEL com.github.containers.toolbox="true"
```


## Tools Stack Breakdown {#tools-stack-breakdown}

In this container I use the following tools:

-   NMAP
-   telnet
-   wireshark-cli (tshark)
-   Powershell
-   NetCat
-   Yara
-   Dig
-   TCPDump

Some of these tools are obvious like NMAP. Others are tailored for my day to day workflow. For example I include Yara and Powershell. Yara I like to keep in the container in case I decide to do some threat hunting. And Powershell is always handy when working on Windows system. Though I will say the Linux version of Powershell cannot do any type of `PSRemoting`.


## Conclusion {#conclusion}

So this is my tool stack for my **Toolbx** container. I write another blog post on how exactly I create and use this container. But for the biggest advantage of using this container is I can use it across Fedora installation. And it will be the same and familiar every time.


### Thank You {#thank-you}

> If you enjoyed or found any of the content on my site helpful, you can buy me a cup of coffee or send some bitcoin  ⚡ so I can continue to bring you amazing content for free!


#### You can Buy Me A Coffee {#you-can-buy-me-a-coffee}

{{< figure src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" link="https://www.buymeacoffee.com/eduardorobles" >}}


#### Tip with some Sats {#tip-with-some-sats}

[Tip Some Sats ⚡](https://getalby.com/p/tacosandlinux)
