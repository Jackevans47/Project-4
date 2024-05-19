# Project-4

### User Stories

#### **First Time Visitor Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/Jackevans47/Project-4/issues/1)| As a First Time Visitor, I want to be able to easily understand the main purpose of the app, so that I can learn more about this app.|
|[#2](https://github.com/Jackevans47/Project-4/issues/2)|As a First Time Visitor, I want to be able to easily navigate through the app, so that I can find the content.|
|[#3](https://github.com/Jackevans47/Project-4/issues/3)|As a First Time Visitor, I want to be able to register my account, so that I can learn the benefits of the app as a user.|
|[#4](https://github.com/Jackevans47/Project-4/issues/4)|As a First Time Visitor, I want to be able to find the app useful, so that it encourages me to return to the app.|

#### **Frequent Visitor Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#5](https://github.com/Jackevans47/Project-4/issues/5)|As a Frequent User, I want to be able to log in to my account, so that I can have an account.|
|[#6](https://github.com/Jackevans47/Project-4/issues/6)|As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account with ease.|
|[#7](https://github.com/Jackevans47/Project-4/issues/7)|As a Frequent User, I want to be able to easily recover my password in case I forget it, so that I can recover access to my account.|
|[#8](https://github.com/Jackevans47/Project-4/issues/8)|As a Frequent User, I can be able to change my password, so that I can keep my account safe in case my password becomes public.|



### Wireframes

- [Desktop Wireframes]
- ![About desktop](https://github.com/Jackevans47/Project-4/assets/148341732/9f6faf61-edb1-47ed-8f07-1f2eeb16945c)
![Delete profile desktop](https://github.com/Jackevans47/Project-4/assets/148341732/8300709c-2367-4331-a2fa-1ccbb1a29e82)
![Edit profile desktop](https://github.com/Jackevans47/Project-4/assets/148341732/ef4bed7b-e334-43ed-9516-b0b89e5cfcf4)
![Home desktop](https://github.com/Jackevans47/Project-4/assets/148341732/7bd6c4b0-4a4d-4f49-84ce-03599add64b0)
![Log in desktop](https://github.com/Jackevans47/Project-4/assets/148341732/1bc92555-e477-43da-825e-bd973da3bd32)
<img width="1220" alt="Sign up page desktop" src="https://github.com/Jackevans47/Project-4/assets/148341732/952b36f8-80ce-4b1d-931b-02e71dad442f">

---

- [Tablet Wireframes]
- ![About tablet](https://github.com/Jackevans47/Project-4/assets/148341732/4f7ac352-9246-42db-94f7-75372526b993)
![Delete profile tablet](https://github.com/Jackevans47/Project-4/assets/148341732/edbf4256-c67f-4368-9fb3-3ab37437c90b)
![Edit profile tablet](https://github.com/Jackevans47/Project-4/assets/148341732/d2dceb9b-412a-4787-b22a-588e64deacd4)
![Home tablet](https://github.com/Jackevans47/Project-4/assets/148341732/5b4a5d78-5156-4894-a25f-ab8fad71689c)
![Log in tablet](https://github.com/Jackevans47/Project-4/assets/148341732/93ac6195-ab0f-4695-a793-eb6f6a283ce3)
![Sign up tablet](https://github.com/Jackevans47/Project-4/assets/148341732/57103b61-a484-48dc-9ce0-abd2cb0e8787)

---

- [Mobile Wireframes]
- ![About mobile](https://github.com/Jackevans47/Project-4/assets/148341732/c7105401-cfd3-40ad-a6e3-0feec0b771a7)
![Delete profile mobile](https://github.com/Jackevans47/Project-4/assets/148341732/9565f141-2e8c-443a-bafe-2966eaa09a36)
![Edit profile mobile](https://github.com/Jackevans47/Project-4/assets/148341732/91193437-dfd5-4ee2-a4db-f3b0f39c606c)
![Log in mobile](https://github.com/Jackevans47/Project-4/assets/148341732/41218696-8484-47d7-8875-86341e442a20)
![Home mobile](https://github.com/Jackevans47/Project-4/assets/148341732/b4e2174a-bcaf-4d68-877e-ce74766ec890)

---


### Entity-Relationship Diagram

* The ERD was created using [Draw.io](https://www.lucidchart.com/).

- [Database Scheme]()
![ERD](https://github.com/Jackevans47/Project-4/assets/148341732/b486a604-718a-46d4-accd-9d8badce261e)

### Data Modeling

1. **User**



| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| UserName      | username      | CharField     |  max_length=50, blank=False, null=True, unique=True    |
| Email         | email         | EmailField    | max_length=50, unique=True, blank=False, null=False    |
| First Name    | first_name    | CharField     | max_length=30, blank=False, null=False    |
| Last Name     | last_name     | CharField     | max_length=30, blank=False, null=False    |
| Phone Number  | email         | CharField     | max_length=30, blank=False, null=False    |

