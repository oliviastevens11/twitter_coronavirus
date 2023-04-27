# Coronavirus twitter analysis

The map reduce project involved processing a zip file containing tweets for an individual day and tracking the usage of hashtags on both a language and country level. This was accomplished by creating a mapping function that processed the zip file, and then reducing the resulting files with ".lang" and ".country" extensions into separate files.

The project then used the reduced files to generate a bar chart that displayed the top 10 countries and languages that used the hashtags "#coronavirus" and "#코로나바이러스". Finally, the outputs file was run through again to plot a line graph of the individual hashtags.

Overall, this project taught me how to deal with large datasets and has potential applications in tracking other social media usage. 

Graph of Top 10 Countries that used #coronavirus
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Countries:%20%23coronavirus.png)
Graph of Top 10 Countries that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Countries:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)
Graph of Top 10 Langauges that used #coronavirus  
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Languages:%20%23coronavirus.png)
Graph of Top 10 Langauges that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Languages:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)
