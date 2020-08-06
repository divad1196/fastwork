import setuptools

setuptools.setup(
    name='fastframework',
    version='0.2',
    author="Gallay David",
    author_email="davidtennis96@hotmail.com",
    description="A fastapi - sqlalchemy based framework",
    setup_requires=['setuptools-markdown'],
    long_description_content_type="text/markdown",
    long_description_markdown_filename='README.md',
    url="https://github.com/divad1196/fastwork",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)