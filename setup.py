# setup.py
from pyhades import __version__
import setuptools
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    _requirements = fh.read()

system_platform = platform.system()

setuptools.setup(
    name="Steam-RS",
    version=__version__,
    author="KnowAI",
    author_email="dev.know.ai@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU AFFERO GENERAL PUBLIC LICENSE",
    url="https://github.com/know-ai/steam-rs",
    package_data={'src': ['*.json']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=_requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring"
    ]
)
