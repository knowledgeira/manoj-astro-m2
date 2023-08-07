FROM python:3.9-slim 
WORKDIR /app
COPY astro_life.py /app/
RUN pip install Flask
EXPOSE 5000
CMD ["python", "astro_life.py"]

