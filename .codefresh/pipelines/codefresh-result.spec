version: '1.0'
kind: pipeline
metadata:
  name: dustinvanbuskirk/example-voting-app/result
  isPublic: false
  labels:
    tags: []
spec:
  triggers:
    - type: git
      repo: dustinvanbuskirk/example-voting-app
      events:
        - push
      branchRegex: /.*/gi
      modifiedFilesGlob: result/**
      provider: github
      context: github
  contexts: []
  steps:
    BuildingDockerImage:
      title: Building Docker Image
      type: build
      image_name: example-voting-app/result
      working_directory: ./result/
      tag: '${{CF_BRANCH_TAG_NORMALIZED}}'
      dockerfile: Dockerfile
  stages: []
