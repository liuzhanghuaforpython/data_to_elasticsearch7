import tensorflow as tf
import numpy as np

# pad_sequence = tf.contrib.keras.preprocessing.sequence.pad_sequences
#
# a=[[1,2],[4,5,6,7]]
# b_len=np.array([len(_) for _ in a])
# bs_packed = pad_sequence(a,maxlen=3,padding='pre',truncating='post',value =6)
sess = tf.InteractiveSession()
embedding_dim=64
vocab_size=5000

embedding = tf.get_variable('embedding', [vocab_size, embedding_dim])

input_embedding = tf.nn.embedding_lookup(embedding, [[2,3,4,5,9],[5,6,5,7,1]])

sess.run(tf.global_variables_initializer())
print(sess.run(embedding))
print(input_embedding.shape)
print(sess.run(input_embedding))