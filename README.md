## Description

This microservice provides the current Unix time when invoked.

## Installation

Create a virtual environment and execute:
```
pip3 install -r requirements.txt
```

## Deployment
Change directory to `src/` and run one of the following:

```
dev: uvicorn epoch:app --reload
prod: gunicorn uvicorn.workers.UvicornWorker epoch:app
```

## Invocation

Example:
```
curl http://localhost:8000
```

## License
Apache 2.0

See [LICENSE](LICENSE)