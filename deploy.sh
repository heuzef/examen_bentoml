bentoml serve service:examen_bentoml --reload
bentoml build
bentoml containerize examen_bentoml:latest
docker run -p 3000:3000 examen_bentoml:latest
docker save -o bento_image.tar examen_bentoml