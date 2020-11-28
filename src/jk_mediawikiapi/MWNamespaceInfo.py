


from ._dump import DumpMethod




class MWNamespaceInfo(DumpMethod):

	def __init__(self, namespaceID:int, nameCanonical:str, namePublic:str, bContent:bool, bNonIncludable:bool, bAllowsSubpages:bool, nameAlias:str):
		self.namespaceID = namespaceID
		self.bContent = bContent
		self.nameCanonical = nameCanonical
		self.namePublic = namePublic
		self.bNonIncludable = bNonIncludable
		self.bAllowsSubpages = bAllowsSubpages
		self.nameAlias = nameAlias
		self.names = [ self.namePublic ]
		if nameCanonical:
			if self.nameCanonical not in self.names:
				self.names.append(self.nameCanonical)
		if nameAlias:
			if self.nameAlias not in self.names:
				self.names.append(self.nameAlias)
	#

	def __str__(self):
		return "NameSpace<" + str(self.namespaceID) + ":" + repr(self.nameCanonical) + ">"
	#

	def __repr__(self):
		return "NameSpace<" + str(self.namespaceID) + ":" + repr(self.nameCanonical) + ">"
	#

#








