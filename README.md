## NEIGHBORHOOD 

### Description

This is a Django web application that allows users to be in the loop about everything happening in your neighborhood.



## Author

**Author** Moses Gakuhi

## Technologies Used

- PYTHON `3.8`
- DJANGO
- HEROKU

### User Stories
As a user of the application I should be able to:
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Specifications:
These are the actions the user will do.Inputs required and their outputs on the page. 


  | Action       | Input                                      |Output                                     |
  | ----------   |:-------------                              | :------                                   |
  | Load page    |On page load                                | Displays the homepage                     |
  | Click        |Click on the join neighborhood button       |Join a neighborhood                        |
  | Click        |Click a post button                         | Post something for your neighbors to see  |
  | Click        |Click the leave button                      | Leave the neighborhood                    |
  | Search       |search for the posted projects              | Projects as per search term               |

## Live Demo

[Live Demo Link]()


### Installation Process

- Clone the repository using the link below

```
$ git clone https://github.com/MosesGakuhi1857/neighbourhod.git

```

- Create a directory and install the requirements

  ```
  pip install -r requirements.txt
  ```
- Run the application using;
  ```
  python3.8 manage.py runserver
  ```
- Test it if its working using;
  ```
  python3.8 manage.py test
  ```
- Open the application on your browser , preferably `chrome` using port `127.0.0.1:8000`



##  License

This project is MIT licensed.