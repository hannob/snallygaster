# SPDX-License-Identifier: 0BSD

import http.server
import os
import ssl
import subprocess
import tempfile
import threading
import unittest

TESTDATA_REPO = "https://github.com/hannob/snallygaster-testdata"

TESTDATA = {"backup_archive": "[backup_archive] https://localhost:4443/backup.zip",
            "git_dir": "[git_dir] https://localhost:4443/.git/config",
            "deadjoe": "[deadjoe] https://localhost:4443/DEADJOE",
            "coredump": "[coredump] https://localhost:4443/core",
            "backupfiles": "[backupfiles] https://localhost:4443/index.php~",
            "ds_store": "[ds_store] https://localhost:4443/.DS_Store",
            "privatekey": "[privatekey_pkcs8] https://localhost:4443/server.key",
            "desktopini": "[desktopini] https://localhost:4443/desktop.ini",
            }


class TestScanTestdata(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("RUN_ONLINETESTS"),
                         "Not running online tests")
    def test_scan_testdata(self):
        tmp = tempfile.mkdtemp(prefix="testdata")
        if os.environ.get("TESTDATA_REPOSITORY"):
            os.symlink(os.environ.get("TESTDATA_REPOSITORY"),
                       tmp + "/testdata")
        else:
            subprocess.run(["git", "clone", "--depth=1",
                            TESTDATA_REPO,
                            tmp + "/testdata"],
                           check=True)

        olddir = os.getcwd()
        os.chdir(tmp + "/testdata")
        httpd = http.server.HTTPServer(("localhost", 4443), http.server.SimpleHTTPRequestHandler)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=tmp + "/testdata/testserver.pem")
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        t = threading.Thread(target=httpd.serve_forever)
        t.daemon = True
        t.start()

        for test, expected in TESTDATA.items():
            testrun = subprocess.run([olddir + "/snallygaster", "-t", test, "localhost:4443",
                                      "--nowww", "--nohttp"],
                                     stdout=subprocess.PIPE, check=True)
            output = testrun.stdout.decode("utf-8").rstrip()
            self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
