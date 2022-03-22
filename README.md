# 🧃 Extract metadata from client JS websites

Today a lot of websites are using JavaScript to render HTML pages in the users browser (aka. the client), for example websites built with the React framework. This requires to execute the JavaScript sent by the server before extracting metadata from the HTML.

This script packages **[Selenium](https://www.selenium.dev/)** and **[Extruct](https://github.com/scrapinghub/extruct)** with Docker to enable you to test extracting metadata from any URL quickly from your terminal ⚡️

The HTML is rendered from the JavaScript using Selenium Firefox, and metadata are extracted from the HTML using `extruct`.

## 🌜️ Run

> Requirements: [Docker 🐳](https://docs.docker.com/get-docker/)

To extract metadata from an URL: pass the URL as argument, and run the script with Docker.

Extract metadata from an URL after automatically executing the JavaScript:

```bash
docker run --rm --shm-size="2g" --network host -it ghcr.io/vemonet/extruct-selenium https://fair-enough.semanticscience.org/evaluation/f0b7a7f7e05592e776c1a54040416500ec69e45c
```

Use the `--no-render` flag to test extracting metadata from the HTML without executing the JavaScript to see the difference:

```bash
docker run --rm --shm-size="2g" --network host -it ghcr.io/vemonet/extruct-selenium https://fair-enough.semanticscience.org/evaluations/8953ccf7bba4bc5fcd2124c0e68730601eeb0362 --no-render
```

Check all options:

```bash
docker run --rm --shm-size="2g" --network host -it ghcr.io/vemonet/extruct-selenium
```

> ℹ️ You can append ` > your_file.json` at the end of the command to store the metadata output in a file instead of displaying it in the terminal.

## 📦️ Build

You can make changes to the script and rebuild the image, feel free to send pull requests to propose improvements!

```bash
docker build --build-arg SELENIUM_TAG=4.1.1-20220121 -t ghcr.io/vemonet/extruct-selenium .
```

> Check the latest available [Selenium tags here](https://hub.docker.com/r/selenium/standalone-firefox/tags)
