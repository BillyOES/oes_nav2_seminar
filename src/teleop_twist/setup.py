from setuptools import setup

package_name = 'teleop_twist'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oes',
    maintainer_email='oes@todo.todo',
    description='For ultimate sam_bot_description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'teleop_twist = teleop_twist.teleop_twist:main',
        ],
    },
)
