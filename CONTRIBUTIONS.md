You want to contribute to snallygaster? Fix a bug or add a new test? Great!

But please consider a few things:

Avoid unreasonable Pull Requests
================================

I have seen pull requests of the form: "I fixed this little bug in line 50. I also changed your
coding style all over the place, because I don't like it. Oh, and I added some newlines here
and there for no reason whatsoever. All of that in a single commit."

Of course I'm exaggerating here, but not much. I often see pull requests that are incredibly
painful to review.

A pull request should change a single thing. Don't mix unrelated changes in one pull request.
If you want to make larger changes consider discussing the changes before you start working
on them.


Avoid complexity
================

I've seen patches that added more lines of code, made the code slower and less readable and
provided no improvement.

As a rule of thumb: If your pull request adds more lines than it removes you need to have
a reason for that. "This is how this is usually done" and "this makes the code follow coding
paradigm XYZ" are not good reasons.


Coding style
============

The code complies with [pycodestyle](https://pypi.python.org/pypi/pycodestyle), except for
the "overly long lines" rule (E501), as forcing shorter lines often makes the code less
readable. We also need to disable W503 to comply with the latest PEP 8
[recommendation for the placement of binary operators](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator).

The code should produce no warnings with this command:

```
pycodestyle --ignore=E501,W503 snallygaster
```


New Tests
=========

If you consider adding new tests please consider that there should be a reasonable balance
between impact, prevalence of the issue and cost (time) of the test.

This is best illustrated with a few examples:

* The ds_store test often has a very low impact, but it is extremely common (prevalence) and
  only a single HTTP request.
* The bitcoin_wallet test rarely finds anything, but the impact is very high and the test is
  cheap.
* The sql_dump test is relatively slow, as it tests many filename variations, but the impact
  can be very high (leak of large amounts of private data) and it happens quite often.

A test with a low impact that rarely finds anything and is very slow is unlikely to get
accepted. Consider doing scans of the Alexa Top 1 Million to get a rough idea of how
prevalent an issue is.
