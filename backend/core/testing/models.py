from django.db import models
from django.conf import settings


class Question(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text


class Test(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class CompletedTest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'test')

    def __str__(self):
        return f'{self.user} - {self.test}'
