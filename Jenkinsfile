properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/Leonavshalom/dev3006.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
