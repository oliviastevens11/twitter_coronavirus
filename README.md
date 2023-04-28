# Coronavirus twitter analysis

The MapReduce project aimed to process a zip file containing tweets for a single day and track the usage of hashtags on both a language and country level. The project began by creating a mapping function to process the zip file, followed by reducing the resulting files with ".lang" and ".country" extensions into separate files.

Using the reduced files, the project generated a bar chart displaying the top 10 countries and languages that used the hashtags "#coronavirus" and "#코로나바이러스". The code for this can be found in the visualize.py file. Additionally, the alternative_reduce.py file plotted a line graph for individual hashtags. The code can plot any number of hashtags as required. In the line graphs below, I demonstrated the code's flexibility by plotting both two and three hashtags.

This project has provided me with an invaluable lesson on handling and visualizing large datasets. As we look to the future, this project holds potential applications in tracking the usage of specific words or phrases across various social media platforms. Below are the bar charts and line plot for your reference.

# Graph of Top 10 Countries that used #coronavirus
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Countries:%20%23coronavirus.png)

# Graph of Top 10 Countries that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Countries:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)

# Graph of Top 10 Langauges that used #coronavirus  
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Languages:%20%23coronavirus.png)

# Graph of Top 10 Langauges that used #코로나바이러스
![alt text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/Chart%20of%20Top%2010%20Languages:%20%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4.png)

# Line Plot of the Use of Two Hashtags throughout 2020: "#virus" and "#flu"
![alt_text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/line_plot_hastag.png)

# Line Plot of the Use of Three Hashtags throughout 2020: "#virus", "#flu", and "#corona"
![alt_text](https://github.com/oliviastevens11/twitter_coronavirus/blob/master/line_plot_hastag2.png)

