# Rate-My-Coop

Rate My Co-op is a full-stack web application concept designed to help students make more informed decisions about co-op and internship opportunities.

The platform will allow students to search companies and co-op positions, read reviews from previous students, compare experiences, and eventually discover current job opportunities.

The goal is to create a centralized platform similar to Rate My Professor, but focused specifically on the co-op experience.

---

## Project Status

🚧 **Currently in Planning / Early Development**

At the moment, the project is in the design and planning stage. We are defining the database structure, technologies, features, and overall user experience before beginning development.

---

## Planned Features

### Company & Co-op Reviews

Students will be able to search for companies and specific co-op positions and view reviews from previous employees or co-op students.

Reviews may include ratings for:

- Overall experience
- Workload
- Work environment and company culture
- Learning opportunities
- Management and mentorship
- Pay satisfaction

Students will also be able to provide additional information such as:

- What they worked on during the co-op
- Typical responsibilities
- Requirements or skills needed for the position
- Typical working hours
- Pay range
- Whether they would recommend the position

---

## Search & Filtering

Users will be able to search and filter co-op opportunities by factors such as:

- Company
- Position
- Industry
- Location
- Rating
- Pay range
- Co-op term
- Work environment

---

## User Accounts

Users will eventually be able to create accounts in order to:

- Submit reviews
- Edit their reviews
- Save companies or positions
- Track co-op opportunities

One possible feature is using university email verification to help improve the reliability of reviews.

---

## Job Opportunities

The platform is planned to integrate with job-listing APIs so students can discover current:

- Co-op positions
- Internships
- Entry-level opportunities

Users will eventually be able to view job opportunities alongside company reviews, allowing them to research a company before applying.

---

## Future Resume Analysis Feature

A future goal is to create a resume-to-job matching tool.

Users would be able to upload their resume and compare it with a selected job description.

The tool could provide feedback such as:

- Skills that match the job description
- Skills or qualifications that may be missing
- Relevant experience from the resume
- Resume improvement suggestions
- Personalized application feedback

This feature is currently a future concept and has not yet been implemented.

---

## Core Data Model

The initial database will likely contain four main categories.

### Companies

Possible fields:

- Company name
- Industry
- Location
- Company size
- Description

### Co-op Positions

Possible fields:

- Job title
- Company
- Division or team
- Location
- Pay range
- Co-op term
- Position description

### Reviews

Possible fields:

- Overall rating
- Workload rating
- Work environment rating
- Learning value
- Mentorship quality
- Pay satisfaction
- Responsibilities
- Typical hours
- Position requirements
- Recommendation
- Written review

### Users

Possible fields:

- User ID
- Email
- Username
- Account creation date
- Submitted reviews

---

## Planned Development Roadmap

### Phase 1 — Project Setup

- [ ] Design database schema
- [ ] Create React/Vite project
- [ ] Configure Git/GitHub repository
- [ ] Create Supabase project
- [ ] Connect frontend to Supabase

### Phase 2 — Basic Website

- [ ] Create navigation bar
- [ ] Create homepage
- [ ] Create company listing page
- [ ] Create co-op position page
- [ ] Create review display page

### Phase 3 — Database

- [ ] Create Companies table
- [ ] Create Co-op Positions table
- [ ] Create Reviews table
- [ ] Create Users table
- [ ] Add sample companies and positions
- [ ] Display database information on the website

### Phase 4 — Search & Filtering

- [ ] Search companies
- [ ] Search co-op positions
- [ ] Filter by industry
- [ ] Filter by location
- [ ] Filter by rating
- [ ] Filter by pay range

### Phase 5 — User Accounts

- [ ] Add user registration
- [ ] Add login/logout
- [ ] Add university email verification
- [ ] Allow users to submit reviews
- [ ] Allow users to edit/delete their own reviews

### Phase 6 — Job Opportunities

- [ ] Research job-listing APIs
- [ ] Integrate job API
- [ ] Display available co-op and internship positions
- [ ] Connect job opportunities with company pages

### Phase 7 — Resume Matching

- [ ] Allow users to upload or paste a resume
- [ ] Allow users to select a job description
- [ ] Compare resume content with job requirements
- [ ] Identify matching and missing skills
- [ ] Generate personalized resume feedback

---

## Initial MVP

The first version of Rate My Co-op will focus on a smaller set of features:

1. View companies
2. View co-op positions
3. Read company and position reviews
4. Search for companies
5. Filter co-op positions
6. Create an account
7. Submit a review

Additional features such as job APIs and resume analysis will be added after the core platform is functional.

---

## Project Goal

Rate My Co-op aims to make the co-op search process more transparent.

Students often have access to job descriptions, but those descriptions do not always explain what the day-to-day experience is actually like.

By collecting student experiences in one place, Rate My Co-op hopes to help students answer questions such as:

- What will I actually be doing?
- What skills should I have before applying?
- Is the company a good place to work?
- Will I learn useful skills?
- What is the work environment like?
- Is the position worth applying for?
- How much should I expect to be paid?

---

## Contributors

This project is currently being designed and developed as a student-led software project.

---

## Disclaimer

Rate My Co-op is an independent student project and is not affiliated with Northeastern University or any company listed on the platform.

All reviews will represent individual user experiences and opinions.
