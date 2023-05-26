# Readme
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
User-stories are used to identified the roles, features and create abstract features. They are the nodes and the leafs on the outputs models.  
The relations between the nodes and leafs are computed with FCA and RCA.

<div>
<img src="https://github.com/Hyrlos/Bridging-the-Gap-between-User-Stories-and-Feature-Models-by-Leveraging-Version-Control-Platform/assets/36265996/3b8910c9-2f6e-444a-a5dd-e969f9fd2392" width="600"/>
</div>

**Version Control System(VCS) modelised with for FCA and RCA:**

<div>
<img src="https://github.com/Hyrlos/Bridging-the-Gap-between-User-Stories-and-Feature-Models-by-Leveraging-Version-Control-Platform/assets/36265996/b13605b5-16aa-4ca2-aa04-14322c835932" width="600"/>
</div>


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
