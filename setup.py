from setuptools import setup

setup(
    name="pinata-python",
    version="1.0.0",
    description="A python API for pinata.cloud library.",
    url="https://github.com/pan-efs/pinata-python",
    author="Panagiotis Efstratiou",
    author_email="",
    license="MIT",
    packages=[
        "pinata_python",
        "pinata_python.exceptions",
        "pinata_python.urls",
        "pinata_python.utils",
        "pinata_python.tests"
    ],
    python_requires='>=3.8',
    install_requires=["pytest", "requests"],
    include_package_data=True,
    zip_safe=False,
)