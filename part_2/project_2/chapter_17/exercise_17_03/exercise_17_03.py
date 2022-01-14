# Exercise 17-3 (unittest python_repos.py)

import unittest
import python_repos as pr

class PythonReposTest(unittest.TestCase):
    """Test python_repos.py"""

    def test_status_code(self):
        """Check if status code is 200"""
        status_code = pr.r.status_code
        self.assertEqual(status_code, 200)
    
    def test_len_top_repos(self):
        """Check if there are specifically 30 top repos"""
        len_repos = len(pr.repo_dicts)
        self.assertEqual(len_repos, 30)
    
    def test_len_total_repos(self):
        """Check if total repos are more than top repos"""
        len_top_repos = len(pr.repo_dicts)
        len_all_repos = pr.response_dict['total_count']
        self.assertTrue(len_top_repos <= len_all_repos)

if __name__ == '__main__':
    unittest.main()