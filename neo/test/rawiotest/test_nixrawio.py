import unittest
import os
import shutil
from tempfile import mkdtemp
from neo.rawio.nixrawio import NIXRawIO
from neo.test.rawiotest.common_rawio_test import BaseTestRawIO
from neo.test.iotest.test_nixio import NixIOTest
from neo.io.nixio import NixIO

try:
    import nixio as nix

    HAVE_NIX = True
except ImportError:
    HAVE_NIX = False


testfname = "nixrawio-1.5.nix"


@unittest.skipUnless(HAVE_NIX, "Requires NIX")
class TestNixRawIO(BaseTestRawIO, unittest.TestCase):
    rawioclass = NIXRawIO
    entities_to_test = [testfname]
    files_to_download = [testfname]


@unittest.skipUnless(HAVE_NIX, "Requires NIX")
class TestNixRawIOCustom(unittest.TestCase):

    nixfile = None
    nix_blocks = None

    @classmethod
    def setUpClass(cls):
        cls.tempdir = mkdtemp(prefix="nixiotest")
        cls.filename = os.path.join(cls.tempdir, "testnixio.nix")
        if HAVE_NIX:
            cls.nixfile = NixIOTest.create_full_nix_file(cls.filename)

    def setUp(self):
        self.io = NixIO(self.filename, "ro")

    @classmethod
    def tearDownClass(cls):
        if HAVE_NIX:
            cls.nixfile.close()
        shutil.rmtree(cls.tempdir)

    def tearDown(self):
        self.io.close()

    def test_full_read(self):
        pass


if __name__ == "__main__":
    unittest.main()
