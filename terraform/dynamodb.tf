module "dynamodb_table" {
  source = "terraform-aws-modules/dynamodb-table/aws"

  name      = "csv"
  hash_key  = "_id"
  range_key = "serial_number"

  attributes = [
    {
      name = "_id"
      type = "S"
    },
    {
      name = "serial_number"
      type = "S"
    }

  ]
}
