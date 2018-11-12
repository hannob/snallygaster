# snallygaster

[![Rawsec's CyberSecurity Inventory](https://inventory.rawsec.ml/img/badges/Rawsec-inventoried-FF5050_flat.svg)](https://inventory.rawsec.ml/tools.html#snallygaster)
[![PyPI version](https://badge.fury.io/py/snallygaster.svg)](https://badge.fury.io/py/snallygaster)
[![GitHub version](https://badge.fury.io/gh/hannob%2Fsnallygaster.svg)](https://badge.fury.io/gh/hannob%2Fsnallygaster)
[![GitHub issues](https://img.shields.io/github/issues/hannob/snallygaster.svg)](https://github.com/hannob/snallygaster/issues)
[![GitHub forks](https://img.shields.io/github/forks/hannob/snallygaster.svg)](https://github.com/hannob/snallygaster/network)
[![GitHub stars](https://img.shields.io/github/stars/hannob/snallygaster.svg)](https://github.com/hannob/snallygaster/stargazers)
[![GitHub license](https://img.shields.io/github/license/hannob/snallygaster.svg)](https://github.com/hannob/snallygaster/blob/master/LICENSE)

Tool to scan for secret files on HTTP servers

what?
=====

snallygaster is a tool that looks for files accessible on web servers that shouldn't be public
and can pose a security risk.

Typical examples include publicly accessible git repositories, backup files potentially containing
passwords or database dumps. In addition it contains a few checks for other security vulnerabilities.

As an introduction to these kinds of issues you may want to watch this talk:
* [Attacking with HTTP Requests](https://www.youtube.com/watch?v=Bppr9rbmwz4)

See the [TESTS.md](TESTS.md) file for an overview of all tests and links to further information
about the issues.

install
=======

snallygaster is available [via pypi](https://pypi.python.org/pypi/snallygaster):

```
pip3 install snallygaster
```

It's a simple python 3 script, so you can just download the file "snallygaster"
and execute it. Dependencies are urllib3, beautifulsoup4 and dnspython.

faq
===

Q: I want to contribute / send a patch / a pull request!

A: That's great, but please read the [CONTRIBUTIONS.md](CONTRIBUTIONS.md) file.

Q: What's that name?

A: [Snallygaster](https://en.wikipedia.org/wiki/Snallygaster) is the name of a dragon that
according to some legends was seen in Maryland and other parts of the US. There's no particular
backstory why this tool got named this way, other than that I was looking for a fun and
interesting name.

I thought a name of some mythical creature would be nice, but most of those had the problem
that I would have had name collisions with other software. Checking the list of dragons on
Wikipedia I learned about the Snallygaster. The name sounded funny, the idea that there are
dragon legends in the US interesting and I found no other piece of software with that name.

credit and thanks
=================

* Thanks to Tim Philipp Schäfers and Sebastian Neef from the
  [Internetwache](https://www.internetwache.org/) for plenty of ideas about things to look
  for.
* Thanks to [Craig Young](https://secur3.us/) for many discussions during the
  development of this script.
* Thanks to [Sebastian Pipping](https://blog.hartwork.org/) for some help with Python
  programming during the development.
* Thanks to the organizers of Bornhack, Driving IT, SEC-T and the Rights and Freedom track at
  34C3 for letting me present this work.

author
======

snallygaster is developed and maintained by [Hanno Böck](https://hboeck.de/).
