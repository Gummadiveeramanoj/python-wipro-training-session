import subprocess
result=subprocess.run(
    "echo Hello World",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)