# django-blog
 
 This project run a django blog
 
 
 ## Run a data base for test.
 
 ### Create a data base 
`docker run -d --name dj-blog -p 5434:5432 -e POSTGRES_PASSWORD=dj-blog -e POSTGRES_DB=dj-blog -e POSTGRES_USER=dj-blog postgres`

### Run data base
`docker start  dj-blog`

### stop data base
`docker stop  dj-blog`

### delete data base
`docker rm  dj-blog`
