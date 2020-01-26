from setuptools import setup, find_packages

setup(
    name="vrb2json",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(),

    install_requires=["flask"],

    author="Yannick Rehberger",
    author_email="dev@rehberger.family",
    description="Simple HTTP service, that converts VRB statements into json.",
    keywords="flask banking statement csv json",
    url="https://github.com/ityreh/vrb2json",
)
