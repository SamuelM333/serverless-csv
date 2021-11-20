module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "samuelm333-csv"
  acl    = "private"
}

