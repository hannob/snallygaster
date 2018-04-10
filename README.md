# snallygaster
Tool to scan for secret files on HTTP servers

what?
=====

snallygaster is a tool that looks for files accessible on web servers that shouldn't be public
and can pose a security risk.

Typical examples include publicly accessible git repositories, backup files potentially containing
passwords or database dumps. In addition it contains a few checks for other security vulnerabilities.

As an introduction to these kinds of issues you may want to watch this talk:
* [Attacking with HTTP Requests](https://www.youtube.com/watch?v=Bppr9rbmwz4)

author
======

snallygaster is developed and maintained by [Hanno Böck](https://hboeck.de/).
