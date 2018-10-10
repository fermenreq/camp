from setuptools import setup, find_packages

# Replace the place holders with values for your project

setup(

    name='camp-exe-docker-comp',

    version='0.1',
    author='SINTEF Digital',
    author_email='anatoly.vasilevskiy@sintef.no',
    description='CAMP execution module',

    # This must correspond to the actual packages in the plugin.
    packages=find_packages(exclude=['tests']),

    license='MIT LICENSE',
    zip_safe=False,
    install_requires=['pyyaml'],
    entry_points={  # Optional
        'console_scripts': [
            'campexe=core.exe_comp:exe_comp_cli',
        ],
    }
)