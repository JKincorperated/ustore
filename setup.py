from setuptools import setup

setup(
    name='ustore',
    version='1.0',    
    description='A libary that makes user managment easier.',
    url='https://github.com/JKincorperated/ustore/',
    author='JKinc',
    license='GNU General Public License v3.0',
    author_email='offical.jkinc@gmail.com',
    install_requires=['hashlib',
                      'json',         
                      'pyaes',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.9',
    ],
)
