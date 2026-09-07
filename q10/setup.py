from setuptools import setup, find_packages

setup(
    name="greetlab-2502007013",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "sdt-greet = greetlab.cli:main"
        ]
    }
)
