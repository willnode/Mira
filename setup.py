import pip

reqs = """wheel==0.30.0
setuptools==39.0.1
pip==9.0.1
gensim
tensorflow
line-bot-sdk
scikit-learn
numpy
flask
mysql
mysql-connector-python-rf""".splitlines(False)

for line in reqs:
    print line
    # call pip's main function with each requirement
    pip.__main__._main(['install','-U', line])