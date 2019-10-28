import setuptools

setuptools.setup(
    name='flowlog-pprint',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=['colorama'],
    python_requires='>=3.5.0',
    entry_points={
        'console_scripts': [
            'flowlog_pprint = flowlog_prettyprint.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
