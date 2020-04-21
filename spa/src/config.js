/**
* Author: Ryan Sreenivasam
* Description: Config file to ensure that the url of the django server is 
* correct for any user.
*/

/** 
* This is the URL of the Django server that is running the backend of this 
* application. If your django server is running on a different URL, change 
* this variable to that URL so the API requests will go to the correct 
* address.
*
* TODO set this up in package.json to handle testing vs production URL
*/
const djangoURL = "http://127.0.0.1:8000/"

export { djangoURL };