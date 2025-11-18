from setuptools import setup, find_packages

setup(
    name="get-costs",
    version="1.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "get-costs=get_costs.get_project_costs:main",  # ruft main.main() auf
        ],
    },
    install_requires=[
        #"python3-xlsxwriter", "python3-pandas", "python3-openpyxl"
        "XlsxWriter==3.2.2", "Pandas==2.2.3", "openpyxl==3.1.5"
    ],
    python_requires=">=3.8",
)
