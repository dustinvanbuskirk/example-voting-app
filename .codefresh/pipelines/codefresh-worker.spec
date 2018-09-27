version: '1.0'
kind: pipeline
metadata:
  name: dustinvanbuskirk/example-voting-app/worker
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
      modifiedFilesGlob: worker/**
      provider: github
      context: github
  contexts: []
  steps:
    BuildingDockerImage:
      title: Building Docker Image
      type: build
      image_name: example-voting-app/worker
      working_directory: ./worker/
      tag: '${{CF_BRANCH_TAG_NORMALIZED}}'
      dockerfile: Dockerfile
  stages: []
