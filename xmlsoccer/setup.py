from setuptools import setup

setup(
    name="xmlsoccer",
    version="0.2",
    description="Parse xmlsoccer feed",
    author="Martin Eastwood",
    author_email="hello@martineastwood.co.uk",
    packages=["xmlsoccer"],
    install_requires=["requests", "lxml"],
    url="http://pena.lt/y",
)
