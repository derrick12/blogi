from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

ACCESS = {
  'user': 0,
  'admin': 1
}

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):

  __tablename__='users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(300))
  firstname = db.Column(db.String(300))
  lastname = db.Column(db.String(300))
  email = db.Column(db.String(300))
  date_joined =db.Column(db.DateTime,default=datetime.now)
  pass_secure = db.Column(db.String(300))
  access=db.Column(db.String(300), default=ACCESS['user'])

  comments = db.relationship('Comments', backref='user', lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You do not have the permissions to access this')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()

  def find_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user

  def is_admin(self):
    return self.access == ACCESS['admin']
    
  def allowed(self, access_level):
    return self.access >= access_level

  def init_db():
    if User.query.count() == 0:
      adminuser = User(username='adminuser', password='architect', firstname='derrick', lastname='kariuki', email='questech254@gmail.com', access=ACCESS['admin'])
      
      db.session.add(adminuser)
      db.session.commit()

  def __repr__(self):
    return f'User {self.username}'


class Comments(db.Model):

  __tablename__='comments'

  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  posted = db.Column(db.DateTime,default=datetime.now)
  post = db.Column(db.Integer, db.ForeignKey('posts.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  def delete_comments(self):
    db.session.delete(self)
    db.session.commit()


  @classmethod
  def get_comments(cls, id):
    comments = Comments.query.filter_by(posted=id).all()
    return comments


class Post(db.Model):

  __tablename__='posts'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(300))
  body = db.Column(db.String)
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  
  comments = db.relationship('Comments', backref='post_comments', lazy='dynamic')

  def save_post(self):
    db.session.add(self)
    db.session.commit()

  def delete_post(self):
    db.session.delete(self)
    db.session.commit()

  def get_specific_post(id):
    post = Post.query.filter_by(id=id).first()
    return post

  @classmethod
  def get_posts(cls):
    posts = Post.query.all()
    return posts

  def get_comments(self):
    post = Post.query.filter_by(id = self.id).first()
    comments = Comments.query.filter_by(post=post.id)
    return comments

  def default_posts():
    if Post.query.count() == 0:
      post1=Post(title='How to Silence the Persistent Ding of Modern Life', body="The ding of an incoming email used to give me a panic attack. Who was it? What did they want? Did I need to drop everything and answer them? Of course I did. They expected it. I was providing good customer service by dropping all my work, interrupting my flow, and telling them the thing they wanted to know, even if they could have figured it out on their own.")
      post2=Post(title='Invasion of the Influencers', body="How would you like to kick off your summer at the world’s most exclusive private island, surrounded by beautiful models and celebrities coming together to experience the same transformational weekend?")
      post3=Post(title='Discovering emerging digital innovation', body="Last week, a team of young Kenyans won the United Nations Educational, Scientific and Cultural Organization’s (Unesco) global award on innovation from their work of leveraging technology to eliminate women genital mutilation in Kenya. This apex award was created by Unesco’s Global Observatory on Digital Innovation under its exploration network (Netexplo) that scouts for new innovations across the world and brings them to market.")
      post4=Post(title='Belize, the rule of law and judicial independence', body="The strong eastern winds blowing from the Caribbean Sea thwarted my jogging efforts. I kept going; the scenery was idyllic. It was 6:45 am and I was in Belize City. The city was asleep. The sun had already been up for more than an hour. Suddenly, I noticed that not everyone was asleep. Dean Barrow was also jogging, perhaps walking fast, at a comfortable pace on the other side of the street. Mr Barrow is no small man. He is Belize’s Prime Minister. He had no bodyguards, no retinue; he was alone.")
      post5=Post(title='Counties can improve service delivery by embracing peer review', body="It is said that ''What gets measured gets done.'' In other words, regular measurement and reporting keeps you focused. Last week, President Uhuru Kenyatta demonstrated his conviction in this wisdom by launching the African Peer Review Mechanism (APRM) country report at a time when most other African countries have almost abandoned the process.")
      post6=Post(title='Unprotected server exposed data on 80 million U.S. households', body="A cloud server operated by Microsoft has been leaking the personal data of 80 million U.S. households including people's full names, physical addresses, and dates of birth.A pair of Israeli security researchers say they discovered the unprotected database while working on a web mapping project with VPN review site vpnMentor. In addition to names and addresses, the 24GB database also stored coded information on people's gender, marital status, income levels, and whether they've been a homeowner.")
      post7=Post(title='AWS opens up its managed blockchain as a service to everybody', body="After announcing that they were launching a managed blockchain service late last year, Amazon Web Services is now opening that service up for general availability.It was only about five months ago that AWS chief executive Andy Jassy announced that the company was reversing course on its previous dismissal of blockchain technologies and laid out a new service it would develop on top of open source frameworks like Hyperledger Fabric and Ethereum.")
      post8=Post(title='YouTube sets a goal of having half of trending videos coming from its own site', body="YouTube  wants to have half of the featured videos in its trending tab come from streams originating on the company’s own site going forward, according to the latest quarterly letter from chief executive Susan Wojcicki.")
      db.session.add(post1)
      db.session.add(post2)
      db.session.add(post3)
      db.session.add(post4)
      db.session.add(post5)
      db.session.add(post6)
      db.session.add(post7)
      db.session.add(post8)
      db.session.commit()