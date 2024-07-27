Topic Modeling and Content Insights on Netflix Reviews End-To-End SageMaker Pipeline
===========================================



Project Overview
-------

This project aims to build an end-to-end machine learning pipeline using AWS SageMaker to perform topic modeling and extract content insights from Netflix reviews data. The primary objectives are to identify key topics in the reviews, analyze viewer interests and feedback, and visualize trends using AWS QuickSight. Additionally, the project will simulate real-time data integration to demonstrate the pipeline's capability to handle live updates.

Objectives
-------

1.  **Topic Modeling**: Apply BERTopic to categorize Netflix reviews into key topics.
    
2.  **Content Insights**: Analyze the distribution of topics to gain insights into viewer interests, preferences, and feedback on specific content.
    
3.  **Visualization**: Use AWS QuickSight to create interactive dashboards displaying topic trends and insights for content strategy teams.
    
4.  **Real-Time Simulation**: Simulate real-time reviews into the pipeline to demonstrate the system's ability to handle live data updates.


Dataset
-------

*   **Source**: Kaggle Netflix Reviews Dataset
    
*   **Time Period**: 2018 to present
    
*   **Attributes**:
    
    *   reviewId: Unique identifier for each review
        
    *   userName: Name of the reviewer
        
    *   content: Text content of the review
        
    *   score: Rating given by the reviewer
        
    *   thumbsUpCount: Number of likes on the review
        
    *   reviewCreatedVersion: Version of the app used to create the review
        
    *   at: Date and time of the review
        
    *   appVersion: Version of the app
     
Tools and Technologies
-------

*   **Data Preprocessing**: Pandas, NLTK
    
*   **Topic Modeling**: BERTopic
    
*   **Visualization**: AWS QuickSight, Plotly (for initial EDA)
    
*   **AWS Services**: SageMaker, S3, Lambda, Kinesis, CloudWatch

    
Project Phases
-------

1.  **Phase 1: Batch Processing and Initial Insights**
    
    *   **Data Loading and Preprocessing**: Clean and preprocess the review data for analysis.
        
    *   **Exploratory Data Analysis (EDA)**: Perform initial analysis to understand the data distribution and basic statistics.
        
    *   **Topic Modeling**: Train a BERTopic model to identify key topics in the review data.
        
    *   **Content Insights**: Analyze the distribution of topics and perform sentiment analysis to gauge viewer sentiment.
        
    *   **Visualization**: Create dashboards in AWS QuickSight to visualize topic trends and insights.
        
2.  **Phase 2: Real-Time Data Simulation**
    
    *   **Streaming Data Pipeline**: Set up AWS services (e.g., Kinesis, Lambda) to simulate real-time review data ingestion.
        
    *   **Real-Time Processing**: Implement Lambda functions to process streaming data and update the SageMaker model predictions.
        
    *   **Dashboard Integration**: Ensure the QuickSight dashboards update in real-time to reflect new data.


Project Workflow
-------

1.  **Data Ingestion**: Load and preprocess the Netflix reviews dataset.
    
2.  **Model Training**: Train the BERTopic model on the cleaned review data.
    
3.  **Insights Generation**: Analyze topics and sentiment, and generate insights.
    
4.  **Visualization**: Create interactive dashboards in QuickSight to display insights.
    
5.  **Real-Time Simulation**: Implement a pipeline to simulate real-time review ingestion and processing.
    
6.  **Continuous Monitoring**: Set up monitoring to track data and model performance, ensuring the system adapts to new data.


AWS QuickSight Dashboard Components
-------

1.  **Topic Distribution Over Time**: Line chart showing the frequency of different topics over time.
    
2.  **Sentiment Analysis**: Bar charts displaying sentiment distribution within each topic.
    
3.  **Word Cloud**: Visual representation of the most common words within specific topics.
    
4.  **Interactive Filters**: Controls to filter data by date range, content type, and specific topics.
    

Expected Outcomes
-------

*   A comprehensive machine learning pipeline for topic modeling and content insights using AWS SageMaker.
    
*   Interactive dashboards in AWS QuickSight that provide valuable insights into viewer interests and content performance.
    
*   Demonstration of the pipeline’s capability to handle real-time data updates, showcasing robust and scalable ML solutions.
    

Future Enhancements
-------

*   Extend the pipeline to include more advanced NLP techniques for deeper sentiment analysis.
    
*   Implement more granular real-time data processing and integration features.
    
*   Explore additional visualizations and insights to support content strategy and decision-making.
    

How to Use
-------

1.  **Setup**: Ensure you have access to AWS SageMaker, QuickSight, and other necessary AWS services. Load the dataset into an S3 bucket.
    
2.  **Preprocess Data**: Clean and preprocess the dataset using the provided preprocessing steps.
    
3.  **Train Model**: Train the BERTopic model and save the trained model to S3.
    
4.  **Generate Insights**: Run the analysis to generate topic distribution and sentiment insights.
    
5.  **Visualize Data**: Create and configure QuickSight dashboards to visualize the insights.
    
6.  **Simulate Real-Time Data**: Set up the real-time data pipeline and ensure the dashboards update with new data.
    

This README serves as a guide to understand the scope, objectives, and workflow of the project. For detailed implementation steps and code, refer to the project documentation and individual script files.

Contact
-------

For any questions or support, please contact curio25.ai@gmail.com
