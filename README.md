# Project Setup

## Directory Structure
```
├── data/          # Data files and datasets
├── notebooks/     # Jupyter notebooks for exploration
├── model/         # Trained models and model artifacts
├── src/           # Source code
├── requirements.txt
└── README.md
```

## Environment Setup

### Create Python Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Libraries
```bash
pip install -r requirements.txt
```

## Dependencies
- torch: PyTorch deep learning framework
- transformers: Hugging Face transformers library
- datasets: Hugging Face datasets library
- pandas: Data manipulation and analysis
- scikit-learn: Machine learning utilities
- nltk: Natural language processing toolkit
- sentencepiece: Text tokenization library