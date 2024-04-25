**Using Approuter and Python app in Kyma for user authentication**

I used this as a first project to check on how we can secure published apps in Kyma with user authentication by using an SAP BTP IDP.

**Landscape**
- SAP BTP (Trial)
- SAP Kyma environment
- SAP Authorization and Trust Management Service (Kyma generated)
- Docker
- Python 3.12 as the app (Dockerized)
- SAP Approuter image on Dockerhub (sapse/approuter:16.0.1)


**Usecase**
Until now my apps have always been published via API-Rule in Kyma to everybody. There was no login procedure before accessing the app.
To make my applications only available to users I want the app to use I tried to find a solution to generate some kind of login procedure without having to manage a user database myself by hosting a user database.

SAP BTP has a service called "Authorization and Trust Management Service" available in the BTP (aka XSUAA).
With that you can handle the user management inside your BTP subaccount.
What you have to do yourself is routing the request from the login screen to your app.
This is done by using SAP Approuter - which is publicly available as an image on dockerhub (https://hub.docker.com/r/sapse/approuter)


