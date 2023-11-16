import random
import string
from sample_feed.post.models import Person
from sample_feed.feed.models import PersonRelation
from sample_feed.post.serializers import PostSerializer


def create_random_person() -> Person:
    username = f'user_{random.randint(1000, 9999)}'  # Generates a random username
    person = Person(username=username)
    person.save()
    return person


def create_random_relations(person: int = None, n=2, relation_type='friend'):
    if not person:
        person = create_random_person().id

    relations = []
    for _ in range(n):
        friend = create_random_person()
        relations.append(PersonRelation(person=person, related_person=friend.id, relation_type=relation_type))
    return PersonRelation.objects.bulk_create(relations)


def create_random_text(length):
    # Generate a random string of ASCII characters, of the specified length
    letters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(letters) for _ in range(length))


def create_posts(person: int = None, n=10):
    if not person:
        person = create_random_person().id  # Create a new user for each post

    posts = []
    for _ in range(n):
        content_length = random.randint(200, 500)  # Random length between 200 and 500
        content = create_random_text(content_length)  # Generate random text content
        ser = PostSerializer(data={"person": person, "content": content})
        ser.is_valid(raise_exception=True)
        ser.save()
        posts.append(ser.instance)
    return posts

