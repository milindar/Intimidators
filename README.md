# Intimidators
Course: 44-517-02

Project number: 7

List of developers:
- Pradeepkumar Theegala - [s534742@nwmissouri.edu](s534742@nwmissouri.edu)
- Millindar Reddy Maligireddy - [s534638@nwmissouri.edu](s534638@nwmissouri.edu)
- Sunil Mundru - [s534939@nwmissouri.edu](s534939@nwmissouri.edu)

# Links
- Repo: [https://github.com/pradeepkumartheegala/Intimidators](https://github.com/pradeepkumartheegala/Intimidators)
- Issue tracker: [https://github.com/pradeepkumartheegala/Intimidators/issues](https://github.com/pradeepkumartheegala/Intimidators/issues)
# Introduction:
We are going to use superstore data to find the maximum, minimum and average among the sales based on the category or segment.
# Data Source:
- Link to Data source: [https://www.kaggle.com/aksha17/superstore-sales](https://www.kaggle.com/aksha17/superstore-sales)

# V's of big data
This dataset is based on sales of superstore and its size is 2 MB which includes 21 columns and 9994 records. The data in the dataset is Structured data and it is available in excel format. The velocity of the dataset is zero because data is updated every four years. The data is not messy and it is cleaned.
# Big Data Problems:

Pradeepkumar

Problem: For each category, find the maximum number of sales.

Mapper Input: 
| 1 | CA-2016-152156 | 8/11/2016 | 11/11/2016 | Second Class | CG-12520 | Claire Gute | Consumer | United States | Henderson | Kentucky | 42420 | South | FUR-BO-10001798 | Furniture | Bookcases | Bush Somerset Collection Bookcase | 261.96 | 2 | 0 | 41.9136 |
|---|----------------|-----------|------------|--------------|----------|-------------|----------|---------------|-----------|----------|-------|-------|-----------------|-----------|-----------|-----------------------------------|--------|---|---|---------|


Mapper Output:

| Category  | Maximum no of sales |
|-----------|---------------------|
| Furniture | 261.96              |

Reducer Ouput:

| Category  | Maximum no of sales |
|-----------|---------------------|
| Furniture | 261.96              |

Chart:Bar chart

Sunil

Problem: For each category, find the minimum number of sales.

Mapper Input:
| 3 | CA-2016-138688 | 12/6/2016 | 16-06-16 | Second Class | DV-13045 | Darrin Van Huff | Corporate | United States | Los Angeles | California | 90036 | West | OFF-LA-10000240 | Office Supplies | Labels | Self-Adhesive Address Labels for Typewriters by Universal | 14.62 | 2 | 0 | 6.8714 |
|---|----------------|-----------|----------|--------------|----------|-----------------|-----------|---------------|-------------|------------|-------|------|-----------------|-----------------|--------|-----------------------------------------------------------|-------|---|---|--------|


Mapper Output:
| Category        | Minimum no of sales |
|-----------------|---------------------|
| Office Supplies | 14.62               |

Reducer Ouput:
| Category        | Minimum no of sales |
|-----------------|---------------------|
| Office Supplies | 14.62               |

Chart: Bar chart 

Millindar Reddy

Problem: For each segment, find number of sales

Mapper Input:
| 2 | CA-2016-152156 | 8/11/2016 | 11/11/2016 | Second Class | CG-12520 | Claire Gute | Consumer | United States | Henderson | Kentucky | 42420 | South | FUR-CH-10000454 | Furniture | Chairs | Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back | 731.94 | 3 | 0 | 219.582 |
|---|----------------|-----------|------------|--------------|----------|-------------|----------|---------------|-----------|----------|-------|-------|-----------------|-----------|--------|-------------------------------------------------------------|--------|---|---|---------|


Mapper Output:

| Segment  | Count |
|----------|-------|
| Consumer | 1     |

Reducer Ouput:

| Segment  | Count |
|----------|-------|
| Consumer | 1     |

Chart: Bar chart

 ![count](  "https://github.com/pradeepkumartheegala/Intimidators/blob/master/images/count.png")




