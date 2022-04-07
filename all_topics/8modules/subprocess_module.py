import subprocess

# run -- to run command on terminal

subprocess.run("dir", shell=True) # as dir is built in method of shell, we need to use shell=True
# as we used shell = True, we can specify the entire command as first argument for run command
# with shell argument
# subprocess.run('ls -ltr', shell=True)
# without shell argument
# subprocess.run(['ls', '-ltr'])

# to get arguments
p1 = subprocess.run("dir", shell=True)
print(p1.args)
# to get return code
print(p1.returncode)
# to get standard out
print(p1.stdout)

# captured_output argument is store the output into variable
out = subprocess.run("dir", shell=True, capture_output=True, text=True)
print(out.stdout)

# setting standard_out directly
p1 = subprocess.run("dir",shell=True, stdout=subprocess.PIPE, text=True)
print(p1.stdout)

# redirecting stdout to file
with open("output.txt", "w") as f:
    p1 = subprocess.run("dir", shell=True, stdout=f, text=True)

# when the command is wrong or it is throwing error python will not throw error

p2 = subprocess.run("eded", shell=True, capture_output=True)
print(p2.stderr)
print(p2.returncode)

# to python throw error we will use argument check=True if commands wrong it will throw error

p3 = subprocess.run("ererre", shell=True, stderr=subprocess.DEVNULL)
print(p3.stderr)


# import subprocess
# import sys
#
# subprocess.run([sys.executable, "-c", "print('good ni8')"])