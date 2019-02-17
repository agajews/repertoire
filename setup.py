import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repertoire",
    version="0.0.1",
    author="Alex Gajewski",
    author_email="agajews@gmail.com",
    description="Spaced repetition in plain text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agajews/repertoire",
    packages=setuptools.find_packages(),
    install_requires=["blessings", "click", "getkey"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
