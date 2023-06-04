import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="gpt-cli",
    version="1.0.0",
    author="Valery Kharitonov",
    author_email="val@kharvd.com",
    description="Command-line interface for ChatGPT, Claude, and Bard",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kharvd/gpt-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "gpt-cli = gptcli.__main__:main",
        ],
    },
    python_requires=">=3.6",
    install_requires=requirements,
)
