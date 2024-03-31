# SC4052-Cloud-Computing

## This is the implementation for the **Individual Assignment 2** of the **Cloud Computing** Course.
In this assignment, I implemented the Pagerank Algorithm, the famous algorithm that runs behind the Google Search Engine.
Pagerank, introduced in 1998 by **Larry Page** and **Sergey Brin**, is a mathematical formula to help rank the webpages based on the importance of each webpage. 

<img width="1180" alt="methodology" src="https://danielctw.com/wp-content/uploads/2007/10/google-PR.jpg">
Image source: https://danielctw.com/wp-content/uploads/2007/10/google-PR.jpg

### Installation
```
git clone https://github.com/KelvinDo183/SC4052-Cloud-Computing.git
cd SC4052-Cloud-Computing
conda create -n pagerank python=3.8
conda activate pagerank
pip install -r requirements.txt
```

### Graph Visualisation
Before running, which graph to be visualized needs to be chosen. A list of available graphs can be found under **/Graph** Folder.
After making changes to the Python file, simply run:
```
python Visualisation.py
```

### Random Graph Generation
Besides the graphs provided, users can easily create random graphs. 
Before running, hyperparameters about the number of nodes and edges must be specified.
After making changes to the Python file, simply run:
```
python Create_Random_Graph.py
```
After executing, a new graph will be created under the **/Graph** folder.

### Pagerank 
Before running, which graph needs to be chosen to run. A list of available graphs can be found under the **/Graph** Folder.
After making changes to the Python file, simply run:
```
python Pagerank.py
```
After executing, the analysis and the experiment results will be displayed and saved under **/Visualisation_Results**.
### Pagerank with MapReduce/Pyspark
In this experiment, MapReduce is implemented using the Python framework, **PySpark**. Please note that in this code, I do not implement **Random Walker**, which results in the case that the dangling nodes will have the most weight
Before running, which graph needs to be chosen to run. A list of available graphs can be found under the **/Graph** Folder.
After making changes to the Python file, simply run:
```
python Pagerank_MapReduce.py
```

## Conclusion
Pagerank is a powerful tool for ranking web pages. Through the experiments, I have more hands-on experience with famous algorithms. In the future, I want to explore integrating neural networks. One question: <b>Is there a better way to do this with the Random Walker or Transition Matrix? <b>. This might involve exploration of more **Stochastic Processes** rather than Random Walk to get a better result. 
