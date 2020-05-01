from ps5 import TitleTrigger
from ps5 import PhraseTrigger
from ps5 import NewsStory
for i in ["purple cow", "PURPLE COW"]:
	t = TitleTrigger(i)
	N = NewsStory("", "Did you see a purple     cow?", "", "", "")
	print (t.evaluate(N))