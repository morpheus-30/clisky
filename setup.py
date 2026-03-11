from setuptools import setup, find_packages

setup(
    name="clisky",
    version="0.1.0",
    description="AI-powered Linux CLI command recommender",
    author="Naksh",
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