import paramiko
import argparse
from config import username, password


def run_command(server, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    ssh.close()
    return output


parser = argparse.ArgumentParser()
parser.add_argument("servers", nargs='+', help="list of servers to run the command on")
parser.add_argument("command", help="command to run on the servers")
args = parser.parse_args()
servers = args.servers
command = args.command

results = []
for server in servers:
    result = run_command(server, command)
    results.append(result)

for output in results:
    print(output)
