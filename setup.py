import subprocess
import re
from setuptools import find_packages, setup
import semver


# run a shell command and return stdout
def run_cmd(cmd):
    cmd_proc = subprocess.run(cmd, shell=True, capture_output=True)
    if cmd_proc.returncode != 0:
        raise OSError(f"Shell command '{cmd}' failed with return code {cmd_proc.returncode}\n"
                      f"STDERR: {cmd_proc.stderr.decode('utf-8')}")
    return cmd_proc.stdout.decode('utf-8').strip()


#
# fetch the most recent version tag to use as build version
#
latest_tag = run_cmd('git describe --abbrev=0 --tags')
build_version = re.sub('v\.?\s*', '', latest_tag)
# validate that this is a valid semantic version - will throw exception if not
semver.VersionInfo.parse(build_version)

# use the contents of the README file as the 'long description' for the package
with open('./README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name='industry-solutions-release',
    version=build_version,
    author='Antoine Amend',
    author_email='antoine.amend@databricks.com',
    description='Deploy solution accelerators as HTML files',
    long_description=long_description,
    include_package_data=True,
    install_requires=[
        'databricks-api==0.9.0',
    ],
    long_description_content_type='text/markdown',
    url='https://github.com/databricks-industry-solutions/industry-solutions-release',
    packages=find_packages(where='.'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Other/Proprietary License',
    ],
)