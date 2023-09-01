from django.db import models


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField()
    Q1 = models.TextField()
    Q2 = models.TextField()
    #id = 
    #comment_set = 

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    # poll_id
    # 저장방법 고민 숫자 글자 