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
    - [Installation](#installation)
  - [👨🏻‍ About the Author](#-about-the-author)
</details>

## ⚙ ️Setup

### Setup venv
<code>
  sudo apt install python3.8-venv
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
</code>

### BentoML
<code>
  alias bentoml='/home/ubuntu/.local/bin/bentoml'
  bentoml serve service --reload
  bentoml build
  bentoml containerize service:latest
</code>

### Docker
<code>
docker run -p 3000:3000 service:latest
docker save -o bento_image.tar service
</code>

## 👨🏻‍ About the Author

**Heuzef**

This project was created by Heuzef. Connect with me on [heuzef.com](https://heuzef.com) to learn more about my projects and professional background.


<p align="right"><a href="#readme-top">Top ⬆️</a></p>