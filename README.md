# intelistyle task:
Your task is to build a (single page) website that I can search for a garment (e.g. black hat) and it should display the garments that match the search criteria.

## The solution:
The website should load garments from a MongoDB database. You can load data into your database from this file:

https://stylr-ai-engine-srv-data.s3.eu-west-1.amazonaws.com//srv/data/new_scrapes/shopstyle-1689-men-18-03-2019/garment_items.jl

You have the freedom to use any build toolchain or helper libraries necessary, but you must stick to our core technologies of ReactJS for the frontend and NodeJS or Python for the backend.

As part of the deliverable, there should be automated tests for all the possible use cases of the task.

## Success Criteria:
- Application architecture and framework best practices for the framework in use are followed and understood.
- Code is formatted well and easy to follow. Variable and function names make sense
- Application gracefully handles database error cases and is resistant to unexpected messages.
- Database queries are optimised for performance
- Test coverage of the web page is sufficient and thought has been put into what areas of the application should and
  shouldn’t be tested.

## Bonus Points (optional):

- Design an infrastructure architecture diagram that can be used to scale the website to thousands of searches per
  second

## Submission Requirements:

- Send an email to your recruiter with a link to a public git repository (in GitHub/BitBucket/GitLab, etc) with the
  name [firstname]-[submission date].
- Provide a link to a hosted version of the project
- You will be asked to screen share and walk through this app & code in your next interview, please have it ready to be
  run prior to the interview.

## Run

Set environment variable:

```shell script
export MONGODB_URL=<mongo db URL>
export MONGODB_DB_NAME=<mongo db database name>
export MONGODB_COLLECTION=>mongo db collection>
```

### Terminal with virtual env

If you want to run the app in a terminal, write:

```shell script
cd src
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```

Test:

```shell script
pytest -vvv
```

### Docker

Run:

```shell script
make run
```

Stop:

```shell script
make stop
```

Check the API with http://127.0.0.1:8000/health

## Documentation

http://127.0.0.1:8000/docs
