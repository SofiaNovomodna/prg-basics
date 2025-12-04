class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(self.username,':')
        print()
        count = 1
        for i in self.posts:
            print(count, i)
            print()
            count +=1

person1 = SocialMediaProfile('johndoe')
person1.add_post('Hello, world!')
person1.add_post('Had a great day at the park!')
person1.add_post("What's up, Natalie? How are you?")
person1.display_timeline()