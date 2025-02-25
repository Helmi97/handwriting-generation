from setuptools import setup, find_packages

setup(
    name="handwriting_generation",
    version="0.1.0",
    description="Unified toolkit for handwritten text generation including VATr, ScrabbleGAN, and VATrpp",
    author="Your Name",
    author_email="your-email@example.com",
    url="https://github.com/helmi97/handwriting-generation",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.7",
    include_package_data=True,
)
