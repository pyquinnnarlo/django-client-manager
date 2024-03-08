from setuptools import setup, find_packages

setup(
    name="django_client_manager",
    version="1.0",
    packages=find_packages(),
    install_requires=["django"],
    
    # Project metadata
    author="Quinn Narlo",
    author_email="pyquinnnarlo@gmail.com",
    description="A Client manager for custom django user.",
    long_description="Django Client Manager is a Python library designed to streamline the process of creating custom user accounts in Django applications. This library simplifies the handling of Django's custom user creation by providing a set of convenient and efficient tools.",
    url="https://github.com/pyquinnnarlo/django-client-manager",
    
    # Other optional metadata
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="django client manager",
    project_urls={
        "Source": "https://github.com/pyquinnnarlo/django-client-manager",
    },
)