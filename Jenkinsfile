#!groovy

node('master') {
    stage('Preparation') {
        echo 'Code preparação'
    }
    
    stage('Build') {
       withMaven(maven: 'Maven 3') {
          dir('bobcat') {
            sh 'mvn clean test -Dwebdriver.type=chrome -Dwebdriver.chrome.driver=E:/Workspace/chromedriver.exe'
          }
    }
    
    stage('Results') {
        echo 'Results'
    }
}
