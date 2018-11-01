import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pippractice",
    version="0.0.1",
    author="Lulu",
    author_email="luludarcy@gmail.com",
    description="A practice package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luludarcy/pippractice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)