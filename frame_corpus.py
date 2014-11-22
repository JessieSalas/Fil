#sorted list of expansions are the values of a frame keys


indicators = {"give": "gift", "want": "want", "hit": "attack", "computer": "computer" , "building": "building", "situation": "problem", "business": "business"}

frame_properties = {"gift": ["tip", "presents", "money", "food", "bonus", "extra","surprise"],"building": ["door", "inside", "outside"], "business": ["transaction", "stock", "finance", "consulting"], "situation": ["problem", "solution", "solved"], "want": ["something", "food", "badly"], "attack": ["violently", "him"], "computer": ["program", "problems", "keyboard", "software"]} 

def isIndicator(word):
    return word in indicators

def evokeFrame(word):
    return frame_properties[indicators[word]]


"""
    
class Frame:
    def __init__(self, name,props):
	    self.name = name
		self.properties = props

	def get_name(self):
	    return self.name

	def get_frame_relations(self):
	    return self.properties
"""
