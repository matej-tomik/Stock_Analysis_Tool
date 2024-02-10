from setuptools import setup, find_packages


# TODO: Upravit ROFL Rekni Chudickovi
VERSION = "1.0.0"
DESCRIPTION = "stock analyser"
LONG_DESCRIPTION = "this analyzer analyzes stocks using Graham's numbers DDM and DCF models and returns their results relative to the current stock price"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="verysimplemodule",
    version=VERSION,
    author="Matěj Tomík",
    author_email="<mtomik.work@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["yfinance"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "stock analysis"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
