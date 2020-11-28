


from ._dump import DumpMethod

from .MWTimestamp import MWTimestamp



class MWUploadFileResult(DumpMethod):

	def __init__(self, title:str, bIsNew:bool, timestamp:MWTimestamp, width:int, height:int):
		self.title = title
		self.timestamp = timestamp
		self.bIsNew = bIsNew
		self.width = width
		self.height = height
	#

	def __bool__(self):
		return True
	#

	def __str__(self):
		return "MWUploadFileResult(" \
			+ "title=" + repr(self.title) \
			+ ", bIsNew=" + repr(self.bIsNew) \
			+ ", timestamp=" + repr(self.timestamp) \
			+ ", width=" + repr(self.width) \
			+ ", height=" + repr(self.height) \
			+ ")"
	#

#








