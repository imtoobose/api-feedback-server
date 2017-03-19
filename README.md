# Feedback analysis: Server

This is the server/web app for a college faculty feedback application that 
we built over the course of 8 hours during D.J.S.C.O.E's ACM chapter's hackathon
(API). The server provides GET/POST calls to interact with an Android application
and also has pages that give an analysis based on the data recieved from the 
Android app. 


We used sklearn for a Sentiment Analysis of the comments written by students,
as well as a Bigram Collocation Finder using NLTK that would extract 
meaningul highlights from comments recieved, along with averages, strengths
and weaknesses of individual teachers.


This was built in collaboration with [@CCD-1997](https://github.com/CCD-1997) and
[@jitendra9873](https://github.com/jitendra9873). The android component of this
application is [here.](https://github.com/jitendra9873/api-feedback-android) The
code is incredibly messy, and not meant for production, but it works!


### Installing and running the server:

```
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```
