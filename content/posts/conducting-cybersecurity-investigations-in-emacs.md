+++
title = "Conducting Cybersecurity Investigations in Emacs"
author = ["fenix"]
date = 2023-11-05T20:24:00+01:00
publishDate = 2023-11-05
draft = true
+++

## <span class="org-todo done DONE">DONE</span> Emacs + Orgmode + Cybersecurity = Winning {#emacs-plus-orgmode-plus-cybersecurity-winning}

I work as a Cybersecurity Analyst and I use Emacs as my primary note taking application. Naturally I have developed some techniques and writing practices around my work and the use of Emacs aids in the process. I think the power of Emacs and Orgmode are a winning combination for the type of work I do. So let me share with you a some of the templates I created that help me in getting work done!


## The _Investigation_ Template {#the-investigation-template}

Recently, I published my [templates](https://github.com/eduardo-robles/cyber-work-templates) on Github. Let's take a look at my _Investigations_ template.


### Creating notes on investigations {#creating-notes-on-investigations}

```text
#+TITLE:
#+AUTHOR:
#+EMAIL:

 * Investigations
 * * IN-PROGRESS Investigation#: Suspicious Powershell Command  Date Created: 20230101
:properties:
:export_file_name: 20230101_investigation_suspciouspowershell
:end:
```

Here I am laying out the main information about this document. I set a title, author, and email address. I also include information about the date it was created and what the status of the to-do item is. In the `properties` drawer, I include an `export_file_name` section, so I can carefully curate my export to HTML or whatever I want.


### The meat and bones {#the-meat-and-bones}

```text
 * * * Vendor
Super Duper Cybers Corps.
 *** Title
Suspicious Powershell Command Executed by Finance Department
 *** Assigned:
Eduardo Robles
 *** Contacts
- Cyber Team
- Eduardo Robles
 *** Description
Our IDR logged an a suspicious Powershell command executed from the Finance department.
 *** Questions
1. Was this an intentional execution?
2. What is the purpose of the Powershell command?
3. Did anyone verify with I.T department regarding the Powershell command in question?
 *** Solutions [%]
- [ ] Investigate the origin of the Powershell command
- [ ] Speak with employee who's work station is in question and their supervisor
- [ ] Flag the Powershell command as suspicious
 *** Notes
:LOGBOOK:
:END:
 *** Debug/Troubleshooting Logs
:LOGBOOK:
:END:
 *** Email/Chat Logs
:LOGBOOK:

:END:
```

In this portion, I include as many details as I can about the ongoing investigation. These notes usually end up as a report that I hand into upper management. So I have to be as descriptive as I can be.

I tend to use `org-contacts` in my _Contacts_ section to make it easier to show email address when I export my content to HTML. In the _Solutions_ section I include `org-checkboxes` so I can keep track of work. In my _Notes_, _Debug+Troubleshooting Logs_, and _Email+Chat Logs_ sections I take advantage of `LOGBOOK` to create timestamped notes of events.


## It's all about writing it down {#it-s-all-about-writing-it-down}

Alerts are constant in my line of work. So it's easy to get distracted and disorganized with all the noise. Developing a practice of consistently writing out notes is key to finding calm in all the noise. I developed this template after a lot of trial and error. And I am still working on them but for now they work for me. The best part is that they modular. Use what works and add or remove what doesn't.
