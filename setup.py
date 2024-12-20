#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bumpversion>=0.5.3",
        "ipython",
        "mypy==1.10.0",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
        "hypothesis>=4.18.0,<5",
        "coverage",
    ],
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="coti-eth-account",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.0.0",
    description="""coti-eth-account: Sign COTI messages/transactions with local private keys and encrypt/decrypt data with local AES keys.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="COTI Development",
    author_email="dev@coti.io",
    url="https://github.com/coti-io/coti-eth-account",
    include_package_data=True,
    install_requires=[
        "bitarray>=2.4.0",
        "eth-abi>=4.0.0-b.2",
        "eth-keyfile>=0.7.0, <0.9.0",
        "eth-keys>=0.4.0",
        "eth-rlp>=2.1.0",
        "eth-utils>=2.0.0",
        "hexbytes>=1.2.0",
        "rlp>=1.0.0",
        "ckzg>=2.0.0",
        "pydantic>=2.0.0",
        "coti-sdk>=1.0.4"
    ],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["eth_account"],
    license="MIT",
    zip_safe=False,
    keywords=["coti", "privacy", "ethereum", "blockchain", "web3", "garbled-circuits", "l2", "on-chain-compute"],
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    package_data={
        "eth_account": [
            "py.typed",
            "hdaccount/wordlist/*.txt",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
