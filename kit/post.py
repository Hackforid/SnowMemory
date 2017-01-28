# coding=utf-8
from models.user import User
from models.post import Post
from models.comment import Comment


def fill_users(posts):
    user_ids = []
    for post in posts:
        if post['author_id'] not in user_ids:
            user_ids.append(post['author_id'])
        if post['target_id'] not in user_ids:
            user_ids.append(post['target_id'])
        for comment in post.get('comments', []):
            if comment['author_id'] not in user_ids:
                user_ids.append(comment['author_id'])

    users_db = User.select().where(User.id << user_ids)
    users = [user.to_dict() for user in users_db]
    for post in posts:
        post['target'] = get_user_by_id(users, post['target_id'])
        post['author'] = get_user_by_id(users, post['author_id'])
        for comment in post.get('comments', []):
            comment['author'] = get_user_by_id(users, comment['author_id'])

def get_user_by_id(users, id):
    try:
        return  next(user for user in users if user['id'] == id)
    except:
        pass

def fill_comments(posts):
    post_ids = [post['id'] for post in posts]
    comments = Comment.get_by_post_ids(post_ids)
    for post in posts:
        post['comments'] = [comment.to_dict() for comment in comments if comment.post_id == post['id']]

def fill_user_and_comment_to_post(posts):
    fill_comments(posts)
    fill_users(posts)
