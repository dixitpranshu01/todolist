from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_next_task_id(cls):
        last_task = cls.objects.order_by('id').last()
        if last_task:
            return last_task.id + 1
        else:
            return 1

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.get_next_task_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
