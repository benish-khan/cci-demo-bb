from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, BeBe!'
    

version: 2.1 # use 2.1 to make use of orbs and pipelines
# setup: true
#### Orbs  ###
orbs:
  heroku: circleci/heroku@1.2.6 #quickly deploy applications with minimal config
  #path-filtering: circleci/path-filtering@0.0.2
  #continuation: circleci/continuation@0.1.2



### Executors ### 
executors: #can reuse this executor in other job
  python-executor:
    docker:
      - image: cimg/python:3.8



### Workflows ###
workflows:
  version: 2.1
  build-test-&-deploy:
    jobs:
      - build
      - test_crud_operations:
          #context: my-restricted-context
          requires:
            - build 


      - hold:
          type: approval
          requires:
            - build
            - test_crud_operations

      - heroku/deploy-via-git: #using the pre-configured job, deploy-via-git in heroku orb!
          requires:
            - hold
          filters:
            branches:
              only:
                - master #will only deploy if commit was pushed from master && approved in UI. Can get fancier with regex or multiple feature branches too


 ### Jobs here ###
jobs:
  
  build: 
    executor: python-executor 
    steps:
      - checkout
      - restore_cache: # download new dependencies, if any, and not redownload everything on every build
          keys:
            - pip-packages-v1-{{ .Branch }}-{{ checksum "Pipfile.lock" }}
            - pip-packages-v1-{{ .Branch }}-
            - pip-packages-v1-
      - run: 
          name: Install Python venv 
          command: | 
            pipenv install 
      - run:
          name: Check Python version
          command: | 
            pipenv run python --version

      - save_cache: # cache Python dependencies using checksum of Pipfile as the cache-key 
          key: pip-packages-v1-{{ .Branch }}-{{ checksum "Pipfile.lock" }}
          paths:
            - ./venv

#Caching persists data between the same job in different workflows runs.

  test_crud_operations: #job with steps to test my applicatio.
    executor: python-executor   #this was pre-defined and called here
    parallelism: 4
    resource_class: medium
    steps:
      - checkout
      - attach_workspace: #persist data between jobs in a single workflow
          at: ~/project
      - run: 
          name: Install Python Dependencies in a venv 
          command: | 
            pipenv install 
            pipenv install unittest-xml-reporting
      
      - run: 
          name: Create test-results file to store test-results in
          command: |
              cd /home/circleci/project
              mkdir test-results
      - run:
          name: Running tests within test_app.py file. 
          command: pipenv run python test_app.py  

      - store_test_results:
          path: test-results
      - store_artifacts: #Artifacts persist data after a workflow has finished.
          path: test-results
          destination: trl

      - run:
          name: Just a happy message that all tests passed
          command: echo "Its working successfully."



# pre-heroku-orb 

  # deploy-to-heroku: #jobs with steps to deploy my application once build and tests jobs pass on master only.
  #   executor: python-executor
  #   steps:
  #     - checkout
  #     - run:
  #         name: Setup Heroku CLIs
  #         command: |
  #           sudo curl https://cli-assets.heroku.com/install.sh | sh
  #     - run:
  #         name: Restart heroku dyno #update comment
  #         command: |
  #           heroku restart web.1 --app $HEROKU_APP_NAME

  #     - run:
  #         name: Run Log
  #         command: |
  #           heroku logs --app $HEROKU_APP_NAME