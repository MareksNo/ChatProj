from django.db import models


class Conversation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Message(models.Model):
    conversation = models.ForeignKey(to=Conversation, on_delete=models.CASCADE)
    content = models.TextField()

    # Fields required for the mvp, in the future additions like the sender etc. are planned.
    def __str__(self):
        return self.content
