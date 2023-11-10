import random
import string
from .models import Person, Post


def create_random_user():
    username = f'user_{random.randint(1000, 9999)}'  # Generates a random username
    user = Person(username=username)
    user.save()
    return user


def create_random_text(length):
    # Generate a random string of ASCII characters, of the specified length
    letters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(letters) for _ in range(length))


def create_100_posts():
    for _ in range(100):
        user = create_random_user()  # Create a new user for each post
        content_length = random.randint(200, 500)  # Random length between 200 and 500
        content = create_random_text(content_length)  # Generate random text content
        post = Post(author=user, content=content)
        post.save()


# Call create_100_posts to populate the database with posts
create_100_posts()
