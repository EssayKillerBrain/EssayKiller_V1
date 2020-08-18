# -*- coding: gbk -*-

# Original work Copyright 2018 The Google AI Language Team Authors.
# Modified work Copyright 2019 Rowan Zellers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# 本项目仅限于学术与交流用途，包括开源部分，禁止用于任何商业用途
# 使用搭载好的EssayKilelrBrain各个模块构造pipeline，端到端输出文本
# 部分核心代码已加密，若要获取完整版本请附上个人/研究机构链接证明

from absl import app
from absl import flags
import collections
import tensorflow as tf
import sys
import requests
from utils import *
from AutoDetect.text_detection_video import *
from AutoFormatter.formatter import *
from AutoRecog.ocr import *
from AutoScorer.DNN_Scorer import *
from AutoWritter.scripts import *
from Essaykiller import AutoBrainBase

tf.logging.set_verbosity(tf.logging.ERROR)
tf.get_logger().setLevel('INFO')
tf.autograph.set_verbosity(1)

FLAGS = flags.FLAGS
flags.DEFINE_string('gpu', None, 'comma separated list of GPU(s) to use.')

result = []

class EssayKillerPipeline(AutoBrainBase):
	"""
	@params
	input_feed: text input_feed
	sequence_len: sequence length
	...
	
	为防止自动化EK框架被人恶意抢注、利用或复刻，pipeline核心代码与构造类暂不开源
	若有学术需要，请带上个人或机构的学术需求陈述，发送邮件到deanyuton@gmail.com
	根据陈述信息，我将会发送完整版的代码与测试数据到给定的邮箱。谢谢理解
	"""
	def __init__():
		self.config = FLAGS.config
		pass 

	def enable_visiondetect():
		'''
		开启视频检测，从硬件输入端获取视频流文件
		硬件配置：Logitech C930C
		@params:video视频流输入端口
		...
		'''
		pass

	def generage_char_from_videostream():
		pass 

	def extract_topic_sentence():
		pass 

	def essay_writter_core():
		pass

	def scoring_to_best_essay():
		pass 

	def formatting_essay_to_exam():
		pass


		
def main(argv):
    del argv
    if FLAGS.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu
    else:
        print('Please assign GPUs.')
        exit()

print("test sample in trained model...")
if __name__ == "__main__":
	try:
		pass
	except:
		print("pipeline has failed...")
	#dicts = result[0].split(":")
	#plexity = result.get['ppl']
	print("the final ppl score is: \n",scores )
	print("the final text output as :", text)
	print(sum(result))
