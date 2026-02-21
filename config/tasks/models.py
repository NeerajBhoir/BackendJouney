from django.db import models
from django.contrib.auth.models import User
from datetime import date   # ← add this

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_overdue(self):
        """
        Returns True if task has a due date,
        is not completed, and due date has passed.
        """
        if self.due_date and not self.completed:
            return self.due_date < date.today()
        return False

    def __str__(self):
        return self.title