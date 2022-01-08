# HW4: Analyze A-B Test Results

## Prerequisites

* **Workspace**: (Anaconda) Jupyter Notebook
* Additional installations: None

## Project Overview: Analyze A/B Test Results 

A/B tests are very commonly performed by data analysts and data scientists. It is important that you get some practice working with the difficulties of these. For this project, you will be working to understand the results of an A/B test run by an e-commerce website. The company has developed a new web page in order to try and increase the number of users who "convert," meaning the number of users who decide to pay for the company's product. Your goal is to work through this notebook to help the company understand if they should implement this new page, keep the old page, or perhaps run the experiment longer to make their decision. You will be provided a dataset reflecting data collected from an experiment. Use statistical techniques to answer questions about the data and report your conclusions and recommendations in a report.

## Project Details 

  The Project was divided into Three Parts i.e. : 

  ### Part I - Probability

  > Statistics were computed to find out the probabilities of converting regardless of page. These were used to analyze if one page or the other led to more conversions.

  ### Part II - A/B Test

  > Next, hypothesis testing was conducted assuming the old page is better unless the new page proves to be definitely better at a Type I error rate of 5%. The data was bootstrapped and sampling distributions were determined for both pages. Conclusions were drawn on conversions for both pages by calculating p-values.

  ### Part III - Regression

  > Logistic regression was then performed to confirm results of the previous steps. Null and alternative hypotheses associated with this regression model were stated and verified using statsmodel.

## Data Sources

* Source: ab_data.csv
* Source: countries.csv
* HW4_Analyze_AB_Test_Results_Notebook_template.ipynb

## How to do the Homework

* Download the 3 files from DSP2105 repo or download from Canvas in zip format normally
* Make a copy of the Jupyter Notebook file and rename it to
  * HW4_Analyze_AB_Test_Results_Notebook_Your_Name.ipynb
* Launch Anaconda Jupyter and open the very ipynb file and follow along the instruction inside.
* Finish answering all the questions.
* Knit the ipynb file to an HTML file, Open it to see if it looks like whatsoever you see on the ipynb file.
* Submit the HTML file in Canvas. 

## Authors

* HaccTech
* Udacity

## License

* Free
