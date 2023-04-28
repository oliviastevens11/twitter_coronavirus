# Coronavirus twitter analysis

The map reduce project involved processing a zip file containing tweets for an individual day and tracking the usage of hashtags on both a language and country level. This was accomplished by creating a mapping function that processed the zip file, and then reducing the resulting files with ".lang" and ".country" extensions into separate files.

The project then used the reduced files to generate a bar chart that displayed the top 10 countries and languages that used the hashtags "#coronavirus" and "#코로나바이러스". This code can be found in the visualize.py file. Finally, the alternative_reduce.py file plots a line graph of the individual hashtags. When I ran the file, I gave it the input of "virus" and "fl
u". The code can take any number of hashtags and plot in graph.

Overall, this project taught me how to handle and visualize large datasets. As we look toward the future, this project has potential applications in tracking other social media's usage of certain words or phrases. Below find the bar charts and line plot. 


# Graph of Top 10 Countries that used #coronavirus
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Countries:%20%23coronavirus.png)

# Graph of Top 10 Countries that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Countries:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)

# Graph of Top 10 Langauges that used #coronavirus  
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Languages:%20%23coronavirus.png)

# Graph of Top 10 Langauges that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Languages:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)

# Line Plot of the Use of Two Hashtags throughout 2020: "#virus" and "#flu"
This can be ran for any of the hashtags. I choose virus and flu, as I believe they would have so similarities in their usage. 
![alt_text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/line_plot_hastag.png)
