import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Package Name",
    version="0.0.1",
    author="Timotheos Savva",
    author_email="",
    description="package description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github repo url",
    packages=setuptools.find_packages(),
    install_requires=[
        'reportlab',
        'pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
