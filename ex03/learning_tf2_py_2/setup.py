from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'learning_tf2_py_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='belyakovaDep',
    maintainer_email='d.belyakova1@g.nsu.ru',
    description='Module 4 Task 3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['static_turtle_tf2_broadcaster = learning_tf2_py_2.static_turtle_tf2_broadcaster:main',
			    'turtle_tf2_broadcaster = learning_tf2_py_2.turtle_tf2_broadcaster:main',
			     'turtle_tf2_listener = learning_tf2_py_2.turtle_tf2_listener:main',
        ],
    },
)
