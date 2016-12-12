HOST='10.120.137.207'
USER='hzy'
PASSWORD='saber'
services={'parkService':'/home/hzy/hzy/3rd-party-service/jars/parkService.jar'}

START = 'nohup java -jar ${serviceJarPath} >>/dev/null 2>&1 & \n sleep 1 \n ps -ef|grep \'${serviceJarPath}\'|grep -v grep'
STOP = 'ps -ef |grep ${serviceName} |grep -v grep|awk \'{print $2}\'|xargs kill -9|ps -ef |grep ${serviceName} |grep -v grep'
STATUS = 'ps -ef|grep \'${jarLocation}\'|grep -v grep'
TOP='top -b -n 1'
TOP_PID='ps -ef |grep ${serviceName}|grep -v grep |awk \'{print $2}\'|xargs top -b -n 1 -p'

def generate_shell_command(command,service_info=None):
    if command=='start':
        return START.replace('${serviceJarPath}', services.get(service_info))
    elif command=='stop':
        return STOP.replace('${serviceName}', service_info)
    elif command=='status':
        return STATUS.replace('java', service_info)
    elif command=='top':
        if service_info == None:
            return TOP
        else:
            return TOP_PID.replace('${serviceName}',service_info)
