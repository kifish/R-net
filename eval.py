from model import *
config = CONFIG()
with tf.Session() as sess:
    model = RNET(mode='eval')
    model.eval(sess=sess)
