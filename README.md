## Problem Statement

•	Whenever we search for any symptoms on google, it ultimately leads us to bigger diseases like HIV, Cancer etc which might be not the case every time.

•	A lot of people including corporate employees and students don’t get much time or procrastinate to take advice from a doctor, which in future leads to severe complications.


•	People from small towns are often being referred to doctors in bigger cities at crucial point of time and sometimes detecting the actual problem gets delayed and people have to suffer from severe complications of disease.  

## Solution Proposed

•	We are making the search process more defined by not only asking the user for symptoms but also the severity of the symptoms on a scale of 1-5, and also more than one symptoms with its severity is considered to predict the disease precisely. Apart from the symptoms ,  the user also need to input his/her age and sex for best results.
•	This combination of inputs now predicts the 5 most probable diseases along with the probability to the user. 
•	After predicting the diseases, the user can view various useful information regarding any of the 5 disease of which choice. This info contains the following things:

* Blogs: related to the diseases being predicted
* Medicines: suggested medicines that can be helpful in that diseases with disclaimer that not to take it without consulting the doctor for proper doses.
* Complication: List of complications that can arise in future if the diseases is not treated on time.
* Home Remedies: To avoid consumption of medicines for diseases that can be cured by simple home remedies.
* Symptoms: The user may only know few symptoms that he/she is experiencing and may have few more that they are actually not sure of. So, our symptoms list will help them to get a clear knowledge  about their symptoms .

•	Our application will be a multiuser platform where people using it will be rating the blogs, medicines, list of doctors and everything else based on how it helped them, and how much they liked it. This way our review system will sort the best blogs and other materials to always give the best result on top for the user.




## Technology used

•	Machine Learning(NLP+ Supervised Learning)

•	Django

•	Python

•	HTML

•	CSS

•	JS

## Working

•	Run `pip install -r requirements.txt`

•	Run `pip install sklearn`

•	Run `pip install scipy`

•	Here the name of the Project is IT_day wherease the name of the app of knowmedy.To run the server , use command:
  `python manage.py runserver`
  
•	Visit address http://127.0.0.1:8000/ and Enter the login credentials after which we are directed on the Page where we need to            
  fill in the symptoms and patient details. 
  
•	On submitting , we are given a result of most probable diseases with probabilities . On clicking on the particular disease we 
  are redirected to the Details of the Disease including Introduction,Other Symptoms, Remedies,Causes and Medicines.

• Now visit address http://127.0.0.1:8000/index where we need to enter the Name of The disease and we are redirected to the Details of the Disease including Introduction,Other Symptoms, Remedies,Causes and Medicines.

## Future Scope
During this limited time period we were only able to built a prototype of our proposed solution and still have some significant points in our mind where we can improve and scale it to a larger scale. So here goes our future scope:
•	Using the geo navigation, our application will also provide the list of doctors present nearby to the location of the user, for those particular diseases that he/she may be suffering with.

•	We will be incorporating a chat system where people can chat with other doctors or among themselves sharing advices and knowledge ,which will be more of a community.

•	We also thought of implementing this system on Block Chain to make this process decentralized and scalable on National or Bigger level.
