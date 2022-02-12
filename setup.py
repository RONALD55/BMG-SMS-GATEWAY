from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='bmg_sms_gateway',
    version='0.0.8',
    description='An package to assist with bmg sms gateway integrations in python',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/RONALD55/BMG-SMS-GATEWAY',
    author='Ronald Nyasha Kanyepi',
    author_email='kanyepironald@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['zimbabwe', 'sms in Zimbabwe','bulk messages zimbabwe','sms gateway for Zim numbers'],
    packages=find_packages(),
    install_requires=['requests'],


)
