# vrb2json
Simple HTTP service, that converts VRB statements into json.

## Run
You can simply run the service locally in your Virtualenv.

```
FLASK_APP=./src/app.py flask run
```

Note that this is a development server. Do not use it in a production deployment.
Use curl to validate availability.

```
curl http://localhost:5000/vrb2json/v1/info
```
