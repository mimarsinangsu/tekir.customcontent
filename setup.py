from setuptools import find_packages, setup

setup(
    name="tekir.customcontent",
    version="1.0a1",
    description="Basic custom content types for Plone.",
    author="H. Turgut Uyar",
    author_email="uyar@tekir.org",
    packages=find_packages(),
    namespace_packages=["tekir"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "plone.api",
        "plone.app.dexterity",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
