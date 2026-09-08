from setuptools import setup

setup(
    name="greetlab-2502007013",
    version="0.1.0",
    packages=["greetlab"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "sdt-greet = greetlab.cli:main"
        ]
    }
)
