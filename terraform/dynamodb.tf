module "dynamodb_table" {
  source = "terraform-aws-modules/dynamodb-table/aws"

  name     = "csv"
  hash_key = "_id"

  attributes = [
    {
      name = "_id"
      type = "S"
    }
  ]
}
