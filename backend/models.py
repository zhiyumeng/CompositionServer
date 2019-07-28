from django.db import models


# Create your models here.

class Composite(models.Model):
    def __init__(self,title=None,author=None,text=None):
        super().__init__()
        self.title = title
        self.author = author
        self.text = text
    title = models.CharField('composite title', max_length=200)
    text = models.TextField('coposite content')
    author = models.CharField('author',max_length=200)

    def __str__(self):
        return "%s written by %s"%(self.title,self.author)
