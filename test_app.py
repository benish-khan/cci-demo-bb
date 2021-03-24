import unittest
import sqlite3
from app import app 


class testClass(unittest.TestCase):

    def setUp(self):
        """ We have to first create a Sqlite db with actual db code. """
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()
        #setup a table called posts with 2 required fields.
        cmd_to_create_test_db = "CREATE TABLE posts (title TEXT, content TEXT)"
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
        #print(test_posts)
        #self.assertEqual(len(test_posts), n, "All posts should print")

        self.conn.close()


    # def test_get_post(self): #need to pass in post_id without it erroring out.
    #     #test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
    #     first_post = self.conn.execute('SELECT * FROM posts WHERE title = ?', (1,)).fetchone()
    #     print(first_post)
    #     # second_post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    #     # print(second_post)
    #     self.assertEqual(first_post.title,"First Post", "Blog post 1 should print")
    #     self.conn.close()




    def test_post(self):
       test_posts = self.conn.execute('SELECT * FROM posts').fetchall()
    #    post = test_get_post(post_id)
       self.conn.close()


    def test_create(self):
        # title = request.form['title']
        # content = request.form['content']
# error received: NameError: name 'request' is not defined

        # if not title:
        #     flash('Title is required!')
        # else:
        #     conn = get_db_connection()
        #     conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
        #                  (title, content))
        #     conn.commit()
        #     conn.close()
        self.conn.close()



    def test_edit(self):
        #  post = test_get_post(id)

        # if request.method == 'POST':
        #     title = request.form['title']
        #     content = request.form['content']

        #     if not title:
        #         flash('Title is required!')
        #     else:
        #         conn = get_db_connection()
        #         conn.execute('UPDATE posts SET title = ?, content = ?'
        #                     ' WHERE id = ?',
        #                     (title, content, id))
        self.conn.close()   
    
    def test_delete(self):
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

