{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first     I know someone will respond this question as duplicate. Actually i already search and follow but still got error. In my emulator it working but when i run in real device i got that error. I already add dependencies which is<br>   compile 'com.android.support:appcompat-v:..'   compile 'com.android.support:design:..'`But still got error. I really don't know how to solve it. I also got this error. Caused by: android.view.InflateException: Binary XML file line #: Error inflating class android.support.design.widget.CoordinatorLayoutCaused by: java.lang.reflect.InvocationTargetExceptionCaused by: java.lang.IllegalArgumentException: You need to use a Theme.AppCompat theme (or descendant) with the design library.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Slow version of gensim.models.doc2vec is being used\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "before lda\n",
      "[(0, '0.013*\"line\" + 0.006*\"name\" + 0.006*\"file\"'), (1, '0.005*\"want\" + 0.005*\"like\" + 0.005*\"get\"'), (2, '0.010*\"file\" + 0.007*\"line\" + 0.007*\"app\"')]\n",
      "Original_TAGS  android binary invocationtargetexception \n",
      "[[(2, 0.98732618877112688)]]\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "import numpy as np\n",
    "# Read in the data.\n",
    "#games = pandas.read_csv(\"/home/swathi/Desktop/title.csv\")\n",
    "#games1 = pandas.read_csv(\"/home/swathi/Desktop/body.csv\")\n",
    "games = pandas.read_csv(\"/home/swathi/Desktop/new.csv\")\n",
    "body = games.Body\n",
    "title = games.Title\n",
    "A = np.squeeze(np.asarray(games))\n",
    "tmpC = list(map((lambda x: x[1]), A))\n",
    "temp=list(map((lambda x: x[0]), A))\n",
    "print(\"first\",tmpC[0])\n",
    "\n",
    "doc_complete=tmpC\n",
    "#print(\"doc_complete\",doc_complete)\n",
    "test4 =tmpC[0]\n",
    "test = [test4]\n",
    "\n",
    "#print(doc_complete)\n",
    "from nltk.corpus import stopwords \n",
    "from nltk.stem.wordnet import WordNetLemmatizer\n",
    "import string\n",
    "stop = set(stopwords.words('english'))\n",
    "exclude = set(string.punctuation) \n",
    "lemma = WordNetLemmatizer()\n",
    "def clean(doc):\n",
    "    stop_free = \" \".join([i for i in doc.lower().split() if i not in stop])\n",
    "    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)\n",
    "    normalized = \" \".join(lemma.lemmatize(word) for word in punc_free.split())\n",
    "    return normalized\n",
    "\n",
    "doc_clean = [clean(doc).split() for doc in doc_complete]  \n",
    "doc_clean1 = [clean(doc).split() for doc in test]  \n",
    "\n",
    "# print(\"doc_clean\",doc_clean)\n",
    "\n",
    "\n",
    "\n",
    "import gensim\n",
    "from gensim import corpora\n",
    "from gensim.corpora import Dictionary\n",
    "from gensim.models import ldamodel\n",
    "# Creating the term dictionary of our courpus, where every unique term is assigned an index.\n",
    "dictionary = corpora.Dictionary(doc_clean)\n",
    "dictionary1 = corpora.Dictionary(doc_clean1)\n",
    "#print(\"dictionary1 \",dictionary1)\n",
    "#print(dictionary.token2id)\n",
    "\n",
    "\n",
    "# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.\n",
    "doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]\n",
    "doc_term_matrix1 = [dictionary1.doc2bow(doc) for doc in doc_clean1]\n",
    "#print(\"doc_term_matrix1\",doc_term_matrix1)\n",
    "#print(doc_term_matrix)\n",
    "# Creating the object for LDA model using gensim library\n",
    "print(\"\\n\\nbefore lda\")\n",
    "Lda = gensim.models.ldamodel.LdaModel\n",
    "\n",
    "# Running and Trainign LDA model on the document term matrix.\n",
    "ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=100)\n",
    "#lda = Lda(num_topics=2,id2word = dictionary)\n",
    "\n",
    "print(ldamodel.print_topics(num_topics=3, num_words=3))\n",
    "print(\"Original_TAGS\",temp[0])\n",
    "topics=ldamodel.get_document_topics(bow=doc_term_matrix1, minimum_probability=None, minimum_phi_value=None, per_word_topics=False)\n",
    "\n",
    "print(list((topics)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
