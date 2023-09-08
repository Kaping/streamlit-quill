from pathlib import Path
import setuptools


setuptools.setup(
    name="streamlit-quill-no-handler",
    version="0.0.3",
    author="kaping",
    author_email="",
    description="Quill component for Streamlit",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kaping/streamlit-quill",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
