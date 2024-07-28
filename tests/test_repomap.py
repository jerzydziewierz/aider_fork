import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from aider.repomap import RepoMap, should_ignore

class TestRepoMap(unittest.TestCase):
    def setUp(self):
        self.repo_map = RepoMap(root="/test/root")

    def test_should_ignore(self):
        with patch('pathlib.Path.exists', return_value=True), \
             patch('pathlib.Path.open', return_value=MagicMock()):
            # Test file that should be ignored
            self.assertTrue(should_ignore("/test/root/ignored.txt", "/test/root"))
            
            # Test file that should not be ignored
            self.assertFalse(should_ignore("/test/root/not_ignored.txt", "/test/root"))

    def test_get_rel_fname(self):
        self.assertEqual(self.repo_map.get_rel_fname("/test/root/file.txt"), "file.txt")
        self.assertEqual(self.repo_map.get_rel_fname("/test/root/dir/file.txt"), "dir/file.txt")

    # Add more tests for other methods in RepoMap class

if __name__ == '__main__':
    unittest.main()
