import setuptools
from splitpdf_pro import __version__

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="splitpdf-pro",
    version=__version__,
    author="Jak Bin",
    description="A python package for split pdf",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jakbin/splitpdf-pro",
    project_urls={
        "Bug Tracker": "https://github.com/jakbin/splitpdf-pro/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='pdf,python-pdf,splitpdf,pypdf,splitpdf-pro',
    python_requires=">=3.6",
    install_requires=['PyPDF2'],
    packages=["splitpdf_pro"],
    entry_points={
        "console_scripts":[
            "splitpdf-pro = splitpdf_pro:main.main",
            "splitpdf = splitpdf_pro:main.main"
        ]
    }
)
