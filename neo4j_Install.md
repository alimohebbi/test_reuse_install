# Neo4J Desktop Setup
- create a project
- create a local graph name "db" set password for example "1234""
- Go to manage -> plugins -> install APOC and restart we used 3.5.0.9 probably new version is also ok 
- Go to manage -> setting add following lines  in the end of file and reset

````
apoc.import.file.enabled=true
apoc.import.file.use_neo4j_config=false
````

- click on open browser and use the user "neo4j"and pass "1234""
- run command `:SERVER change-password` and change password to "neo4j". You cannot change the settings through desktop Neo4j which is ok. Also details is not valid anymore because it cannot connect to db. click ignore on prompt box regarding enter the new password. 
- For testing your database run `neotest.sh`. It should create a graph with 17 nodes & 24 relations. You need to have `db.json`file in same place as `neotest.sh`  Don't worry about removing them from db. ATM does it before creating new graph. 

Following commmand returns the count of nodes (Can be used for testing whether the database runs correctly)
````
MATCH (n) RETURN count(n) as count
````


Following command removes everything from db (Just in case if you need it). It can be run from Neo4j browser.
````
MATCH (n) DETACH DELETE n
````


# Neo4J server  
Server can be used without any desktop. Still web browser is accessible.

### APOC plugin
- get jar file from internet. It should be compatible with the version.
- Put in $NEO4J_HOME/plugin
- insert the two line of mange setting in $NEO4J_HOME/conf/neo4j.conf

### Initialization
- set java home to java 11
- start the server $NEO4J_HOME/bin/neo4j [start/console]
- set initial password 
````
neo4j-admin set-initial-password <the password>
````
- change the password if necessary
````
ALTER USER <username> SET PASSWORD '<password>';
````

### Request 
- `note`: For authentication you should encode <user>:<pass> to base 64
- `note`: To send request to a database other than default you should send to 
```
localhost:7474/db/<database name>/tx/commit
```