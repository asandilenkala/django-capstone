from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """
    Configuration class for the 'portfolio' app in the Django project.

    This class is responsible for setting up and configuring the 'portfolio'
    application. It defines the default primary key field type to use for
    models in this app, as well as the name of the app.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use for models.
        name (str): The name of the Django application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
