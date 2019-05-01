from app.models import User, Comments, Post
from app import db

class CommentTest(unittest.TestCase):

  def setUp(self):
    self.new_user=User(1, 'derrick', 'derrick@email.com', datetime.now(), 'derrick', 'white', password='banana', access=1)
    
    self.new_post = Post(1, 'title', 'body', datetime.now())

    self.new_comment = Comments(1, 'just awesome', 1, datetime.now(),1)

  def tearDown(self):
    Post.query.delete()
    User.query.delete()
    Comments.query.delete()

  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.id, 1)

    self.assertEquals(self.new_comment.Comment, 'just awesome')

    self.assertEquals(self.new_comment.user_id, 1)

    self.assertEquals(self.new_comment.post, self.new_post.id)

  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all())>0)

  def test_get_comment_by_id(self):
    self.new_comment.save_comment()
    rcvd_comments = Comments.get_comments(56789)
    self.assertTrue(len(rcvd_comments) == 1)

  def test_delete_comments(self):
    self.new_comment.save_comment()
    self.new_comment.delete_post()
    self.assertTrue(len(Comments.query.all()) == 0)
