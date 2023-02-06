# job-hunting-helper

Program to help in my job-hunting process

## Motivation

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
  - [ ] The job application contains the job title of the job opening or the job title desired when there isn't a job opening but exist the interest in working with certain company.
  - [ ] The job application contains an application status.
  - [ ] The job application contains a date of application. (Optional)
  - [ ] The job application contains the source of the job opening.
  - [ ] The job application contains the company name.
  - [ ] The job application contains the skills specific to the job opening.
  - [ ] The job application contains an indicator of the skill alignment.

- [ ] 4 - Application status

  As a user, I want to check and modified the status of any application or my interest in a company or job so that I can keep track of the things to do or that I've done in preparation for the job.

  Acceptance criteria:

  - [ ] I can see the predefined status as _Interesado_ (Spanish for interested).
  - [ ] I can change the status predefined to one the following:

    - _Preparando/personalizando CV_ (Spanish for preparing/personalizing resume)
    - _CV enviado/aplicacion iniciado_ (Spanish for resume sent/application initiated)
    - _Agendando entrevista_ (Spanish for scheduling interview)
    - _Entrevista agendada_ (Spanish for interview scheduled)
    - _Rechazado_ (Spanish for rejected)
    - _Aceptado_ (Spanish for approved)
    - _Contrato firmado_ (Spanish for contract signed)
    - _Onboarding_

- [ ] 5 - Date of application

  As a user, I want to add the date I begun the applying process so that I can have an idea of the time passed since the process begun.

  Acceptance criteria:

  - [ ] The date is automatically set when the status change from _Interesado_ or _Preparando/personalizando CV_ to _CV enviado/aplicacion iniciada_ to the current date.
  - [ ] The date can be mannually set.

- [ ] 6 - Job title

  As a user, I want to add or edit the job title so that at first glance I know what to expect from the job opening.

  Acceptance criteria:

  - [ ] I can use a previous entered job title instead of typing it again.
  - [ ] I get autocompletion suggestions
  - [ ] I get suggestions based on keywords.

- [ ] 7 - Source

  As a user, I want to add the source from where I'm applying to the job opening or in the case of interest for a job/company the medium to contact them so that I know where to check for updates of the process and review the job opening.

  Acceptance criteria:

  - [ ] I can select a predefined source. For example: Linkedin, company website.
  - [ ] I can add a new source.
  - [ ] When done with the editing I can select the source and be redirect to the job opening website or company website.
