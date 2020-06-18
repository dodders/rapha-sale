#!/bin/sh

aws lambda update-function-code --function-name rapha-sale --zip-file fileb://function.zip --profile iam-admin
