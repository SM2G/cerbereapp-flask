import os
import cerbereapp
import unittest
import tempfile

class CerbereappTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, cerbereapp.app.config['DATABASE'] = tempfile.mkstemp()
        cerbereapp.app.config['TESTING'] = True
        self.app = cerbereapp.app.test_client()
        cerbereapp.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(cerbereapp.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
