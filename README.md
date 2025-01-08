<a name="readme-top"></a>
<div align="center">

<a href="" target="_blank" title="Go to  website">
<img width="196px" alt="Examen BentoML" src="https://www.inovex.de/wp-content/uploads/mlops-mit-BentoML-1500x880.png">
</a>

# Examen BentoML

Complete pipeline with BentoML for predict the chance of admission of a student in a university.

</div>

<div align="center"><h4><a href="#-table-of-contents">️Table of Contents</a> • <a href="#-setup">⚙ ️Setup</a> • <a href="#-about-the-author">👨🏻‍ About the Author</a></h4></div>

## ️Table of Contents
 <details>
<summary>Open Contents</summary>

- [Examen BentoML](#examen-bentoml)
  - [⚙ ️Setup](#-setup)
  - [👨🏻‍ About the Author](#-about-the-author)
</details>

## ⚙ ️Setup

### Setup requirements

Python, Docker and BentoML is needed. Please install before use. So set the python env :

```bash
  sudo apt install python3.8-venv
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
```

### Prepare data and load your model

```python  
python3 src/prepare_data.py
python3 src/train_model.py
```

### Create container with BentoML
```bash
  bentoml build
  bentoml containerize service:latest
```

### Docker
```bash
bentoml list # get the tag
docker run --rm -p 3000:3000 service:<tag>
```

### Tests

```python  
python3 -m pytest tests/test_api.py
python3 tests/predict.py
```

## 👨🏻‍ About the Author

**Heuzef**

This project was created by Heuzef. Connect with me on [heuzef.com](https://heuzef.com) to learn more about my projects and professional background.

<p align="right"><a href="#readme-top">Top ⬆️</a></p>