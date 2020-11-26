# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
# TODO: NewsStory

class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def is_phrase_in(self, text):
        phrase = self.phrase.lower()
        phrase_words = phrase.split()
        cleaned_text = ""
        for letter in str.lower(text):
            if not letter.isalpha():
                cleaned_text += " "
            else:
                cleaned_text += letter
        if phrase in " ".join(cleaned_text.split()):
            if phrase_words[len(phrase_words) - 1] in cleaned_text.split():
                return True
        return False

# trig = PhraseTrigger("hello world")
# print(trig.is_phrase_in("he hello *$%&^%world ld"))

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
    
'''
cuddly    = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
spaces    = NewsStory('', 'Did you see a purple     cow?', '', '', datetime.now())
caps      = NewsStory('', 'The farmer owns a really PURPLE cow.', '', '', datetime.now())
exact     = NewsStory('', 'purple cow', '', '', datetime.now())

plural    = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
brown     = NewsStory('', 'How now brown cow.', '' ,'', datetime.now())
badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
nospaces  = NewsStory('', 'purplecowpurplecowpurplecow', '', '', datetime.now())
nothing   = NewsStory('', 'I like poison dart frogs.', '', '', datetime.now())

s1 = TitleTrigger('PURPLE COW')
s2  = TitleTrigger('purple cow')
for trig in [s1, s2]:
    print(trig.evaluate(cuddly))# "TitleTrigger failed to fire when the phrase appeared in the title.")
    print(trig.evaluate(exclaim))# "TitleTrigger failed to fire when the words were separated by exclamation marks.")
    print(trig.evaluate(symbols))# "TitleTrigger failed to fire when the words were separated by assorted punctuation.")
    print(trig.evaluate(spaces))# "TitleTrigger failed to fire when the words were separated by multiple spaces.")
    print(trig.evaluate(caps))# "TitleTrigger failed to fire when the phrase appeared with both uppercase and lowercase letters.")
    print(trig.evaluate(exact))# "TitleTrigger failed to fire when the words in the phrase were the only words in the title.")
    print("--------------")
    print(trig.evaluate(plural))# "TitleTrigger fired when the words in the phrase were contained within other words.")
    print(trig.evaluate(separate))# "TitleTrigger fired when the words in the phrase were separated by other words.")
    print(trig.evaluate(brown))# "TitleTrigger fired when only part of the phrase was found.")
    print(trig.evaluate(badorder))# "TitleTrigger fired when the words in the phrase appeared out of order.")
    print(trig.evaluate(nospaces))# "TitleTrigger fired when words were not separated by spaces or punctuation.")
    print(trig.evaluate(nothing))# "TitleTrigger fired when none of the words in the phrase appeared.")
    print("-----------")
'''

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    def evaluate(self, story):
        story_time = story.get_pubdate()
        if story_time.tzinfo == None:
            story_time = story_time.replace(tzinfo=pytz.timezone("EST"))
        else:
            story_time = story_time.astimezone(pytz.timezone('EST'))
        return self.time > story_time

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    def evaluate(self, story):
        story_time = story.get_pubdate()
        if story_time.tzinfo == None:
            story_time = story_time.replace(tzinfo=pytz.timezone("EST"))
        else:
            story_time = story_time.astimezone(pytz.timezone('EST'))
        return self.time < story_time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, T):
        self.trigger = T
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.trigger_1 = T1
        self.trigger_2 = T2
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.trigger_1 = T1
        self.trigger_2 = T2
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered_stories = []
    for story in stories:
        triggered = False
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break
    return filtered_stories

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_dict = {}
    for line in lines[:-1]:
        element = line.split(',')
        if element[1] == 'TITLE':
            trigger_dict[element[0]] = TitleTrigger(element[2])
        if element[1] == 'DESCRIPTION':
            trigger_dict[element[0]] = DescriptionTrigger(element[2])
        if element[1] == 'AFTER':
            trigger_dict[element[0]] = AfterTrigger(element[2])
        if element[1] == 'BEFORE':
            trigger_dict[element[0]] = BeforeTrigger(element[2])
        if element[1] == 'NOT':
            trigger_dict[element[0]] = NotTrigger(element[2])
        if element[1] == 'AND':
            trigger_dict[element[0]] = AndTrigger(element[2], element[3])
        if element[1] == 'OR':
            trigger_dict[element[0]] = OrTrigger(element[2], element[3])
    trigger_list = []
    for trigger in lines[-1].split(',')[1:]:
        trigger_list.append(trigger_dict[trigger])
    # print(lines)
    # print(trigger_list)
    return trigger_list
    # print(lines) # for now, print it so you see what it contains!

# read_trigger_config('triggers.txt')

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

