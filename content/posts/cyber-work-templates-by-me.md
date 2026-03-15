+++
title = "Cyber Work Templates by Me!"
author = ["fenix"]
date = 2023-10-22T09:08:00+02:00
publishDate = 2023-10-22
draft = true
+++

## The obvious approach {#the-obvious-approach}

I use Emacs + Org-mode for my note-taking workflow as a Cybersecurity Analyst. Emacs is my geeky cred at my job, plus it is genuinely useful. So one day when working on taking some repetitive notes on an incident I had a bright idea. Why don't I just create a few templates that speed up my workflow?

-   A demonstration of my workflow for capturing notes on an incident
    ```text
    Incident --> Get Data --> Investigation --> Capture Templates --> Notes
    ```


## Expanding the approach {#expanding-the-approach}

Once I became comfortable with the approach of my capture templates, I expanded them to use the full power of Emacs and Org-mode! I began integrating Org-babel into my workflow. I use a Window 10 PC for my day job and I have WSL2 for all my Linux needs. Furthermore, I can call WSL from a regular shell (by default it calls the Windows Command Prompt) in Emacs. Org-babel does the work of putting the results in my notes. If this sounds familiar to you `#Emacs` nerds, well it's the concept of [Literate Devops](https://howardism.org/Technical/Emacs/literate-devops.html) by Howard Abrams. I as many others was inspired by the work of Howard Abrams and decided to incorporate their ideas into my workflow. It's a little weird to use these tools in a Windows environment, but hey it works ¯\\_(ツ)\_/¯.

> Here I am explaining one of my weird workflows.
>
> <https://emacs.ch/@tacosandlinux/111108755456994431>


## The templates and beyond {#the-templates-and-beyond}

So I put up my templates on [Github](https://github.com/eduardo-robles/cyber-work-templates) and licensed them under `CC BY-SA 4.0`. I will continue working on them and updating them as needed. At the time of writing this blog post, I move my note-taking workflow to [Org Roam](https://www.orgroam.com/) and I will be tweaking the templates to better fit that workflow. But I plan on creating a different set of templates, I do change them.

I mentioned Literate Devops earlier and while my workflow isn't "Devops" but it is "Literate". It's more like _Literate Pentesting_ which is very useful for me. I am not the first one to try this idea for Pentesting. [Michael Taggart](https://github.com/mttaggart) and [@HuskyHacks](https://github.com/HuskyHacks) have the really cool project [Blue Jupyter](https://github.com/mttaggart/blue-jupyter). They take the Jupyter Notebooks and apply them to Blue Team work.

So check out and fork my templates on github! Happy Hacking!

<https://github.com/eduardo-robles/cyber-work-templates>
