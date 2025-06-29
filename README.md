# CS340-Client-Server-Development
### How do you write programs that are maintainable, readable, and adaptable? 
  *Consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two.* 
  * In order to keep my programs maintainable I like to create functions that are reusable meaning I can take that function and call it at different locations in my code. This reduces the amount of times I need to rewrite certain lines and completely eliminates others. In the project we created for this class I had a .py file where all of my functions lived.
  * Having all the functional code in my .py file made the main code base more readable. My file was used to house the create, read, update, and delete functions as well as the code that created the object constructors used on the CRUD operations.
  * One of the abilites of separating the code in such a way is that it becomes more adaptable. I was able to use the same crud.py module by importing it into different programs and then run the operations with no issues.   

### What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
  * The advantage of creating a crud.py module was that it was reusable as the main code changed. The database stayed the same which is why we were able to use the same module. Making changes in the main program was simple and only required a function call to implement. In our project only the create method was utilized so in the future if I wanted to use the other methods all I would need to do is update the main code to include their functionality. I could also create something entirely new to utilize the database and implement the CRUD functions.  

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
