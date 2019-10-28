import setuptools

setuptools.setup(
    name='flowlog_pprint',
    version='0.0.2',
    packages=setuptools.find_packages(),
    install_requires=['colorama'],
    python_requires='>=3.5.0',
    entry_points={
        'console_scripts': [
            'flowlog_pprint = flowlog_pprint.__main__:main'
        ]
    },
    url="https://github.com/d-karlss/flowlog-pprint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
