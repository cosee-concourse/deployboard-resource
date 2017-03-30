# Deployboard Resource
 
[![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/deployboard-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/deployboard-resource)

Finds html surefire reports and uploads the to S3.

## Source Configuration

* `AWS_ACCESS_KEY`: *Required* Access Key for the AWS Account the S3 Bucket belongs to
* `AWS_SECRET_KEY`: *Required* Secret Key for the AWS Account the S3 Bucket belongs to

## Behavior

### `out`: Post messages to Slack

* Uploads html reports to an S3 bucket.
  
#### Parameters
 
* `version`: *Required* Filepath to `semver` version file
* `directory`: *Required* The directory that will be searched for surefire reports
* `bucket`: *Required* The name of the bucket to upload the reports to
  
### `check`: no-op

* Since this resource does not have a version itself `check` returns an empty JSON.

### `in`: no-op

* Simply returns the provided version

## Example Configuration

### Resource Type
``` yaml
- name: deployboard-resource
  type: docker-image
  source:
    repository: quay.io/cosee-concourse/deployboard-resource
```
### Resource

``` yaml
- name: deployboard
  type: deployboard-resource
  source: 
    AWS_ACCESS_KEY: AKAIMFHEFIWNL43579HFKFEHIEUFH384759
    AWS_SECRET_KEY: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Plan

``` yaml
  - put: slack
    params: 
      version: version/number
      directory: junit
      bucket: test-bucket
```
