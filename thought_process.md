## My thought process while building the solution 

### Approach:

- Especially keeping in "watch" feature in mind, I thought of the following appraches:
    - going with redis or other framework which gives inbuilt functionality but I didn't want to use extra dependencies. 
    - Somehow use trigger? didn't help much
    - Maybe use flask signals? didn't work out as well
    - For this assessment at least, I used the concept of Server side events(which works perfectly for our use case ^_^) with the help of [python sse client](https://github.com/btubbs/sseclient)
- Used flask-restful wrapper around flask to approach the problem in an object ortiented mannner. 
- Made use of click package which helped me write beautiful cli with minimum effort
- Made use of sqlite itself which doesn't require any external dependencies or servers set up. 
- Used pytest to easily test out the api with minimal fixtures to get the job done.
- Documented and added comments how much ever I can

### Other thoughts

- Haven't exactly followed the HTTP suggested specification by passing data in GET requests, Ideally can be implemented in an other way.
- Tests are not super upto the mark, major efforts were kept to implement custom watch functionality without external dependencies(I learned new things here).
- Kept in mind the reusability of the code in this appoach

## Future scope

- Add more proper tests with increasing functionalities and code coverage
- Go for established frameworks to utilize their pub/sub model like redis when used in scale
- Add security to the handle data via encryption, or de-duplication, if the use cases require it
- Introduce retries for failures.
- Add extensive error handling, monitoring (like latency of processing) for failures
