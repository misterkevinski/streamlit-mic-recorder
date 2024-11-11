from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_mic_recorder_custom",
    version="0.0.1",
    author="Kevin Beck",
    author_email="misterkevinski@gmail.com",
    description="Streamlit component that allows to record mono audio from the user's microphone, and/or perform speech recognition directly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misterkevinski/streamlit-mic-recorder",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
        "SpeechRecognition"
    ],
)
