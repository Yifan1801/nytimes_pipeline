terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  credentials = var.gcp_key
  project     = var.project_id
  region      = var.region
}

resource "google_storage_bucket" "project-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true
}

resource "google_bigquery_dataset" "project-dataset" {
  dataset_id    = var.bq_dataset_name
  friendly_name = "nytimes_best_seller_project"
  description   = "The dataware house for nytimes best seller project"
  location      = var.location
}