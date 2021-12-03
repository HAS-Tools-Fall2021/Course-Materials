# Week 15: Computing resources
This week we are going explore how you can access and use computing resources beyond your laptop.
___
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#references)
1. [ Instructions](#instructions)
1. [ Assignment](#assignment)
___
<a name="todo"></a>
## To Do List
1. Modify your forecast script so it is easy to transport.

2. Run your forecast script on two locations other than your laptop

2. Submit your homework assignment and your **final** forecast by **noon on Monday**:

___
<a name="references"></a>
## References and resources
**UA HPC**
- [UA HPC Main Page](https://public.confluence.arizona.edu/display/UAHPC)
- [UA HPC Quick Start](https://public.confluence.arizona.edu/display/UAHPC/Puma+Quick+Start)
- [UA HPC Training](https://public.confluence.arizona.edu/display/UAHPC/Training)
- [Portal for account management](https://portal.hpc.arizona.edu/portal/)
- [UA HPC OnDemand instructions](https://public.confluence.arizona.edu/display/UAHPC/Open+On+Demand)
- [UA HPC OnDemand Portal](https://ood.hpc.arizona.edu/pun/sys/dashboard)
- [Tutoral on running Python Jupyter Notbooks on UAHPC](https://public.confluence.arizona.edu/display/UAHPC/Using+and+Installing+Python)

**Cyverse**
 - [Cyverse](https://cyverse.org/)
 - [Cyverse getting started](https://learning.cyverse.org/en/latest/#cyverse-faq)

**Some Cloud Computing Examples**
- [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
- [My Binder](https://mybinder.org/)

**Docker**
- [Intro to Docker](https://docker-curriculum.com/)

___
<a name="instructions"></a>
## Quick Start Steps For logging in and running a job on UAHPC
These instructions are following [this tutorial](https://public.confluence.arizona.edu/display/UAHPC/Puma+Quick+Start)

1. Login to UA HPC. You can do this either from terminal line like this:
`ssh lecondon@hpc.arizona.edu` (This should work from GitBash but windows users might need to install putty for this to work) or you can login to the on-demand portal: <https://ood.hpc.arizona.edu/>. From the on demand portal you can then launch a terminal and follow along with these instructions the same as if you had launched a local terminal and ssh into HPC. In both cases you should select **Puma** as the location.

2.  To see where you are type `echo $HOSTNAME` this should return `login2`
Then use `va` to see what group you are a part of and what your allocation is.

1. Setup a Python environment (Note you only need to do this step once). The instructions below follow [this tutorial](https://public.confluence.arizona.edu/display/UAHPC/Using+and+Installing+Python). I recommend doing this with virtual env not conda but the idea is the same if you want to follow the conda instructions.
    - **NOTE**: In order to follow these instructions you first need to launch a terminal and type 'interactive' to launch an interactive session and get onto Puma.

2. Optional: Setup your environment to be active all the time. (if you prefer not to do this you can just module load and source your environment within a run script and as needed when you login).
  - `vi ~/.bashrc`
  - type `i` get into insert mode and then add the following two lines:
  ```
  module load python
  source ~/mypyenv/bin/activate
  ````
  - type `esc + shift + zz` to save
  - `source ~/.bashrc`

5. Create a directory for `HAS_tools`. You can do this with the file explorer from OnDemand or using mkdir from terminal

4. Upload some files to this directory. You can use the starter codes from previous weeks. Or you can just create your own really simple 'hello  world' python script (i.e. a python script with a print statement in it that says 'hello world')

2. Create a pbs script to submit your job. You can do this using the job builder tool: <https://jobbuilder.hpc.arizona.edu/>
  - select: 1 node, 1 core, for the standard queue
  - Create a run name and use lecondon for your group name
  - set your run time to 5  minutes
  - Create a new file in the folder with your python script (e.g. `run_python.sh`) and copy and paste the resulting bash file lines into that files
  - Add the following four lines to the bottom of the  script:
  ```
  module load python/3.8
  source ~/mypyenv/bin/activate

  cd /path/to/HAS_Tools
  python test.py
  ```
  - Note 1: Replace `/path/to` with the path to your HAS tools directory
  - Note 2: If the job won't submit you might need to change `cputime` to `cput`.

7. Submit your job like this: `sbatch run_python.sh`

8. check on the status of your job. You can do this one of two ways: 
- From terminal type:  `squeue -u yournetid` or you can just check on your one job like this: `squeue -u yourjob#`
- Or from on demand go to `jobs` and `active jobs` to see a list of your jobs that are queued, complete or running. 
NOTE: To see more slurm commands you can refer to the the table [here](https://public.confluence.arizona.edu/display/UAHPC/Running+Jobs+with+SLURM)

9. Use vi to look at the outputs of your job in the two files that are created `runame.orunnumber` and `runname.erunnumber`

___
<a name="assignment"></a>
## Assignment 15: Supercomputing!
This week we are going to voyage off our our laptops. Your job is to make your script portable and run your forecast on Ocelote and one other location of  your choosing (i.e. two locations total)

#### Assignment

**Part 1: Run your forecast on Puma using a submit script**
1. On your laptop modify your python script so that it will not need to be run interactively (i.e. so that you can run it from command line like this `python myscrip.py` and it will print out and save everything that you want). Also make sure it is setup so that any file it needs is in the same directory to make paths easier. You can test this by opening a terminal from within vscode and trying to run your script from there.  You can also simplify your script so that you don't need as many packages if you would like. No maps are required for this weeks submission.

2. Setup your environment and make a directory to work in on UA HPC see the instructions above (this should already be done from class)

3. Upload your script and inputs to your HAS_Tools folder on UA_HPC

4. Modify your job submisison script so that rather than running hello_world.py it runs your homework script.  This should be the only like you need to change in this script. If your script takes longer than 5 mintues to run though you might also want to request more time.  

5. Submit your job from the terminal: 
`sbatch run_python.sh`

6. Download your output file and pbs script for submission.

**Part 2: Run your forecast using an interactive session jupyter notebook**
- Next try converting your script to a jupyter notebook on your laptop
- Upload this notebook to UA HPC
- Try runing by launching an interactive jupyter session through open on demand. 

**BONUS**
- If you ahve extra time feel free to try running your script on google co-lab too!

**Part 3: Reflection**
With your submission please provide a readme that answers the following questions:

1. What resources did you request on Puma? How long did you wait in the queue for your job to run and how long did it take to run?
2. What was the most confusing part to you about setting up and running your job on Puma?
3. What questions do you still have after doing this?


#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions for the one and two week forecasts and up to August 21st for the 16 week forecast.

#### Submission Instructions
1. Submit your forecast to the forecast competition following normal procedures.
2. Create a `Week15` folder in your `Forecast_Submissions` folder of your homework folder and submit the following:
  - The output file generated from your run `runname.orunnumber`
  - The python script you ran
  - The submission script you created
  - Your written discussion `LastName_HW15.md`
