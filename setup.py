import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimpleDashboard",
    version="0.0.1",
    author="Lukas Scheffler",
    author_email="luke@lukecodewalker.de",
    description="Simple framework for web dashboards.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukeSkywalker92/SimpleDashboard",
    packages=setuptools.find_packages(),
    install_requires=['flask',
                      'flask-socketio',
                      'greenlet',
                      'eventlet'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
