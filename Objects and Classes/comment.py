class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

    def User_comment(self):
        return f'{self.username}: {self.content} Likes: {self.likes}'


username = input()
content = input()
likes = int(input())

comment = Comment(username, content, likes)

print(comment.User_comment())
