from django.apps import AppConfig

# Configuration class for the 'accounts' app
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Sets the default auto field type for model primary keys
    name = 'accounts'  # Specifies the name of the app
