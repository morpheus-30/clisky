from setuptools import setup, find_packages

setup(
    name="clisky",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "openai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "clisky=clisky.cli:ai_cli",
        ],
    },
)