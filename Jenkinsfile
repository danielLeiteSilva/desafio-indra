#!groovy

node {
    stage('Preparation') {
        echo 'Code preparação'
    }
    
    stage('Build') {
       withMaven(maven: 'Maven 3') {
          dir('carrefour') {
            sh 'mvn clean test -Dwebdriver.type=chrome -Dwebdriver.chrome.driver=E:/chromedriver.exe'
          }
    }
    
    stage('Results') {
        echo 'Results'
    }
}
