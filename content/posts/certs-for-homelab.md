+++
title = "Certs for Homelab"
author = ["fenix"]
date = 2023-04-27T18:00:00+02:00
publishDate = 2023-04-27
draft = true
+++

I recently had the opportunity to add an `ssl` certificate in my homelab environment. It was really easy and only took one command in Linux. Once I created my `ssl` certificate all I had to do was upload it to NGINX Proxy Manager and have it serve it to my proxied sites.

You can use any other proxy manager such as Caddy but I had NGINX Proxy Manager in my homelab environment. Be sure to upload both the `.crt` and `.key` files.

Let's examine what the following commands does.

```bash
openssl req -newkey rsa:4096 -x509 -sha256 365 -nodes -out homessl.crt -keyout homessl.key
```

First `openssl req -newkey rsa:4096 -x509 -sha256 365` stating that we want openssl to create a new certificate using `rsa 4096` with type of `x509` a hash of `sha 256` for `365` days.

Then `-nodes -out homessl.crt -keyout homessl.key` is telling openssl that we want the cert file and a key file.

Once you run this command you should have 2 files on your system. In this example they would be `homessl.crt` and `homessl.key`. Those 2 files you simply upload to your proxy manager or cert authority of choice and you will have valid self-signed openssl certificates. If you are curious to learn more about OpenSSL you can always check out the manpages online at <https://www.openssl.org/docs/man3.0/man7/crypto.html>.
