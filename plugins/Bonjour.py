#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *

class Bonjou(Plugin):
    @register("fr-FR", "(Preuve)|(Preuve.*)|(Prouve)|(Prouve.*)")
    def Preuve_brunsson(self, speech, language):
        if language == 'fr-FR':
            self.say("Oui oui, c'est bien bruno qui m'heberge et me fait dire ce que je veux")
        self.complete_request()

    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)")
    @register("fr-FR", "(Bonjour)|(Salut)")
    def rep_bonjour(self, speech, language):
        print language
        if language == 'de-DE':
            self.say("Hallo.")
        elif language == 'en-US':
            self.say("Hello")
        elif language == 'fr-FR':
            self.say("Bonjour, comment ca va aujourd'hui ?")
        self.complete_request()
   
    @register("de-DE", ".*Sinn.*Leben.*")
    @register("en-US", ".*Meaning.*Life.*")
    @register("fr-FR", ".*Sens.*Vie.*")
    def SensDeLavie(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Willst du das wirklich wissen?")
            self.say(u"Du hast \"{0}\" gesagt!".format(answer))
        elif language == 'fr-FR' :
            answer= self.ask("Tu tiens vraiment a le savoir?")
            self.say("Et bien cherche!")
        else:
            self.say("I shouldn't tell you!")
        self.complete_request()
