from setuptools import setup, find_packages

setup(
    name="get-costs",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "get-costs=get_costs.get_project_costs:main",  # ruft main.main() auf
        ],
    },
    install_requires=[
        # z.B. "requests", "PyQt5"
    ],
    python_requires=">=3.8",
)
