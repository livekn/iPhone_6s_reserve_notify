#Hong Kong Apple Store iPhone 6s/6s plus reserve checker (also support other countries)

It will check Hong Kong iPhone reserve for you every 10s (if you need other countries, edit config.py).
When your phone is available, it will send you a push notification using pushbullet

Before you go, install pushbullet client for python
```
pip install pushbullet.py
```

Install [pushbullet][1] on your iPhone/Android/Mac/PC/Chrome.

Edit config.py, insert your own pushbullet [access token][2].

To use it:
```
python main.py
```

When your iPhone is available, I will send you a push.

PS: if you have InsecurePlatformWarning, solution is [here][3].

[1]: https://www.pushbullet.com
[2]: https://www.pushbullet.com/#settings/account
[3]: http://stackoverflow.com/a/29202163