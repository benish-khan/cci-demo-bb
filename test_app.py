import unittest
import sqlite3
from app import index


class testClass(unittest.TestCase):

    def setUp(self):
        """ We have to first create a Sqlite db with actual db code. """
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()
        #setup a table called posts with 2 required fields.
        cmd_to_create_test_db = "CREATE TABLE posts (title TEXT, content TEXT)"
        c.execute(cmd_to_create_test_db)
        # add the first test blog post with title.
        cmd_test_blog_1="INSERT INTO posts (title=First Post , content=Example test content for the first post')"
        c.execute(cmd_test_blog_1)
         # add the first test blog post with title.
        cmd_test_blog_2="INSERT INTO posts (title=Second Post , content='Example test content for the second post')"
        c.execute(cmd_test_blog_2)
        test_posts = conn.execute('SELECT * FROM posts').fetchall()
        print(test_posts)
        self.conn.commit()


    # def test_index(self):
    #     """ test is the index page displays all posts """
    #     #self.assertEqual()
    #     pass

    # def test_post(self):
    #     #self.assertEqual()
    #     pass

    # def test_create(self):
    #     #self.assertEqual()
    #     pass

    # def test_edit(self):
    #     #self.assertEqual()
    #     pass

    # def test_delete(self):
    #     #self.assertEqual()
    #     pass 

    # def tearDown(self):
    #     """ This function tears down db once tests are completed."""
    #     self.conn.close()

if __name__ == '__main__':
    unittest.main()

