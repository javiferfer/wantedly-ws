![](https://dubpy8abnqmkw.cloudfront.net/images/feeds/clark_lp/logos/wantedly.png)

# Coding challenge Wantedly

Build a web app where a user can list his/her skills in a profile page and recommend/endorse skills to other users. 

## Characteristics of the project


## url so as to log in

http://127.0.0.1:8000/profiles/register_user/


## Steps for importing the data

from profiles.models import Javi

javi = Javi(name="Javier", age=23, sex="Male", photo="https://www.shareicon.net/data/2016/09/01/822711_user_512x512.png", skillFirst="c++", skillSecond="leadership", skillThird="Communication", skillForth="English")

javi.save()


## References

https://github.com/codingforentrepreneurs/try-django-19