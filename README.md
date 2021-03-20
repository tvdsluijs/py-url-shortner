# Python Flask URL Shortner

> It shortens URL's in a Python Flask website

![GitHub](https://img.shields.io/github/license/tvdsluijs/py-url-shortner)

# Python URL Shortner

I was wondered in how much time I could build a URL shortner. Long long long long long ago I build a [URL shortner in PHP](https://github.com/tvdsluijs/snurl.eu).

It was a massive hit but the servers died on it because of the high traffic and I just could not affort faster servers and more bandwidth.

I think it took me a week or 2 to build the PHP version of the URL shortner. I'm all into Python the last few years and I wanted to see how long it would take me to build a version in Python. Just the most raw version of it. No bling bling webpage, just a simpel working version.

I build this under 45 minutes. Could have been faster, but my cat needed some petting every now and then, she is quite coercive 😺

## Installation

You need to librairies for this to work.

`pip install Flask`

`pip install validators`

I would suggest to install and use these in an python sandboxed environment.

## Usage example

For the first usage you need the database (you can reuse mine or throw mine away 'short.db') and create a new database

`python create_db.py`

You will get an error if my 'short.db' is still there. Delete it first if you don't want to use it.

Then!

`python py-url-shortner.py`

This will run the Flask websetup on [127.0.0.1:5000](http://127.0.0.1:5000/)

You got it running!

## Release History

- 0.0.1
  - First version!

## Backlog items

- More beautiful frontend
- API for shortening urls
- Weekly mail with statistics
- Google connection for fraud signaling

## Meta

iTheo van der Sluijs – [@itheo_nl](https://twitter.com/itheo_nl) – theo@vandersluijs.nl

[itheo.nl](https://itheo.nl)

[vandersluijs.nl](https://vandersluijs.nl)

[https://github.com/tvdsluijs/](https://github.com/tvdsluijs/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
