# dictionary = a collection of key value pairs
#   ordered and changeable . no duplicates

text_posts = {
    1: {"title": "New Post", "content": "This is the content of post 1"},
    2: {"title": "FastAPI Basics", "content": "Introduction to FastAPI and building APIs"},
    3: {"title": "Python Tips", "content": "Useful tips to write clean Python code"},
    4: {"title": "REST APIs", "content": "Understanding REST API principles"},
    5: {"title": "Async in Python", "content": "How async and await work in Python"},
    6: {"title": "Databases", "content": "Connecting FastAPI with SQL and NoSQL databases"},
    7: {"title": "Authentication", "content": "JWT authentication in FastAPI"},
    8: {"title": "Testing APIs", "content": "How to test FastAPI endpoints effectively"},
    9: {"title": "Deployment", "content": "Deploying FastAPI applications to production"},
    10: {"title": "Best Practices", "content": "FastAPI project structure and best practices"},
}
print(max(text_posts.keys()) + 1)


""""""
"""
capitals = {"USA": "Washington DC",
            "UK": "London",
            "COL": "Colombia",}
print(capitals.get("USA"))

if capitals.get("Japan"):
    print("that capital exists")
else:
    print("that capital doesn't exist")

capitals.update({"GER":"Berlin"})
capitals.pop("GER")
capitals.popitem()
keys=capitals.keys()
values = capitals.values()
items = capitals.items()

print(capitals)
print(keys)
print(values)

for key in keys:
    print(key)

for value in values:
    print(value)

for key,values in capitals.items():
    print(f"{key}: {values}")
"""
