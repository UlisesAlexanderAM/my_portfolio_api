# job-hunting-helper (web)

Program to help in my job-hunting process. In the future I'll use fastapi, flask or django to implement it for the web. I'll create a new repo for the GUI version.

## Motivation

I started this project because I was unsatisfied with the implementation of this in a spreadsheet so I decided to build my program to use during my job-searching process.

Also, I started this so that I can showcase and improve my abilities as a software engineer. That's why I write down the user stories I came up with to describe the project.

## User interface mockups

Below are some mockups for the user interface, with the passed of time and as I progress in the development of the app I'll replace the mockups by screenshots of the working app.

This is how I imaginated the skill window without selecting any:

![Skills without selections](https://user-images.githubusercontent.com/30351520/220728276-db83a107-3910-4500-8825-3bc5a79b528c.svg)

Now, with a skill selected:

![Skills with selections](https://user-images.githubusercontent.com/30351520/220728409-22f63301-733e-47b8-8ff2-7cd02ec4b91d.svg)

And finally with all the skill selected:

![Skills all selected](https://user-images.githubusercontent.com/30351520/220728443-75e089b6-94c8-446e-976a-c34d2db2d4ea.svg)

## User stories

- [ ] 1 - Register skill and skill level,

  As a person job-hunting (user), I want to register a skill and my level in that skill so that I know how prepared I'm for a job opening.

  Acceptance criteria:

  - [ ] The skill appears in a section along with other skills.
  - [x] A skill consists of a name.
  - [x] todo: representation of the skill level.

- [ ] 2 - Show skill

  As a user, I want to see my skills together so that I know if there is a skill to register or if I don't consider it relevant anymore.

  Acceptance criteria:

  - [ ] A section where I can see my skills and their respective levels.
  - [ ] From this view, I can choose to edit or delete a skill.

- [ ] 3 - Register a job application/interest in a job or company

  As a user, I want to register my interest in a specific job or company, or a job application to a certain job opening so that I know the job or companies I'm aiming for.

  Acceptance criteria:

  - [ ] The job application appears in a section along with other applications.
  - [x] The job application contains the job title of the job opening or the job title desired when there isn't a job opening but exists an interest in working with a certain company.
  - [x] The job application contains an application status.
  - [x] The job application contains a date of application. (Optional)
  - [x] The job application contains the source of the job opening.
  - [x] The job application contains the company name.
  - [x] The job application contains the skills specific to the job opening.
  - [x] The job application contains an indicator of skill alignment.

- [ ] 4 - Application status

  As a user, I want to check and modified the status of any application or my interest in a company or job so that I can keep track of the things to do or that I've done in preparation for the job.

  Acceptance criteria:

  - [ ] I can see the predefined status as _Interesado_ (Spanish for interested).
  - [ ] I can change the status predefined to one of the following:

    - _Preparando/personalizando CV_ (Spanish for preparing/personalizing resume)
    - _CV enviado/aplicacion iniciado_ (Spanish for resume sent/application initiated)
    - _Agendando entrevista_ (Spanish for scheduling interview)
    - _Entrevista agendada_ (Spanish for an interview scheduled)
    - _Rechazado_ (Spanish for rejected)
    - _Aceptado_ (Spanish for approved)
    - _Contrato firmado_ (Spanish for contract signed)
    - _Onboarding_

- [ ] 5 - Date of application

  As a user, I want to add the date I have begun the application process so that I can have an idea of the time passed since the process began.

  Acceptance criteria:

  - [ ] The date is automatically set when the status change from _Interesado_ or _Preparando/personalizando CV_ to _CV enviado/aplicación iniciada_ to the current date.
  - [ ] The date can be manually set.

- [ ] 6 - Job title

  As a user, I want to add or edit the job title so that at first glance I know what to expect from the job opening.

  Acceptance criteria:

  - [ ] I can use a previously entered job title instead of typing it again.
  - [ ] I get autocompletion suggestions
  - [ ] I get suggestions based on keywords.

- [ ] 7 - Source

  As a user, I want to add the source from where I'm applying to the job opening or in the case of interest for a job/company the medium to contact them so that I know where to check for updates on the process and review the job opening.

  Acceptance criteria:

  - [ ] I can select a predefined source. For example Linkedin, the company website.
  - [ ] I can add a new source.
  - [ ] When done with the editing I can select the source and be redirected to the job opening website or company website.

- [ ] 8 - Company Name

  As a user, I want to add the name of the company I'm applying to or I'm interested in so that I can prioritize my studies, the scheduling the interviews.

  Acceptance criteria:

  - [ ] I can see the company name alongside the job title, and source in the record of the application.
  - [ ] I can select one of the company names from previous company names used in other applications.
  - [ ] I get suggestions as I'm typing.

- [ ] 9 - Skills for a specific job opening or company

  As a user, I want to add the skill required and desired but not required for a job opening or company so that I can know how qualified I'm for the job, know more about myself so I can be honest with the company about my skills, and to know in what I can improve or what I can learn.

  Acceptance criteria:

  - [ ] I can add one or more skills from a list of skills already registered.
  - [ ] If the skill doesn't exist, create it and add it.

- [ ] 10 - Indicator of skill alignment

  As a user, I want to see an indicator of the skill alignment between me and the job opening or company so that I can decide if I start the process or not.

  Acceptance criteria:

  - [ ] I can see the percentage of skill alignment
  - [ ] The color of the indicator changes following the criteria written below:
    - \> 80% of required skills - Green
    - \> 70% of required skills and > 50% of desired but not required skills - Green
    - Between 50% and 70% of required skills and > 80% of desired but not required skills - Green
    - Between 50% and 70% of required skills - Yellow
    - < 50% of required skills and > 80% of desired but no required skills - Yellow
    - < 50% of required skills and < 80% of desired but no required skills - Red

- [ ] 11 - Filters

  As a user, I want to filter my applications or; my interest in companies or jobs so that I can get a clear view of what I want to do at a certain moment.

  Acceptance criteria:

  - [ ] I can filter by company
  - [ ] I can filter by the status of an application
  - [ ] I can filter by skill alignment
  - [ ] I can filter by job title
  - [ ] I can filter by source
  - [ ] I can filter by date of application
