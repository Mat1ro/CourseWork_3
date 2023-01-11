import json


def get_posts_all():
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all():
    with open('./data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_bookmarks_all():
    with open('./data/bookmarks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name) -> list:
    users = get_posts_all()
    result = []
    for i in users:
        if i['poster_name'] == user_name:
            result.append(i)
    if len(result) == 0:
        raise ValueError('User not found')
    elif not 'content' in set(result[0].keys()):
        return []
    return result


def get_comments_by_post_id(post_id) -> list:
    list_comment = []
    cnt = False
    for comment in get_comments_all():
        if post_id == comment['post_id']:
            list_comment.append(comment)
    for i in get_posts_all():
        if post_id == i['pk']:
            cnt = True
    if not cnt:
        raise ValueError
    elif len(list_comment) == 0:
        return []
    return list_comment


def search_for_posts(query) -> list:
    posts = get_posts_all()
    result = []
    for i in posts:
        if query.lower() in i['content'].lower():
            if len(result) >= 10:
                break
            result.append(i)
    return result


def get_post_by_pk(pk):
    posts = get_posts_all()
    for i in posts:
        if pk == i['pk']:
            return i


def save_to_bookmarks(posts):
    with open('./data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)


def add_to_bookmarks(post):
    posts = get_bookmarks_all()
    posts.append(post)
    save_to_bookmarks(posts)


def remove_bookmark(pk):
    posts = get_bookmarks_all()
    for index, post in enumerate(posts):
        if post['pk'] == pk:
            del posts[index]
            break
    save_to_bookmarks(posts)
