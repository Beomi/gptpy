from setuptools import setup, find_packages

setup(
    name="gptpy",
    version="0.1.6",
    description="GPTPy: Your kind Python guide, powered by AI to fix errors and explain code",
    author="Junbum Lee",
    author_email="junbumlee@icloud.com",
    url="https://github.com/beomi/gptpy",
    packages=find_packages(),
    entry_points={"console_scripts": ["gptpy = gptpy.gptpy:main"]},
    install_requires=["requests"],
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
)
