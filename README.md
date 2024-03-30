# New York Times Best Sellers Data Pipeline Project

This project aims to provide readers with insights into the latest best-selling books featured on the New York Times' best sellers lists. By leveraging data from the New York Times API and utilizing various data processing and visualization tools, this project offers a comprehensive view of the most recent week's best sellers, including details about the books, authors, publishers, and historical trends.

## Project Overview

The New York Times Best Sellers Dashboard is designed to offer readers an interactive and informative experience by showcasing the current week's best sellers and providing historical data about books that have appeared on previous best sellers lists. The dashboard enables users to explore trends, discover popular titles and authors, and gain insights into the dynamic world of literature.

## Infrastructure

The project infrastructure consists of the following components:

- **Google Cloud Platform (GCP):** [Official Website](https://cloud.google.com/)
- **Google Cloud Storage (GCS):** [Documentation](https://cloud.google.com/storage)
- **Google BigQuery:** [Documentation](https://cloud.google.com/bigquery)
- **Terraform:** [Official Website](https://www.terraform.io/)
- **Mage:** [GitHub Repository](https://www.mage.ai/)
- **dbt (data build tool):** [Official Website](https://www.getdbt.com/)
- **Docker:** [Official Website](https://www.docker.com/)
- **Looker Studio:** [Official Website](https://cloud.google.com/looker-studio?hl=en)

![Project Architecture Diagram](images/project_architecture.svg)

* Terraform is employed to provision the necessary infrastructure components for our data pipeline on Google Cloud Platform (GCP). This includes setting up Google Cloud Storage (GCS) buckets and BigQuery datasets.
* Mage serves as our data orchestration tool, enabling us to automate the extraction of data from the New York Times (NYT) API and load it into our GCS data lake and later into BigQuery. With Mage, we can schedule and manage our data pipelines efficiently, ensuring timely ingestion of updated NYT Best Sellers data.
* DBT further transforms our raw NYT Best Sellers data and builds data model to combine the overview data and books' review data. After the processing stage in dbt, the result data table is uploaded to BigQuery for later analysis and dashboard.
* Looker Studio is used to create interactive dashboards and reports. With Looker Studio, users can gain valuable insights into trends, patterns, and performance metrics related to the NYT Best Sellers data.

## Dashboard
[** The link to the dashboard **](https://lookerstudio.google.com/reporting/494d1c6b-d145-4972-aba6-0f6751ad2e4f)

IMAGE

## Replication Guide

1. Set up your Google Cloud Platform (GCP) account
    - Register an GCP account and get $300 credit on GCP.
    - Create a service account in IAM & Admin and give it access to Google Cloud Storage and Google BigQuery.
    - Download the json form key for later use.

2. Build Cloud resources needed by Terraform
    - Make sure Terraform is downloaded on your local machine. [Download Terraform](https://www.terraform.io/downloads)
    - Create a new file variables.tfvars to assign values to the variables in variables.tf. 
        - project_id (example: project_id = "YOUR_PROJECT_ID")
        - location
        - region
        - gcp_key (The path to your gcp service account key)
    - Run terraform plan & terraform apply to build the resources

3. Get New York Times API key
    - Create an account on https://developer.nytimes.com/ and get api key for later use.

4. Set up orchestration tool Mage
    - Make sure docker is downloaded on your local machine.
    - Use the Dockerfile in Mage folder to build an image.
    - Start a docker container using the built image and make sure to use mage_nytimes as the mounted volume.
    - Be sure to add your New York Times API key to Secrets which is located on the right side bar. The key name should be "api-key" and the value should be your API key.
    - Run Mage pipelines and feel free to set up triggers and schedule to run the pipelines.

5. Set up DBT
    - Create an DBT account on https://www.getdbt.com/signup and create a new project.
    - dbt folder includes necessary files to build the data models and load the result table to BigQuery

6. Build Dashboard
    - At this point, the data table in your BigQuery dataset is ready to be used for later analysis or building dashboards.
    - This project uses Looker Studio as the dashboard tool. Feel free to use other dashboards.

7. Tear down resources
    - Tear down the resources by running "terraform destroy" to prevent extra cost.


## Next Steps
- Use VM to realize the whole project.
- Add schedule to Mage and DBT to update the Best Sellers data weekly.
- Add tests to make sure the data quality in Mage and DBT.
- Add Documentation to DBT part.