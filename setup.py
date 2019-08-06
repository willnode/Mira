from setuptools import setup

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['foo'],  #same as name
   install_requires=["gensim",
"tensorflow",
"line-bot-sdk",
"scikit-learn",
"numpy",
"flask",
"mysql",
"mysql-connector-python-rf"], #external packages as dependencies
)