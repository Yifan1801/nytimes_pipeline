variable "project_id" {
  description = "The GCP Project ID"
  type        = string
}

variable "location" {
  description = "Your location"
  type        = string
}

variable "gcs_bucket_name" {
  description = "The name of your Google Cloud Storage bucket"
  type        = string
  default     = "nytimes_project"
}

variable "bq_dataset_name" {
  description = "The name of your BigQuery dataset"
  type        = string
}

variable "region" {
  description = "The region used when creating google provider. (eg. us-central1)"
  type        = string
}

variable "gcp_key" {
  description = "The path to your gcp service account key"
  type = string
}