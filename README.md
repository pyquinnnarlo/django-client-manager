# Django Client Manager

Django Client Manager is a Python library designed to streamline the process of creating custom user accounts in Django applications. This library simplifies the handling of Django's custom user creation by providing a set of convenient and efficient tools.

## Features

- **Easy Custom User Creation**: Simplifies the process of creating custom user accounts in Django projects.

- **Password Hashing**: Create secure hashed password.

- **Password Strength Validation**: Built-in password strength validation to enhance security.



## Installation

```bash
pip install django-client-manager
```

## Quick Start

1. Install the package using the command mentioned above.

2. Configure your Django project settings:

   ```python
   # models.py
   
   from django-client-manager.client import Client
   ```

3. Use the `ClientManager` in your code:

   ```python
   from django.db import models
   from .custom import Client
   
   class TestClient(Client):
       pass
 
   ```




## Contributions

Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
