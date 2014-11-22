from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty

from kivy.uix.textinput import TextInput 
from getngrams import getNgrams
import string
from util import *
from frame_corpus import *

class Fill(FloatLayout):
    word0 = StringProperty()
    pass

class Interface(App):

    text = StringProperty()

    word0 = StringProperty()
    word1 = StringProperty()
    word2 = StringProperty()
    word3 = StringProperty()
    word4 = StringProperty()

    my_cont = ObjectProperty()
    my_frames = []
    seen = {}
    
    long_enough = BooleanProperty()

    def get_prediction(self):
        pass
        
    def update_text(self,user_input):
        indicated = False
        properties = ["","","","",""]
        content = user_input.split()
        if len(content) >= 4:
            if user_input[-1] == ' ':
                content = [s.translate(string.maketrans("",""), string.punctuation) for s in user_input.split()]
                for word in content:
                    if isIndicator(word):
                        if word in self.seen:
                            if self.seen[word] >=3: 
                                break
                            else:
                                self.seen[word] +=1
                        else:
                            self.seen[word] =1

                        properties = evokeFrame(word)
                        indicated = True
                        break

                if indicated and len(properties) < 5: 
                    query = getNgrams("{0} {1} *".format(content[-1], content[-2]))
                    for i in range(5-len(properties)):
                        properties.append(query[-i+1].split()[-1])
                else:
                    if not indicated:
                        query = getNgrams("{0} {1} *".format(content[-1], content[-2]))
                        if len(query) < 5:
                            query = getNgrams("{0} *".format(content[-1]))
                        self.word0 = query[-1].split()[-1]
                        self.word1 = query[-2].split()[-1]
                        self.word2 = query[-3].split()[-1]
                        self.word3 = query[-4].split()[-1]
                        self.word4 = query[-5].split()[-1]

                if indicated:
                    self.word0 = properties[0]
                    self.word1 = properties[1]
                    self.word2 = properties[2]
                    self.word3 = properties[3]
                    self.word4 = properties[4]
                           
    def build(self):
        self.Instance = Fill()
        return self.Instance

if __name__ == "__main__":
    Interface().run()
