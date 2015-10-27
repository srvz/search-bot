# Search-bot

Search-bot can be considered as a google proxy. Sometimes when I need search something, but I don't like to turn on
vpn, so I wrote this tool for convinence. Also it can be used as a Wechat Official Accounts backend. 

## Support

Only tested on Python3.5

## how to

If you are familiar with frontend development, just checkout the `front` directory.

### create `weixin/config.py` (required)

Note, wechat encrypt mode not implemented.

```
appid = ''

appsecret = ''

wx_token = ''

wx_aeskey = ''
```

### On your own server

```
virtualenv -p `which python3.5` py3.5

source py3.5/bin/activate

pip install -r requirements.txt

export PRODUCTION=1 //turn off log

nohup python3.5 tornado_app 5678 &// default port 5080

```

Also if you'd like to use `supervisord` and `nginx`, you can reference to `supervisord.conf` and `nginx.conf`.


### On heroku (not tested, maybe works).

Note, one free heroku account only support one worker.

```
heroku create 

git push heroku master
```

### On openshift

```
*.rhcloud.com has already been fucked by GFW.
```

## LICENCE

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>
