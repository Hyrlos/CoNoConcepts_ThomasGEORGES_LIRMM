# From user stories to feature models
## Context
The Software Product Lines (SPL) are now a well-established way to efficiently produce highly-configurable software products. However, migrating an existing software family into an integrated SPL platform is still challenging and organizations may be reluctant to adopt the approach. Hesitations often arise from the lack of standard procedures guiding the process, as well as doubts on the cost/benefit ratio. Although companies own large bases of well-documented code, they still manually build tailored applications from the base code to meet their clients' requirements, sometimes with a clone-and-own strategy.

One of the difficulties during the migration process is to extract a relevant feature model from the existing products. In this notebook, we address this difficulty in the context of products built with an agile process, specifically where requirements are defined using user stories, and a version control system  is used to store and trace project artifacts. User stories are nowadays widely used in a large part of software projects to define requirements. VCS platforms like GitLab or Github are widespread support not only to manage code artifacts but also as a central part of project management, directly using integrated tools to manage the user stories or integrating external tools in the VCS platform. Therefore, our approach is suitable for a large part of projects.

In this context, we have developed an automated feature model synthesis approach based on the knowledge collected from the user stories and the way they are linked to the product code through traceability links established in the VCS.

### Rough view: A Step in migrating a set of similar software into a Soft. product line

**From existing products**  
![fromExistingProducts.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/fromExistingProducts.png)  


**To a feature model**  
![ToAFeatureModel.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/ToAFeatureModel.png)  

## Readme

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/HEAD?labpath=CoNoConcepts_ThomasGEORGES_LIRMM%20.ipynb)

**Objective**   
Provide an automated process for feature models synthesis using Formal Concept Analysis and Relational Concept Analysis by leveraging User-stories and code merges.
All the source code is available in a [Github repository](https://github.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM)

**Inputs:**  
- Dataset extracted from Github or Gitlab:
  - User-stories title and request anwser
  - The user-stories related products
  - The user-stories related merges
  - The merges related changes
  - The changes related Files
  - The changes related Code Diff
  
**Outputs:**  
Two kinds of feature representations:
- *Feature model*: a hierarchical diagram that visually illustrates the features, and their dependencies
- *Feature role model*: a feature model hierarchized by roles

**Process:**  
User-stories are used to identify the roles, features and create abstract features. They are the nodes and the leafs on the outputs models.  
The relations between the nodes and leafs are computed with FCA and RCA.

**Big picture**  
![processCono.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/processCono.png)  

**From User stories to logical constraints**   
![UStoFM.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/UStoFM.png)  



**FCA and RCA Model**  
<div>
<img src="https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/USFeatureFCA.png" width="800"/>
</div>

**Formal Concept Analysis:**  
Each object from Version Control System is represented with a Formal Context:   
- User-stories
- Products
- Roles
- Features
- Merges
- Changes
- Code diffs
- Files
- Abstract features

**Relational Concept Analysis**  
The relations between each objects are in their related Relational Concepts:  
- Products x User-stories  
- User-stories x Roles
- User-stories x Features
- Features x Abstract features
- User-stories x Merges
- Changes x Files
- Changes x Code diffs

**Tools:**
- [FCA4J](https://www.lirmm.fr/fca4j/Introduction.html) to perform Formal concept analysis
- [RCFT](https://www.lirmm.fr/fca4j/Family.html) file extension for FCA and RCA data representation
- [FeatureIDE](https://featureide.github.io/) for Feature Models vizualisation
- Elbows, Kmeans and Word2Vec for Clustering 

### Input:

| usID     | US                                                                                  |
|----------|--------------------------------------------------------------------------------------------|
| 1        | As a farmer , I can refresh the predicted weather                                          |
| 2        | As a farmer, I can CRUD plots                                                              |
| 3        | As a farmer with a plot, I can edit the parameters of a plot (current season)              |
| 4        | As a farmer with a plot, I can sort my plots in the list                                   |
| 5        | As a farmer with a plot, I can filter my plots in the list                                 |
| 6        | As a farmer with a plot, I can export observation data for a plot                          |
| 7        | As a farmer with a plot, I know when my plots will be in danger                            |
| 8        | As a farmer irrigator, I can manage my irrigations and recommendations in my favorite unit |
| 9        | As a farmer irrigator, I choose my preferred irrigation unit in my user-settings           |
| 10       | As a farmer irrigator, I can view my irrigation recommendations in my favorite unit        |
| 11       | As a admin, I can CRUD a farmer                                                            |
| 12       | As a admin, I can relaunch all failed simulation                                           |


### Outputs visualized:
#### Feature Model with FeatureIDE:
![exampleFMCONO.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/exampleFMCONO.png)

#### Feature Role Model with FeatureIDE:
![exampleFRMCONO.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/images/exampleFRMCONO.png)

