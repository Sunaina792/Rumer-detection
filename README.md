## Rumour Detection

This project is a web application designed to detect and analyze rumours from various sources, with a focus on text extracted from images. It uses Optical Character Recognition (OCR) to process images like social media screenshots and applies analysis techniques to flag potential misinformation. The application is built using Streamlit, providing an interactive user interface.

## Features

-   **Interactive Web Interface:** Built with [Streamlit](https://streamlit.io/) for easy interaction and data visualization.
-   **Image-based Text Extraction:** Utilizes Tesseract OCR via `pytesseract` to extract text from images.
-   **Data Analysis:** Leverages `pandas` for data manipulation and analysis of the extracted text.
-   **Visualization:** (Planned) Uses `altair` for creating insightful visualizations of the analysis results.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

-   **Python 3.8+**
-   **Tesseract OCR Engine:** `pytesseract` is a wrapper for Google's Tesseract-OCR Engine. You need to install it separately.
    -   **Windows:** Download and install from the Tesseract at UB Mannheim page. Make sure to add the Tesseract installation directory to your system's `PATH`.
    -   **macOS:** `brew install tesseract`
    -   **Linux (Debian/Ubuntu):** `sudo apt-get install tesseract-ocr`

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd rumour-detection
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required Python packages:**

    A `requirements.txt` file is recommended for this project. If you don't have one, you can create it based on the libraries used. Key dependencies include:
    ```
    streamlit
    pandas
    pytesseract
    altair
    Pillow
    numpy
    ```
    You can install them using pip:
    ```bash
    pip install streamlit pandas pytesseract altair Pillow numpy
    ```
    Or, if a `requirements.txt` file is provided:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application, execute the following command in your terminal from the project's root directory:

```bash
streamlit run main.py
```

This will start the web server and open the application in your default web browser.

## Project Structure

```
.
├── .gitignore
├── main.py         # Main application script
└── .venv/          # Virtual environment directory
```

## How It Works (High-Level)

1.  **Input:** The user uploads an image (e.g., a screenshot of a social media post) through the Streamlit interface.
2.  **OCR Processing:** `pytesseract` is used to extract the text content from the uploaded image.
3.  **Analysis:** The extracted text is processed and analyzed to detect characteristics of a rumour. (The specific detection logic needs to be implemented).
4.  **Output:** The application displays the analysis results, indicating whether the content is likely a rumour and providing relevant details or visualizations.

## Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to create an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request




 



