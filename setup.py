from setuptools import setup, find_packages

setup(
    name="gptpy",
    version="0.1.0",
    description="An AI-powered Python Helper powered by GPT-3",
    author="Junbum Lee",
    author_email="junbumlee@icloud.com",
    url="https://github.com/beomi/gptpy",
    packages=find_packages(),
    entry_points={"console_scripts": ["gptpy = gptpy.gptpy:main"]},
    install_requires=["requests"],
)
