import unittest, os, threading
from app.dame_photo import DamePhoto

class TddUrlThread(unittest.TestCase):
    def test_dame_photo_fetch_method_returns_correct_result(self):
        f = DamePhoto("https://avatars2.githubusercontent.com/u/1023217")
        f.start()
        f.join()
        self.assertEqual(f.url, "https://avatars2.githubusercontent.com/u/1023217")
        # self.assertEqual(f.title, "The GNU Operating System and the Free Software Movement")
        # self.assertEqual(len(f.hrefs)>1, True)

    def test_urlthread_fetch15_method_returns_correct_result(self):
        f = DamePhoto("https://avatars2.githubusercontent.com/u/1023217")
        f.start()
        f.join(timeout=15)
        self.assertEqual(f.url, "https://avatars2.githubusercontent.com/u/1023217")
        # self.assertEqual(f.title, "The GNU Operating System and the Free Software Movement")
        # self.assertEqual(len(f.hrefs)>1, True)
