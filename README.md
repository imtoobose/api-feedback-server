# Feedback analysis: Server

This is the server/web app for a college faculty feedback application that 
we built over the course of 8 hours during D.J.S.C.O.E's ACM chapter's hackathon
(API). The server provides GET/POST calls to interact with an Android application
and also has pages that give an analysis based on the data recieved from the 
Android app. 


We used sklearn for Sentiment Analysis of the comments written by students
as well as Bigram Collaction Finder using NLTK that would extract 
meaningul highlights from comments recieved.


This was built in collaboration with [@CCD-1997](https://github.com/CCD-1997) and
jitendra9873(https://github.com/jitendra9873). The android component of this
application is [here.](https://github.com/jitendra9873/api-feedback-android)
