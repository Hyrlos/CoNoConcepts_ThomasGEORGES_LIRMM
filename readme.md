## Readme

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
Two kind of feature representations:
- *Feature model*: a hierarchical diagram that visually illustrates the features, and their dependencies
- *Feature role model*: a feature model hierarchized by roles

**Process:**  
User-stories are used to identify the roles, features and create abstract features. They are the nodes and the leafs on the outputs models.  
The relations between the nodes and leafs are computed with FCA and RCA.

![UStoFM.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/UStoFM.png)

**Big picture**
![processCono.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/processCono.png)

**FCA and RCA Model**  
![USFeatureFCA.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/USFeatureFCA.png)

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


### Outputs:
#### Feature Model:
![exampleFMCONO.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/exampleFMCONO.png)

#### Feature Role Model:
![exampleFRMCONO.png](https://raw.githubusercontent.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/master/exampleFRMCONO.png)
