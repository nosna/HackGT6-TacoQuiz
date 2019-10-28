# HackGT6-TacoQuiz

**Interactive Language Learning Alexa Skill for all Passionate SSL(Spanish as Second Language) Students**

***Created by: Runsheng Huang, Jinchen Ma, David Pan, Zhen Jiang, Leyan Pan***

## **It's punny** 
> ### *"Alexa, open Taco Quiz"*
> ### *"Hola! A TACO a day, keeps the bad grade away. Let's TACO some basic Spanish vocabulary quizzes. We have 20 vocabs in the word bank. How many vocabs would you like to TACO today?"*

## **It's caring** ##
> ### *"I want to practice zero vocab"*
> ### *"You have to get some tacos. How many vocabs would you like to TACO today?"*

> ### *"I would like to practice three thousands"*
> ### *"You have too many tacos. How many vocabs would you like to TACO today?"*

## **It's patient** ##
> ### *"What's one in Spanish?"*
> ### *"It's dos"*
> ### *"Try again, mi amigo."*

## **It's encouraging** ##
> ### *"What's hello in Spanish?"*
> ### *"It's hola"*
> ### *"Hola is correct. You can say "more tacos" for the next question."*

## **It's your BEST Spanish learning partner!** ##


### Inspiration
Speaking of learning a new language, we usually think of watching long tedious YouTube videos, or holding a massive language intro book in your hand. But how many people have ever thought of the black little sound box located somewhere in the house -- Amazon Echo? Today we introduce a brand new way to learn a new language. It is interactive, instant-feedback, and most importantly, it makes the best use of your fragmented time. If you are cooking in the kitchen, you can learn Spanish while making your delicious tacos.

### What It Does
This Alexa Skill gives user Spanish vocabulary quizzes. User will be prompted to choose how many vocabs he/she wants to be tested on. The user will then be prompted to say either a Spanish word or an English word upon given the meaning of the word in the other language. Alexa will then give instant feedback on whether or not the user is correct. If given the wrong answers in two consecutive runs, Alexa will give user the correct answer.

### How We Built It
Utilizing AWS platform and Alexa developer console, we implemented the Lambda function in Python as our own endpoint for hosting Alexa. Then, we combine intents and handler methods that are unique to Alexa to build a function that prompts the user to test their knowledge in Spanish given the English words that exist in our database.

### Challenges We Ran Into
The first challenge was to determine the technologies we should use. At the starting stage of our project, we spend an entire night on setting up the development environment of DynamoDB with Java on our machines. However, it turned out that using local DynamoDB environment is not absolutely required. We then switch to full cloud development with Python on the next morning and made substantial progress thereafter.

We have no experience in building a Alexa Skill before. The biggest challenge we encountered was understanding the methods, logic, and control flow that are provided and required by Alexa. We spent the most debugging time on dealing with parameter passing between IntentHandler methods to create the control flow we desired. After countless rounds of attempting new fixes, looking up documents and examples, we finally nailed our goal of building a fully functional vocabulary tester.

### Accomplishments that We're Proud Of
Created a complete control flow in an environment in which none of us have experience in, including user voice-input taking, IntentHandling creating and branching, asserting true or false based on user's reply, replying proper messages in different cases, and choosing the most efficient data structure to connect the words in two languages.

### What We Learned
Since having only 36 hours to design an application is very time-constrained, we learned to set up milestones at every stage in order to know that we were on the right track. In addition, we also learned to cooperate with one another to reach a goal that is promising and meaningful.

### What's Next for TacoQuiz
We will host the data to the real database as the demand of the consumers for this Alexa Skill becomes larger and larger. Therefore, hosting the data to the real database not only enables us to include more people, but also encourage a learning atmosphere. In addition, we hope that we can deploy this function to our daily devices, such as phones, Amazon Echo, etc., so customers can have easy access to our handy function. Moreover, in the future, we hope that customers can add their own custom word lists to Alexa using AWS, and Alexa can test them based on the lists given.

### Built With
amazon-alexa, amazon-web-services, python
