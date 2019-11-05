import setuptools

setuptools.setup(
    name='flowlog-pprint',
    version='0.0.4',
    packages=setuptools.find_packages(),
    install_requires=['colorama'],
    python_requires='>=3.5.0',
    entry_points={
        'console_scripts': [
            'flowlog-pprint = flowlog_pprint.__main__:main'
        ]
    },
    url="https://github.com/d-karlss/flowlog-pprint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description='Pretty print AWS VPC Flow Logs'
)
