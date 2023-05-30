**Objective**  
Provide an automated process for feature models synthesis using Formal Concept Analysis and Relationnal Concept Analysis by leveraging User-stories and code merge.

**Inputs:**
- Dataset extracted from Github or Gitlab:
  - User-stories title and request anwser
  - The user-stories related products
  - The user-stories related merges
  - The merges related changes
  - The changes related Files
  - The changes related Code Diff
  
**Outputs:**
- Feature model
- Feature role model  

**Process:**  
User-stories are used to identify the roles, features and create abstract features. They are the nodes and the leafs on the outputs models.  
The relations between the nodes and leafs are computed with FCA and RCA.

**Formal Concept Analysis:**  
Each object from VCS is represented with a Formal Context:   
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
The relations between each objects are in there related Relationnal Concepts:  
- Products x User-stories  
- User-stories x Roles
- User-stories x Features
- Features x Abstract features
- User-stories x Merges
- Changes x Files
- Changes x Code diffs

**Tools:**
- FCA4J to perform Formal concept analysis
- RCFT file extension for FCA and RCA data representation
- Elbows, Kmeans and Word2Vec for Clustering 
- FeatureIDE for Feature Models vizualisation
