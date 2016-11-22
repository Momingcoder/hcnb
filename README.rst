hcnb
===========

.. image:: https://travis-ci.org/Momingcoder/hcnb.svg?branch=master
    :target: https://travis-ci.org/Momingcoder/hcnb

A plugin for Hachi_ to detect spam.

.. _Hachi: https://github.com/guokr/Hachi

Usage
--------

::

    > nb = NaiveBayes()
    > nb.predict(message)

Configuration
--------------

::

    > ('hcnb', "NaiveBayes()", 'bayes')

Dependence
-----------

* scikit-learn
* jieba

Attention
-----------
You need to provide your own ``ham, spam, stopwords, userdict, words`` data in ``./data/`` .

* ``ham`` Normal sentence (bayes)
* ``spam`` Spam (bayes)
* ``stopwords`` (tf-idf)
* ``userdict`` (jiaba)
* ``words`` Every words presented in the above file.

By the way, ``stopwords`` affects little, which means you can just offer an empty file.
