# Music Recommender System

## Description
This repository contains the code for a music recommender system for Radio Javan. The system is designed to suggest songs based on user preferences and listening history. It utilizes TF-IDF for text analysis and incorporates various music features such as danceability, energy, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.6 or higher
- Jupyter Notebook

### Steps
1. Clone the repository
    ```sh
    git clone https://github.com/parvvaresh/Music-recommender-system.git
    ```
2. Navigate to the project directory
    ```sh
    cd Music-recommender-system
    ```
3. Create and activate a virtual environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Jupyter Notebook
1. Start Jupyter Notebook
    ```sh
    jupyter notebook
    ```
2. Open the `.ipynb` file in the Jupyter interface to run the code cells interactively.

### Running the Script
1. Ensure your virtual environment is activated
2. Run the Python script
    ```sh
    python script_name.py
    ```

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Any libraries, datasets, or tutorials that were particularly helpful.
- Any contributors or collaborators.

## Features
- **TF-IDF for Text Analysis**: Utilizes Term Frequency-Inverse Document Frequency (TF-IDF) to analyze textual data.
- **Music Features**: Incorporates various music features such as danceability, energy, and more to enhance recommendations.
