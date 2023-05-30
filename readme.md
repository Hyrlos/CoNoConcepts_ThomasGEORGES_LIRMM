## Readme
**Objective**   
Provide an automated process for feature models synthesis using Formal Concept Analysis and Relationnal Concept Analysis by leveraging User-stories and code merges.
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

![processCono](https://github.com/Hyrlos/CoNoConcepts_ThomasGEORGES_LIRMM/assets/36265996/0b6c5e7a-22dc-4f34-98ff-0e4554f9535d)

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

**Relationnal Concept Analysis**  
The relations between each objects are in their related Relationnal Concepts:  
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
