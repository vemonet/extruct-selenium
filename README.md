# 🧃 Extruct Selenium

Small script and docker image to extract metadata, such as JSON-LD snippets, embedded in HTML pages rendered by JavaScript frameworks on the client side, such as React.

HTML rendered from the JavaScript using Selenium Firefox, metadata extracted from the HTML using `extruct`.

## 📦️ Build

```bash
docker build -t extruct-react .
```

## 🌜️ Run

Use the script to provide the URL to extract metadata from, and run it with docker:

```bash
./run_extruct.sh https://fair-enough.semanticscience.org/evaluation/f0b7a7f7e05592e776c1a54040416500ec69e45c
```

Or run it directly with the long docker command:

```bash
docker run --rm --shm-size="2g" -it extruct-react https://fair-enough.semanticscience.org/evaluation/f0b7a7f7e05592e776c1a54040416500ec69e45c
```

