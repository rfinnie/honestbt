#!/usr/bin/env python3

from setuptools import setup


setup(
    name="honestbt",
    description="Destructive tester which detects dishonest block devices",
    license="GPLv2+",
    platforms=["Unix"],
    author="Ryan Finnie",
    author_email="ryan@finnie.org",
    scripts=["honestbt"],
)
