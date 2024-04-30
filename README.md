# search-engine

This is my pet project to implement search-engine system. The system design will be implemented in the following picture:

![Hello](images/Search%20Engine%20UML.png)


To try this, please follow the following steps:

- Start docker compose to initialize all backend infras, go to folder backend/infrastructure and run:

```
 docker compose --env-file env up -d
```


- After all services is healthy, you need to visit [kaggle site](https://www.kaggle.com/datasets/shivamb/netflix-shows/download?datasetVersionNumber=5) to download sample netflix data for this demo. After downloaded successfully, create ad-hoc script to transform and insert data in Elasticsearch.

- Go to folder backend and set environment for backend (swagger api):

```
ES_HOST=localhost
ES_PORT=9200
ES_USERNAME=elastic
ES_PASSWORD=elasticpassword

```

and, then start service swagger API:

```
# Install package dependencies
pip install -r requirements.txt
python app.py
```

After run application successfully, the swagger api is ready to accept connection.



- When all backend services function properly, navigate to folder frontend/templates and click on file `index.html` to start the search engine in the browser. Enjoy!
  ![results](images/search-engine-results.png)