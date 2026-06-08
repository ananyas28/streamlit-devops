pipeline {
    agent any

    stages {

       stage('Checkout') {
    steps {
        git branch: 'main',
            url: 'https://github.com/ananyas28/streamlit-devops.git'
    }
}
        }

        stage('Build') {
            steps {
                sh 'docker build -t streamlit-devops .'
            }
        }
    }
}