TESTS
=====

An overview of tests provided by snallygaster:

Default tests
=============

These tests are enabled by default and usually output information that directly leads to
potential vulnerabilities.


lfm_php
-------

This checks for Lazy File Manager, a one-file php script that allows arbitrary file operations.
It is often placed on compromised webpages.


idea
----

Configuration file for JetBrains, can contain passwords.


symfony_databases_yml
----------------------

Database configuration file (databases.yml) used by older versions of Symfony. These aren't
supposed to be stored within the web root, but sometimes they are.


rails_database_yml
------------------

Database configuration file (database.yml) used by Ruby on Rails. Misconfigurations can cause
these to be readable.


git_dir
-------

When deploying web pages with a Git repository the .git directory may end up being publicly
readable. This allows downloading the full repository.

* [Internetwache: Don't publicly expose .git or how we downloaded your website's sourcecode](https://en.internetwache.org/dont-publicly-expose-git-or-how-we-downloaded-your-websites-sourcecode-an-analysis-of-alexas-1m-28-07-2015/)
* [Golem.de: Riskante Git-Verzeichnisse](https://www.golem.de/news/websicherheit-riskante-git-verzeichnisse-1507-115476.html)
* [GitTools - scripts to download .git directories](https://github.com/internetwache/GitTools)
* [git-dumper - script to download .git dir, faster than GitTools](https://github.com/arthaud/git-dumper)


svn_dir
-------

Identical to git_dir issue, just with Subversion instead of Git.

* [svnscaper - script to download .svn directories](https://github.com/hannob/svnscraper)


apache_server_status
--------------------

Apache server-status pages. These can contain visitor URLs and IP addresses of visitors.

* [Sucuri: Popular sites with Apache server-status enabled](https://blog.sucuri.net/2012/10/popular-sites-with-apache-server-status-enabled.html)


coredump
--------

Crashing processes on Linux and other unix systems can leave a memory dump file named "core"
that may leak information like passwords.

* [Hanno's Blog: Don't leave Coredumps on Web Servers](https://blog.hboeck.de/archives/887-Dont-leave-Coredumps-on-Web-Servers.html)


sftp_config
-----------

Configuration file from the FTP client sublime FTP (sftp-config.json). It turns out sometimes people
accidentally upload the configuration file of their FTP client, including credentials for their web space.

* [Sucuri: SFTP/FTP Password Exposure via sftp-config.json](https://blog.sucuri.net/2012/11/psa-sftpftp-password-exposure-via-sftp-config-json.html)


wsftp_ini
---------

Similar to sftp_config, but for WS_FTP.


filezilla_xml
-------------

Similar to sftp_config, but for FileZilla.


winscp_ini
----------

Similar to sftp_config, but for WinSCP.


ds_store
--------

The Apple OS X file manager Finder creates these files. They may leak directory and file names.

* [Internetwache: Scanning the Alexa Top 1M for .DS_Store files](https://en.internetwache.org/scanning-the-alexa-top-1m-for-ds-store-files-12-03-2018/)
* [ds_stope_exp (recursively download .DS_Store files)](https://github.com/lijiejie/ds_store_exp)

php_cs_cache
------------

Cache file from php-cs-checker, a codingstyle checker for PHP. This effectively leaks a directory
listing of PHP files.


backupfiles
-----------

Backup files and other leftovers from editors. Many editors create files with a ~ or .bak extension
when overwriting a previous version. VIM creates swap files of the scheme .[filename].swp. On crashes
EMACS creates #[filename]#.
All of these are particularly problematic in combination with PHP, as a file that may contain
secrets will end up on the webspace without a .php extension and thus won't be parsed.

* [FEROSS: 1% of CMS-Powered Sites Expose Their Database Passwords](https://feross.org/cmsploit/)


backup_archive
--------------

Complete or partial backups of servers are sometimes left online. This test checks for common names
like backup.tar.gz.

* [Golem.de: Datenlecks durch backup.zip](https://www.golem.de/news/websicherheit-datenlecks-durch-backup-zip-1904-140564.html)


deadjoe
-------

The editor JOE creates a file DEADJOE on crashes, which contains content of the currently edited files.
Similar to backupfiles.


sql_dump
--------

This checks for common names of SQL database dumps. These can lead to massive database leaks.

* [Zeit Online: How 2,000 Unsecured Databases Landed on the Internet](http://www.zeit.de/digital/datenschutz/2017-07/customer-data-how-2000-unsecured-databases-landed-online)


bitcoin_wallet
--------------

This scans for bitcoin wallets (wallet.dat) left on servers. While this is rare, obviously leaking
those can come at a high cost.


drupal_backup_migrate
---------------------

The Drupal backup_migrate plugin stores backups of the CMS database in the web folder.
Access is prevented with an Apache .htaccess file, but that does not work on other web servers.


magento_config
--------------

Magento is a PHP web store that saves its config (including database credentials) in an XML file
called "local.xml".
Access is prevented with an Apache .htaccess file, but that does not work on other web servers.

* [oss-security: Magento leaking of config file local.xml](http://seclists.org/oss-sec/2017/q4/141)


xaa
---

xaa files are the output of the "split" command line tool on Unix systems. It's used to split large
files. As large files often contain lots of data these may lead to large leaks (similar to sql_dump).


optionsbleed
------------

A test for the Optionsbleed vulnerability, in which Apache corrupts the "Allow" header in a reply
to an HTTP OPTIONS request.

* [Fuzzing Project: Optionsbleed - HTTP OPTIONS method can leak Apache's server memory](https://blog.fuzzing-project.org/60-Optionsbleed-HTTP-OPTIONS-method-can-leak-Apaches-server-memory.html)


privatekey
----------

Checks for private keys, usually belonging to TLS/X.509 certificates.

* [Golem.de: Private Keys on Web Servers](https://www.golem.de/news/https-private-keys-on-web-servers-1707-128862.html)


sshkey
------

Similar to the privatekey check this looks for SSH private keys on web servers.


dotenv
------

This looks for Laravel ".env" files that may contain database credentials.


invalidsrc
----------

This checks all src-references on a webpage's HTML and looks for inaccessible references.
These may indicate domain takeover vulnerabilities.
This test produces warnings quite often, though many of them are harmless: References to
deleted files or simply syntax errors in URLs.

* [Hanno's Blog: Abandoned Domain Takeover as a Web Security Risk](https://blog.hboeck.de/archives/889-Abandoned-Domain-Takeover-as-a-Web-Security-Risk.html)


ilias_defaultpw
---------------

This checks installations of the Ilias e-learning software for the presence of a default
username/password (root/homer).
Ilias was involved in the 2018 hack of the German government, though it's unclear what
vulnerability was used.

* [Golem.de: Hack on German Government via E-Learning Software Ilias](https://www.golem.de/news/government-hack-hack-on-german-government-via-e-learning-software-ilias-1803-133231.html)


cgiecho
-------

The cgiecho tool is part of the unmaintained software cgiemail. It contains a vulnerability
where it allows leaking arbitrary files from the web root if they contain any guessable
string in square brackets (e.g. ['password']).

* [Cgiemail - Source Code Disclosure/Local File Inclusion Exploit](https://github.com/finbar-crago/cgiemail-exploit)


phpunit_eval
------------

Tests for a remote code execution vulnerability in a script shipped with older versions of phpunit
that will simply pass the POST data to PHP's eval.

* [CVE-2017-9841 RCE vulnerability in phpunit](https://web.archive.org/web/20181213234925/http://phpunit.vulnbusters.com/)


acmereflect
-----------

Tests if there's an ACME API endpoint that reflects content and can be abused for XSS.
Outputs acmereflect_html if the API also reflects HTML code, acmereflect_html_sniff if it outputs
HTML code and does MIME sniffing.

* [XSS using quirky implementations of ACME http-01](https://labs.detectify.com/2018/09/04/xss-using-quirky-implementations-of-acme-http-01/)


drupaldb
--------

Misconfigured Drupal installations may expose their SQLite database.


phpwarnings
-----------

Tries to trigger a PHP warning with an invalid PHPSESSID.


adminer
-------

adminer is a one file php database frontend. (I may consider changing this to an info test,
but for now I believe most of these are not intentionally publicly available, though they
often have login forms.)

* [Adminer leaks passwords; Magecart hackers rejoice](https://gwillem.gitlab.io/2019/01/17/adminer-4.6.2-file-disclosure-vulnerability/)


elmah
-----

Public error console for the ELMAH library. This can contain cookies and other sensitive
pieces of information, it shouldn't be accessible from outside.

* [ASP.NET session hijacking with Google and ELMAH](https://www.troyhunt.com/aspnet-session-hijacking-with-google/)


citrix_rce
----------

Check for the Citrix CVE-2019-19781 RCE / directory traversal.

* [Vulnerability in Citrix Application Delivery Controller and Citrix Gateway](https://support.citrix.com/article/CTX267027)
* [Citrix NetScaler CVE-2019-19781: What You Need to Know (Tripwire VERT)](https://www.tripwire.com/state-of-security/vert/citrix-netscaler-cve-2019-19781-what-you-need-to-know/)


installer
---------

Search for unused installers of common PHP web applications.
In most cases a stale installer can be used for code execution by
installing the application and uploading a plugin.


wpsubdir
--------

Search for unused Wordpress installers in /wordpress/ subdir.


axfr
----

Checks if name servers answer to AXFR zone transfer requests. These are usually never intended
to be publicly accessible.

* [Internetwache: Scanning Alexa's Top 1M for AXFR](https://en.internetwache.org/scanning-alexas-top-1m-for-axfr-29-03-2015/)
* [US-CERT: DNS Zone Transfer AXFR Requests May Leak Domain Information](https://www.us-cert.gov/ncas/alerts/TA15-103A)
* [D. J. Bernstein: How the AXFR protocol works](https://cr.yp.to/djbdns/axfr-notes.html)


openmonit
---------

Check for Monit web interface with default username and password.

* [Monit: Configuration file with default username/password combination (admin/monit)](https://bitbucket.org/tildeslash/monit/issues/881/configuration-file-with-default-username)


Info tests
==========

These tests are enabled with the "-i" parameter. They output information about a site that may be
valuable for analysis, but does not directly indicate a security problem.


drupal
------

Checks for the presence of the Drupal CMS and outputs the version.


wordpress
---------

Check for the presence of Wordpress and output version.


mailman
-------

Check for mailman and output version.


composer
--------

Check for composer.json/composer.lock files. Can be checked with the
[Symfony security check](https://symfony.com/doc/current/setup.html#security-checker)
afterwards.
