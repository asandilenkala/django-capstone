from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    """
    Represents a project in the portfolio.

    Attributes:
        title (str): The title of the project.
        description (str): A detailed description of the project.
        github_url (str): The URL to the project's GitHub repository.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField()

    def __str__(self):
        """
        Returns the string representation of the Project, which is the title.

        Returns:
            str: The title of the project.
        """
        return self.title