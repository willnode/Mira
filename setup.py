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

with reqs as f:
    for line in f:
	    print line
        # call pip's main function with each requirement
        pip.main(['install','-U', line])