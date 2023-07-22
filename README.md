# My portfolio API previously known as Job Hunting Helper

This is a project to keep track of my skills and the projects related to them. It is the API of my portfolio.

## Motivation

This project started as an app to keep track of my job applications, but as I was developing it I realized that I was more interested in keeping track of my skills and the projects related to them. So I decided to change the focus of the app. This forms the API of my portfolio. The front end will be in another repository.

## User stories

- [ ] 1 - Register a new skill
  As a person who wants to keep track of my skills, I want to register a new skill, so that I can keep track of it.

  Acceptance criteria:
  - [x] I can register a new skill
  - [x] The skill consists of a name
  - [ ] The skill has a description (optional)
  - [ ] The skill has a list of projects related to it which can be empty
  - [ ] The skill has an image or icon associated with it (optional)
  - [ ] The skill has a list of keywords associated with it which can be empty.

- [x] 2 - Retrieve a skill
  As a person who wants to keep track of my skills, I want to retrieve a skill, so that I can see its details.

  Acceptance criteria:
  - [x] I can retrieve a skill by its id
  - [x] I can retrieve a skill by its name

- [x] 3 - Retrieve all skills
  As a person who wants to keep track of my skills, I want to retrieve all skills, so that I can see all of them.

  Acceptance criteria:
  - [x] I can retrieve all skills

- [ ] 4 - Update a skill
  As a person who wants to keep track of my skills, I want to update a skill, so that I can keep it up to date.

  Acceptance criteria:
  - [x] I can update a skill by its id
  - [x] I can update a skill by its name
  - [ ] I can update a skill's description
  - [ ] I can update a skill's image or icon
    - [ ] I can delete a skill's image or icon
    - [ ] I can add a skill's image or icon
  - [ ] I can modify a skill's name
    - [ ] If the new name is already in use, the skill's name is not modified
  - [ ] I can update a skill's projects
    - [ ] I can add a project to a skill
      - [ ] If the project doesn't exist, it is created
    - [ ] I can remove a project from a skill
  - [ ] I can update a skill's keywords
    - [ ] I can add a keyword to a skill
      - [ ] If the keyword doesn't exist, it is created
    - [ ] I can remove a keyword from a skill

- [ ] 5 - Delete a skill
  As a person who wants to keep track of my skills, I want to delete a skill, so that I can remove it from my list.

  Acceptance criteria:
  - [x] I can delete a skill by its id
  - [x] I can delete a skill by its name

- [ ] 6 - Register a new project
  As a person who wants to keep track of my skills, I want to register a new project, so that I can keep track of it.

  Acceptance criteria:
  - [ ] I can register a new project
  - [ ] The project consists of a name
  - [ ] The project has a description
  - [ ] The project has a list of links that can be empty
  - [ ] The project has a list of skills related to it which can be empty
  - [ ] The project has an image or icon associated with it (optional)
  - [ ] The project has a list of keywords associated with it which can be empty

- [ ] 7 - Retrieve a project
  As a person who wants to keep track of my skills, I want to retrieve a project, so that I can see its details.

  Acceptance criteria:
  - [ ] I can retrieve a project by its id
  - [ ] I can retrieve a project by its name

- [ ] 8 - Retrieve all projects
  As a person who wants to keep track of my skills, I want to retrieve all projects, so that I can see all of them.

  Acceptance criteria:
  - [ ] I can retrieve all projects

- [ ] 9 - Update a project
  As a person who wants to keep track of my skills, I want to update a project, so that I can keep it up to date.

  Acceptance criteria:
  - [ ] I can update a project by its id
  - [ ] I can update a project by its name
  - [ ] I can update a project's description
  - [ ] I can update a project's link
  - [ ] I can update a project's image or icon
  - [ ] I can modify a project's name
    - [ ] If the new name is already in use, the project's name is not updated
  - [ ] I can update a project's skills
    - [ ] I can add a skill to a project
      - [ ] If the skill doesn't exist, it is created
    - [ ] I can remove a skill from a project
  - [ ] I can update a project's keywords
    - [ ] I can add a keyword to a project
      - [ ] If the keyword doesn't exist, it is created
    - [ ] I can remove a keyword from a project

- [ ] 10 - Delete a project
  As a person who wants to keep track of my skills, I want to delete a project so that I can remove it from my list.

  Acceptance criteria:
  - [ ] I can delete a project by its id
  - [ ] I can delete a project by its name

- [ ] 11 - Register a new keyword
  As a person who wants to keep track of my skills, I want to register a new keyword, so that I can keep track of it.

  Acceptance criteria:
  - [ ] I can register a new keyword
  - [ ] The keyword consists of a name
  - [ ] The keyword has a description
  - [ ] The keyword has an image or icon associated with it (optional)
  - [ ] The keyword has a list of skills related to it
  - [ ] The keyword has a list of projects related to it

- [ ] 12 - Retrieve a keyword
  As a person who wants to keep track of my skills, I want to retrieve a keyword, so that I can see its details.

  Acceptance criteria:
  - [ ] I can retrieve a keyword by its id
  - [ ] I can retrieve a keyword by its name

- [ ] 13 - Retrieve all keywords
  As a person who wants to keep track of my skills, I want to retrieve all keywords, so that I can see all of them.

  Acceptance criteria:
  - [ ] I can retrieve all keywords

- [ ] 14 - Update a keyword
  As a person who wants to keep track of my skills, I want to update a keyword, so that I can keep it up to date.

  Acceptance criteria:
  - [ ] I can update a keyword by its id
  - [ ] I can update a keyword by its name
  - [ ] I can update a keyword's description
  - [ ] I can update a keyword's image or icon
  - [ ] I can modify a keyword's name
    - [ ] If the new name is already in use, the keyword's name is not updated
  - [ ] I can update a keyword's skills
    - [ ] I can add a skill to a keyword
      - [ ] If the skill doesn't exist, it is created
    - [ ] I can remove a skill from a keyword
  - [ ] I can update a keyword's projects
    - [ ] I can add a project to a keyword
      - [ ] If the project doesn't exist, it is created
    - [ ] I can remove a project from a keyword

- [ ] 15 - Delete a keyword
  As a person who wants to keep track of my skills, I want to delete a keyword so that I can remove it from my list.

  Acceptance criteria:
  - [ ] I can delete a keyword by its id
  - [ ] I can delete a keyword by its name

- [ ] 16 - Register a new image or icon
  As a person who wants to keep track of my skills, I want to register a new image or icon, so that I can keep track of it.

  Acceptance criteria:
  - [ ] I can register a new image or icon
  - [ ] The image or icon is a file or a link to the file

- [ ] 17 - Retrieve an image or icon
  As a person who wants to keep track of my skills, I want to retrieve an image or icon, so that I can see it.

  Acceptance criteria:
  - [ ] I can retrieve an image or icon by its id
  - [ ] I can retrieve an image or icon by its name

- [ ] 18 - Delete an image or icon
  As a person who wants to keep track of my skills, I want to delete an image or icon so that I can remove it from my list.

  Acceptance criteria:
  - [ ] I can delete an image or icon by its id
  - [ ] I can delete an image or icon by its name
