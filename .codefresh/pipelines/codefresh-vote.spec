version: '1.0'
kind: pipeline
metadata:
  name: dustinvanbuskirk/example-voting-app/vote
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
      modifiedFilesGlob: vote/**
      provider: github
      context: github
  contexts: []
  steps:
    BuildingDockerImage:
      title: Building Docker Image
      type: build
      image_name: example-voting-app/vote
      working_directory: ./vote/
      tag: '${{CF_BRANCH_TAG_NORMALIZED}}'
      dockerfile: Dockerfile
  stages: []
