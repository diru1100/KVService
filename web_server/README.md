# key value web server

## Setup:
- If you have followed installation steps in top-level README.md, go ahead and run the server using
``` flask run```

## Tests

- To run tests, enter 
``` pytest  ```

## Other info:

- This is an api built using flask-restful 
- There are two endpoints present to respond to requests
    - ```/kvstore``` to get and post to key value store in database
    - ```/listen``` is to listen or "watch" the changes happedning to a particular key in database, basically subscribing to changes
