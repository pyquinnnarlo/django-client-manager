from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()
setup(
    name="django_client_manager",
    version="1.0",
    packages=find_packages(),
    install_requires=["django"],
    
    # Project metadata
    author="Quinn Narlo",
    author_email="pyquinnnarlo@gmail.com",
    description="A Client manager for custom django user.",
    long_description=description,
    long_description_content_type="text/markdown",
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