
// 测试提交


//例1：流水线外部定义变量承接返回值
def test = input id: 'Test_input', message: 'Hello , What\'s your name', ok: 'Input finished.', parameters: [string(defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?', name: 'PERSON')], submitter: 'alice,bob', submitterParameter: 'name'
pipeline {
    environment{
        P1 = "test"
        P2 = "${P1}_1"  //在定义环境变量时可以包含已经定义的变量
    }
    agent any
    stages {
        stage('Hello') {
            // steps {
            //     echo 'Hello World1'
            //     echo 'Hello World2'
            // } steps 和 parallel不能同在一个stage出现
            parallel {
                stage('hello.1'){
                    when { // 条件判断
                       environment name:'P1',value:"test" 
                    }                    
                    steps {
                        echo "hello.1${P1}${test['PERSON']}_${BUILD_ID}${BUILD_URL}"
                        sleep 5
                    }
                }
                stage('hello.2'){
                    when {
                       environment name:'P1',value:"test" 
                    }
                    steps {
                        echo "hello.2${P2}" // 有变量要用双引号
                    }
                }
            }
        }
        stage('world') {
            steps {
                echo 'Hello World11'
                echo 'Hello World22'
            }
        }
        stage('print pwd') {
            steps {
                sh 'pwd'
                echo '${p2}'
            }
        }
        stage('clone git') {
            steps {
                echo '开始下载代码'
                sh 'pwd'
                 git credentialsId: 'f6c06727-0552-41e9-bb44-d97c3c07b182', url: 'https://github.com/xiaokaiCoding/2.29-.git'
            }
        }
    }
    post{                                //post部分可以包含多种条件块，可以根据需求只设定自己需要的条件块
        success{                         //当前完成状态为成功时执行
            echo 'success'
       }
        failure{                         //当前完成状态为失败时执行
            echo 'failure'
       }
        unstable{                        //当前完成状态为不稳定时执行
            echo 'unstable'
       }
        cleanup{                         //清理条件块，不论当前完成状态是什么，在其他所有条件块执行完成后都执行
            echo 'cleanup'
       }
    }
}
