# Week 1: GitHub, command line, and our first forecast

This readme has the instructions for the first week of class. Every week you will find a readme similar to this outlining the activities and instructions you will need as well as the weekly forecasting assignment.

____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Setup Instructions](#github)
  - [ GitHub Install](#githubinst)
  - [ Repo Cloning](#repo)
  - [ Text Editor](#atom)
1. [ Homework Setup](#classroom)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)
1. [ Cheat Sheet Assignment](#assignment2)

___
<a name="todo"></a>
## To Do List
1. Follow all of the instructions in the [Setup Instructions Part 1](#setup) to install the necessary software and get the course repo's cloned. You should be able to do all of the steps except the homework repo **before class this Thursday**.
1. Email Laura your GitHub user name and email address by **Wednesday at 5pm**.
3. Once you get the homework assignment invitation follow the Setup Instructions Part 2 to get your homework repo setup and cloned.
2. Complete the required GitHub and command line tutorials in the [training activities](#training) section as soon as possible but before next week.
3. Submit your first streamflow forecast and assignment by **noon on Monday** (see forecast submission instructions).
4. Create a GitHub Cheat Sheet for yourself which will be due by **class Next Thursday** (see Cheat Sheet Instructions)


___
<a name="setup"></a>
## Setup Instructions Part 1 - GitHub, GitKraken and Atom
<a name="githubinst"></a>
#### 1. Setup account and install GitHub
  1.  Register for account on GitHub: <https://github.com/>
  2. Check if you have GitHub installed and if not install it.  Directions for both Windows & Mac [here](http://happygitwithr.com/install-git.html). Windows users should follow Option 1 in 6.2. Mac users can follow Option 1 in 6.3.
  3. Setup options in Git. If you have a Mac, you can go to the terminal (Applications -> Utilities -> Terminal) as shown above. If you have a Windows, open Git BASH, which you should have downloaded.  You will need to  setup you [username](https://help.github.com/en/github/using-git/setting-your-username-in-git) and your [email](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address). Note thatyou just need to
  4. Generate a SSH key so you don’t need to enter your password every time you interact with GitHub. Instructions for this can be found [here](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

<a name="GitKraken"></a>
#### 2.	Install **GitKraken** and link to your GitHub account
  1. This is a handy GUI for working with Git Repos. You can get it on the GitKraken website (www.gitkraken.com/). No need to worry about boards or timelines for now you can just install the free GUI.
  2. You can also get a free upgrade to Git Kraken pro as a student if you go[here](https://education.github.com/pack?utm_source=github+gitkraken). This willlet you work with private as  well as public repos using Git Kraken.
  3. After you have installed GitKraken follow the instructions [here](https://support.gitkraken.com/integrations/github/) to link to your GitHub account. **Note:** you can stop at the 'Oauth step' but make sure you do the **Generate SSH** step.

<a name="repo"></a>
#### 3. Clone the course materials repo to your computer
- Before you clone I recommend you start by creating a directory for this class where you will keep all of your repos. **NOTE:** It is best to create this directory as a local directory on your computer don't put it on OneDrive if you are using that.  I recommend you name this directory `HAS_Tools`
- *GitKraken Approach*
  - In *GitKraken* got to `File/Clone Repo`
  - Use the `Browse` button to navigate to the directory you created for the class that you want your repo cloned to.
  - To get the `URL` open a web browser and go to the [GitHub organization](https://github.com/HAS-Tools-Fall2021) for this course, click on the `Course-Materials21 Repo` and click on the green `code` button **make sure `ssh` is underlined** as the method to be used.
  - When you do this you should see a url for the repo with a clipboard symbol next to it. Click on the clipboard to copy the URL.
  - Paste this into the `URL` field in *GitKraken*

- *Command Line Approach*
    - **NOTE:** The *GitKraken* approach is a little easier but it is good to know that you can do this multiple ways. So you might want to create a different directory and practice cloning this again.
    - Make a directory for this class wherever you would like to have it on your computer
    - Open a terminal window and navigate to your course directory (you can do this using the commands cd and pwd)
    - Clone the main course materials repo: `git clone [ADD SSH]`
    - *if your ssh keys aren't setup you can also clone it like this* `git clone [ADD LINK]`

<a name="atom"></a>
#### 3.	Install the **Atom text editor**
 - This is a great text editor that has GitHub integration.You can install it for Mac or Windows [here](https://atom.io/)

___
<a name="classroom"></a>
## Setup Instructions Part 2 - Homework and GitHub Classroom
1. Once you have setup your GitHub account and cloned the course repo use the following link to make your own homework repo: : https://classroom.github.com/a/tdtRAvpF

  - Follow the instructions from the link and you should see a repo created in our GitHub organization with your name on it [here](https://github.com/HAS-Tools-Fall2021)
  -  *Note:* After you accept an assignment for the first time, we will send you an invite to join the classroom organization as a member. **Please accept this.** You will probably get an email with the invitation, but you should also see a link at the top of your main GitHub page.

2. Clone your homework repo to your course work directory following the same steps you did to clone the course materials repo. **NOTE:** *DO NOT* clone your homework repo into the `Course-Materials` repo you already cloned. Just clone this into your main folder for the class so its sitting side by side with the `Course-Materials` repo

      *Note:* If you received an error in the above steps, you may have to clone with HTTPS instead of SSH. You can do this by again clicking on the "Clone or Download" button in the repository page, then clicking "Use HTTPS" in the top right of the pop-up box. Now copy the link and repeat this step.

___
<a name="training"></a>
## Required Training Activities
1. Read and do the exercises of Intro to Earth Data Science **Chapter 2** on Bash and Shell
  - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/) Intro to Bash
  - [lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/bash-commands-to-manage-directories-files/) Bash Commands
2. Read **Chapter 7** Intro to Earth Data Science on the basics of GitHub
  - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/) What is Version Control?
  - [Lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/fork-clone-github-repositories/) Get files from GitHub
  - [Lesson 3](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/git-commands/) Git Commnad for Verion control
  - [Lesson 4](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/git-undo-local-changes/) Undo local changes with Git


## Additional Optional Training activities
If you want more practice check these out:
1. More command line practice: [Chapter 3 of The Unix Workbench](https://seankross.com/the-unix-workbench/command-line-basics.html#navigating-the-command-line) try the exercises in sections 3.1-3.4. Note that for Mac users you will use **Terminal** and for Windows users you should use **Git Bash** to complete these exercises.
2. Even more command line practice:  [crash course](https://learnpythonthehardway.org/book/appendixa.html)
3. Another [Github tutorial](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6) with practice exercises
4. A GitHub tutorial setup as a [game](https://learngitbranching.js.org/)
5. Do this [intro to GitHub tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

___
<a name="assignment"></a>
## Assignment 1: First Forecast
This week you will generate your first streamflow forecast. The rules for this forecast are simple you will use only Excel to generate your forecasts and the most complicated mathematical operation you can do is take an average. You should make your forecast by simply looking at the historical streamflow and making your best guess of what you think it will be in the future based on whatever logic you want (no fancy calculations!). Don't worry we will get more sophisticated from here, but this week we start basic.

#### 1. Download the stream gauge observations to your homework repo
 The USGS NWIS website has all of the USGS maintained observation sites in the country. Go to their main [website](https://waterdata.usgs.gov/nwis) or their [mapper](https://maps.waterdata.usgs.gov/mapper/) and download the following daily streamflow data for station  *09506000 Verde River Near Camp Verde* using the following parameters:
   - Daily Data
   - Parameter 00060 Discharge (mean)
   - Start date = 1989-01-01
   - End date = Today
   - Select 'tab separated'

- The data will load in a new tab of your browser. Right click and save it as a *streamflow_week1.txt* file in the *data* folder of your **homework repo**.

### 2. Import the data into Excel to look at it
- Open a new Excel workbook and copy and paste the text file into it.
- Use the `text to columns` option in the `data menu` and select `delimited` and by `tabs` to separate the data into columns (If tab doesn't work you can also delimit by `space`)
- Save your workbook as *streamflow_week1.xlsx* in the *assignment_1* folder.
- Read the documentation at the top of the file to understand the format of the data you have downloaded.
- Look at the streamflow values and decide what your forecasted flows will be (remember no math is expected here, the idea here is just to take a look at the historical flow and use your own judgement to make a forecast).  You need to make two forecasts all of which should be expressed as average daily flow in cfs (1) flow next week, (2) flow two weeks from now.

### 3. Submit your first forecast to the competition
- Clone the main class Forecasting repo from our course organization website [GitHub](https://github.com/HAS-Tools-Fall2021) (see instructions above and remember **DO NOT clone it inside another repo** just clone it into the directory for this class next to your others)
- Open the repo in GitKraken. To avoid conflicts make sure your local repo is up to date before you submit your forecast. You can do by pushing `pull` button on GitKraken.
- Find the csv with your last name in the *forecast_entries* folder and enter your forecasts. Enter your forecasts on the row for foercast #1. A few notes:
    - Make sure you just enter numbers (i.e. enter 5 not 5 cfs)
    - Don't convert the file to an xlsx file keep it as a csv.
    - the one '1week' and '2week' refers to your forecasts for next week and the following week.  You can refer to the `forecasts_dates` files in the Forecast repo for more details.
- Save your changes. THen in GitKraken, Stage, commit, and push your changes (see the example video for how to do this).

### 4. Submit your first forecast homework assignment
In addition to submitting your numerical forecasts to the forecast competition you also need to submit a description of your forecast through your homework repo. This is what I will be grading for credit.

- Create a file named `lastname_HW1.md` in the `submission` folder of your homework repo. The easiest way  to do this is just to create a new file in atom.

- Include a header in your file that includes, your name, the date, and the assignment number

- Write a few sentences describing the forecast you made and rational for making it.  Note that we aren't doing anything fancy this week so your rational can be very simple, I'm not looking for a lot of text or any external research. This is really just to practice getting files submitted on GitHub. Save your file.

- When you are done open yor homework repo in GitKraken and  `Stage`, `Committ`, and `Push` your changes to upload your changes.

___
<a name="assignment2"></a>
## GitHub Cheat Sheet assignment:
- Over the course of the semester you will be creating a series of Cheat Sheets' to summarize the different concepts we cover. You can refer to the Cheat Sheets in the `Content` Folder for examples.
- It is entirely up to you though what yours should look like and note that you already have the ones I provided you so it doesn't need to be a duplicate of that. The point is for you to have a concise guide in your own words that will be helpful to you and that you can refer back to.
- This might take the form of a word document, a powerpoint slide, or even a hand written or drawn diagram, a jupyter notebook or pythhon script (when we get to those) or something more creative that I'm not thinking of yet :)
- In general I'm looking for something the equivalent of 1-2 pages long.
- All Cheat Sheet assignments will be graded pass/fail. If I determine yours needs work you will be able to resubmit the following Tuesday with a revised version.
- This week your Cheat Sheet should cover at a minimum:
  1. What is GitHub and version control
  2. What is a repo
  3. The difference between local, remote, origin
  2. The major actions and what they mean - Clone, Fork, Commit, Push, Pull, Fetch (note this could lend itself to a graphic illustration)
