import unittest
import sqlite3
from app import app 


class testClass(unittest.TestCase):

    def setUp(self):
        """ We have to first create a Sqlite db with actual db code. """
        self.conn = sqlite3.connect(":memory:") #supply the special name :memory: to create a database in RAM
        c = self.conn.cursor()
        #setup a table called posts with 2 required fields.
        cmd_to_create_test_db = "CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)"
        c.execute(cmd_to_create_test_db)
        # add the first test blog post with title.
        blog_1= "INSERT INTO posts (title, content) VALUES('First Post', 'blah')"
        c.execute(blog_1)
         # add the first test blog post with title.
        blog_2= "INSERT INTO posts (title, content) VALUES('Second Post', 'blah blah')"
        c.execute(blog_2)
        test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
        #print(test_posts)
        self.conn.commit()



    def test_index(self):
        test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
       # print(test_posts)
        self.assertEqual(len(test_posts), 2, "All posts should print which should be 2")
        self.conn.close()


    def test_get_post(self): #need to pass in post_id without it erroring out.
        test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
        first_post = self.conn.execute('SELECT * FROM posts limit 1').fetchone()
        #print(first_post)
        # second_post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
        # print(second_post)
        self.assertEqual(first_post[1],'First Post', "Blog post 1 should print")
        self.conn.close()



    def test_post(self):
       test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
       second_post = self.conn.execute('SELECT * FROM posts WHERE id = ?', "2").fetchone()
       self.assertEqual(second_post[0],2, "Blog post 2 id should print")
       self.conn.close()


    def test_create(self):
        test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
        blog_3= "INSERT INTO posts (title, content) VALUES('Third Post', 'blah blah blah')"
        self.conn.execute(blog_3)
        self.conn.commit()
        test_posts_now = self.conn.execute('SELECT * FROM posts').fetchall()
        self.assertEqual(len(test_posts_now), 3, "All posts should print which should be 3")
        #print(test_posts_now)
        self.conn.close()



    def test_edit(self):
        test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
        third_post_initial = "INSERT INTO posts (title, content) VALUES('Third Post', 'blah blah blah')"
        self.conn.execute(third_post_initial)
        self.conn.commit()
        test_posts_now = self.conn.execute('SELECT * FROM posts').fetchall()
        # print(test_posts_now)
        # third_post_update = "UPDATE posts SET (id = '3', title = 'Now 3rd', content = 'asdfghjk') WHERE ID = 3", (id, title, content)
        # self.conn.execute()
        # self.conn.commit()
        # print(third_post_update)
        # print(test_posts)
        self.conn.close()   
    
    def test_delete(self):
        test_posts_1 = self.conn.execute('SELECT * FROM posts').fetchall()  
        blog_3= "INSERT INTO posts (title, content) VALUES('Third Post', 'blah blah blah')"
        self.conn.execute(blog_3)
        self.conn.commit()
        print(test_posts_1) # prints 2 entries
        test_posts_2 = self.conn.execute('SELECT * FROM posts').fetchall()
        print(test_posts_2)# prints 3 entries
        # 'SELECT * FROM posts WHERE id = ?', "2"
        new_blog_lst = self.conn.execute('DELETE FROM posts WHERE id = ?', "3")
        self.conn.commit()
        #print(test_posts)
        #print(new_blog_lst)
        self.conn.close()


    def tearDown(self):
        # post = get_post(id)
        # conn = get_db_connection()
        # conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        # conn.commit()
        # conn.close()
        # flash('"{}" was successfully deleted!'.format(post['title']))
        self.conn.close()


if __name__ == '__main__':
    unittest.main()

