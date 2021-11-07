# EDA Course Project Introduction

## Summary

Say that you'd like to do some data work for an organization, but they aren't hiring. They might not even know that they could benefit from the data science services of a skilled practitioner like you. How can you get their attention?  

For this project, you are going to deliver a preliminary analysis to your target organization (“client”) to try to get your foot in the door. Your job is to lay out a case that your skills and insights are useful for their unique needs.

To do this, you will take advantage of free, accessible data about the patterns of transit traffic in New York City: [MTA turnstile data](http://web.mta.info/developers/turnstile.html). Using this data source, as well as any other relevant dataset(s) of your choosing, perform an exploratory analysis in Python and SQL that offers insightful and actionable quantitative findings (including visualizations) to your client. Communicate your process and findings in a 5 minute presentation at the end of week 2 and a short written description.

## About MTA: 

The Metropolitan Transportation Authority is North America's largest transportation network, serving a population of 15.3 million people across a 5,000-square-mile travel area surrounding New York City through Long Island, southeastern New York State, and Connecticut.

The MTA network comprises the nation’s largest bus fleet and more subway and commuter rail cars than all other U.S. transit systems combined. The MTA's operating agencies are MTA New York City Transit, MTA Bus, Long Island Rail Road, Metro-North Railroad, and MTA Bridges and Tunnels.

## MTA Turnstile Data:
Data obtained from http://web.mta.info/developers/turnstile.html.

## Field Description:

| Field Name | Description                                                                     |
|------------|---------------------------------------------------------------------------------|
| C/A        | Control Area (A002)                                                             |
| UNIT       | Remote Unit for a station (R051)                                                |
| SCP        | Subunit Channel Position represents an specific address for a device (02-00-00) |
| STATION    | Represents the station name the device is located at                            |
| LINENAME   | Represents all train lines that can be boarded at this station                  |
| DIVISION   | Represents the Line originally the station belonged to BMT, IRT, or IND         |
| DATE       | Represents the date (MM-DD-YY)                                                  |
| TIME       | Represents the time (hh:mm:ss) for a scheduled audit event                      |
| DESC       | Represent the "REGULAR" scheduled audit event (Normally occurs every 4 hours)   |
| ENTRIES    | The comulative entry register value for a device                                |
| EXITS      | The cumulative exit register value for a device                                 |


## Example:

The data below shows the entry/exit register values for one turnstile at control area (A002) from 09/27/14 at 00:00 hours to 09/29/14 at 00:00 hours

### C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS.<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,00:00:00,REGULAR,0004800073,0001629137<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,04:00:00,REGULAR,0004800125,0001629149<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,08:00:00,REGULAR,0004800146,0001629162<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,12:00:00,REGULAR,0004800264,0001629264<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,16:00:00,REGULAR,0004800523,0001629328<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-27-14,20:00:00,REGULAR,0004800924,0001629371<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,00:00:00,REGULAR,0004801104,0001629395<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,04:00:00,REGULAR,0004801149,0001629402<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,08:00:00,REGULAR,0004801168,0001629414<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,12:00:00,REGULAR,0004801304,0001629463<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,16:00:00,REGULAR,0004801463,0001629521<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-28-14,20:00:00,REGULAR,0004801737,0001629555<br>
A002,R051,02-00-00,LEXINGTON AVE,456NQR,BMT,09-29-14,00:00:00,REGULAR,0004801836,0001629574<br>


### Your backstory
This is a fairly free-form project, and creativity is welcome. Be sure that there is enough time to do good work with the data, but it is fine to tinker with the premise of the project.
The client organization can be real or imaginary, a private company or a social sector group, anything you desire. For instance, you may decide that a non-profit organization has approached you, soliciting your help. Here's an example email that a former group "received" from a non-profit: [Example Client Email](example_client_email.md).


## Components
Metis projects are broken down into 5 component parts -- **design, data, algorithms, tools, and communication** -- that 
are each scored individually. Below is a description of each component as it relates to this project. For more detail 
on how these components are graded and how extra points are rewarded, refer to the [project success guide](./project_success_guide.md).  


### Design:

*  The project should include a clearly defined backstory that satisfies a specific need for the client organization. It should be centered around discovering useful, actionable insights that inform your client about the movement of people in the city.
*  All **deliverable deadlines should be met**, reflecting **professionalism** and **effective scoping and workflow**

### Data:

* The primary data source should be [MTA turnstile data](http://web.mta.info/developers/turnstile.html) 
* Aim to use at least 3 months worth of data; consult with an instructor if you are considering deviating from this rule of thumb, which may vary depending on your use case
* You are welcome and encouraged to incorporate any additional, relevant data sources 
 
### Algorithms

* Perform a thorough Exploratory Data Analysis of the MTA turnstile data; clean, explore, aggregate, and visualize the data as appropriate to address the client's problem 
* The MTA Analysis Pairs [1](../../pairs/mta-pair-1), [2](../../pairs/mta-pair-2), and [3](../../pairs/mta-pair-3), 
which we'll cover over the next few days, will help you get started with your data exploration

### Tools
* **Ingesting the raw data into a SQL database** and **querying from that database into Python via SQLAlchemy** is required; exploratory analysis and data cleaning in SQL is optional
* **Exploratory data analysis in pandas** is required
* **Python visualization libraries** (such as matplotlib and seaborn) are required   
*  Other tools not covered in the course are optional but welcome
- Major examples of applicable tools not covered in the course:
  - *Processing* tools could include Google Cloud or Amazon Web Services for cloud computing resources
  - *Visualization* tools could include more advanced python libraries such as Bokeh and Plotly or resources outside of Python such as Tableau


### Communication:
* Students will deliver a **5 minute slide presentation** at the end of the course. These should be given in a compelling, 
clear manner and include effective visuals for communicating your objectives and findings.
* You will also submit a **~1 page written description** summarizing your work: it should begin with a **~100 word abstract**
to be followed by a breakdown of your project along the 5 major components.
  

## Deliverables:

**Please submit all project deliverables through the [Student Submissions Form](https://docs.google.com/forms/d/e/1FAIpQLSeM7MPx5r_FaX6ordJGkG1ObLh94GEE8qzlvEFxfvmWsKmXNA/viewform)**. All project deliverables and code should be uploaded to a personal, project-specific GitHub repository. Click [here](https://github.com/thisismetis/Metis_Fundamentals/tree/main/git_and_github) for instructions on how to set up a personal repo. 

**For exact deliverable dates, refer to the main schedule [here](/README.md).**
  
**For exact deliverable details, refer to the (linked) Metis Fundamentals project deliverable templates**.

 * [Project proposal](https://github.com/thisismetis/NBM_Metis_Fundamentals/tree/master/project_deliverable_templates/project_proposal.md): short description shared with instructors
    - Additionally, students may meet with an instructor for a scope meeting
 * [Minimum Viable Product (MVP)](https://github.com/thisismetis/NBM_Metis_Fundamentals/tree/master/project_deliverable_templates/mvp.md) submission  
 * [Written description, presentation slides PDF, and project code](https://github.com/thisismetis/NBM_Metis_Fundamentals/tree/master/project_deliverable_templates/final_deliverable.md) 
 * Project presentation
 
## Example Code
[MTA Turnstile Data Analysis - Kaggle](https://www.kaggle.com/nieyuqi/mta-turnstile-data-analysis)
