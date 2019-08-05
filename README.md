# Reply bot

The simple reply bot for some courses. 
The bot helps to collect messages of users in one chat for answering. 
Development on Python.

---

For starting:

> + Create file 'config.py' in src folder
> + Created certificate and private key in root folder
> + Enter 'python src/main.py' in terminal (from root folder)

---

Example of config.py file:

```
TOKEN = 'some token of a bot'
CHAT = '-000000000'
WEB_HOOK_HOST = '111.22.33.44'
WEB_HOOK_PORT = 8080
WEB_HOOK_LISTEN = '0.0.0.0'
WEB_HOOK_SSL_CERT = '../public_cert.pem'
WEB_HOOK_SSL_PRIV = '../private_key.pem'

admins_id = ['000000000']
```