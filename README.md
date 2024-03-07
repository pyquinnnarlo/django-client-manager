# Django Client Manager

Django Client Manager is a Python library designed to streamline the process of creating custom user accounts in Django applications. This library simplifies the handling of Django's custom user creation by providing a set of convenient and efficient tools.

## Features

- **Easy Custom User Creation**: Simplifies the process of creating custom user accounts in Django projects.

- **Flexible Configuration**: Allows customization of user creation through configuration options, making it adaptable to various project requirements.

- **Password Strength Validation**: Built-in password strength validation to enhance security.

- **Email Verification**: Optional email verification for newly created user accounts.

- **User Profile Support**: Integration with Django user profiles for additional user information.

## Installation

```bash
pip install django-client-manager
```

## Quick Start

1. Install the package using the command mentioned above.

2. Configure your Django project settings:

   ```python
   # settings.py
   
   AUTH_USER_MODEL = 'your_app.YourCustomUser'
   ```

3. Use the `ClientManager` in your code:

   ```python
   from client_manager import ClientManager

   client_manager = ClientManager()
   user = client_manager.create_user(username='example', email='example@example.com', password='securepassword')
   ```

4. Customize the configuration as needed:

   ```python
   # settings.py
   
   CLIENT_MANAGER_SETTINGS = {
       'PASSWORD_POLICY': {
           'min_length': 8,
           'require_uppercase': True,
           'require_digits': True,
       },
       'EMAIL_VERIFICATION': True,
   }
   ```

## Configuration Options

- **PASSWORD_POLICY**: Dictionary to configure password strength requirements.

- **EMAIL_VERIFICATION**: Boolean to enable or disable email verification for newly created user accounts.

- **USER_PROFILE**: Boolean to enable or disable user profiles.

## Example Usage

```python
# views.py

from client_manager import ClientManager

def register_user(request):
    if request.method == 'POST':
        client_manager = ClientManager()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = client_manager.create_user(username=username, email=email, password=password)

        # Additional logic, such as sending a verification email

        return HttpResponse('User registered successfully!')
    else:
        return render(request, 'registration/register.html')
```

## Contributions

Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
