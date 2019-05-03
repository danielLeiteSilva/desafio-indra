    
#!groovy

pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/daniel19942015/desafio-indra.git'
            }
        }
        stage ("Test"){
            steps{
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//s//activate
                '''
                bat '''
                
                python -m Pyautomators -f json -o .//relatorio.json
                '''
                
            }
        }
    }
}
