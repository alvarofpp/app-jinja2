# Jinja2 template app

An application made in Streamlit that allows you to test Jinja2 templates.

## How to use

There are two ways to use the application: using the repository or using the Docker image.
Both ways use Docker, but in the first case you can make your changes to the code and test locally.

If you want to use a web version, [click here][streamlit-app].

### Using the repository

The instructions are in the `Makefile`, so just run the command below to generate the image:

```shell
make build
```

Now up a container from the previously generated Docker image:

```shell
make up
```

### Using the Docker image

I've already left a Docker image ready to use. Just run it:

```shell
docker run -p 8501:8501 --rm alvarofpp/app-jinja2
```

[streamlit-app]: https://streamlit.io/cloud
