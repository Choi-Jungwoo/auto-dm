from setuptools import setup, find_packages

setup(
    name='auto-dm',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Choi-Jungwoo/auto-dm',
    license='MIT',
    author='JungWoo',
    author_email='jungwoo@cineuse.com',
    description='大麦自动抢票程序',
    install_requires=[
        'pyqt5',
        'qt_material',
        'requests',
        'selenium',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'auto-dm = auto_dm.__main__:main'
        ]
    }
)
