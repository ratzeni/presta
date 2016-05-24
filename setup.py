from setuptools import setup

AUTHOR_INFO = [
  ("Gianmauro Cuccuru", "gianmauro.cuccuru@crs4.it"),
  ]
MAINTAINER_INFO = [
  ("Gianmauro Cuccuru", "gianmauro.cuccuru@crs4.it"),
  ]
AUTHOR = ", ".join(t[0] for t in AUTHOR_INFO)
AUTHOR_EMAIL = ", ".join("<%s>" % t[1] for t in AUTHOR_INFO)
MAINTAINER = ", ".join(t[0] for t in MAINTAINER_INFO)
MAINTAINER_EMAIL = ", ".join("<%s>" % t[1] for t in MAINTAINER_INFO)
PACKAGES = ['app', 'app.celery']

setup(name="presta",
      version='0.1',
      description="Utility to process sequencing data",
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      install_requires=['alta', 'celery', 'drmaa'],
      packages=PACKAGES,
      dependency_links=[
        "https://github.com/gmauro/alta/tarball/master#egg=alta",
      ],
      license='MIT',
      platforms="Posix; MacOS X; Windows",
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Topic :: Utilities",
                   "Programming Language :: Python :: 2.7"],
      )



