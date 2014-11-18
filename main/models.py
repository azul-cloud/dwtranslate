from django.db import models


EXP_TYPE_CHOICES = (
    ('INT', 'International'),
    ('POS', 'Positions Held'),
    ('PUB', 'Patents and Publications'),
    ('TEC', 'Technical'),
)


class Experience(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=3, default='INT', choices=EXP_TYPE_CHOICES)
    description = models.CharField(max_length=300)
    order = models.IntegerField(null=True, blank=True)
    special = models.BooleanField()
    special_order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['type', 'order']

    def __str__(self):
        return self.get_type_display() + ' - ' + self.title