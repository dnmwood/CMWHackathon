## Look at this graph

### Setup

Make sure you have flask downloaded

`pip install Flask`

### Running
To run the server
`FLASK_APP=hello.py flask run`

### Quick debugging from the shell
We can send HTTP requests from the shell by running

To initialize the server

`curl -XPOST localhost:5000/init`

To get percentages

`curl -XGET localhost:5000/percentage`