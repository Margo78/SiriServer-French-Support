#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
import socket, sys, os
import ping

class ClientSSH(Plugin):
    HOST = '192.168.0.29'
    PORT = 5000
    mySocket = ""
    ConnectionOK = True

    @register("fr-FR", u"Éteindre (ordinateur|pc)")
    def Envoyer_Bonjour(self, speech, language):
        # 1) cration du socket :
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2) envoi d'une requte de connexion au serveur :
        try:
            self.mySocket.connect((self.HOST, self.PORT))
            ConnectionOK = True
        except socket.error:
            ConnectionOK = False
            print "La connexion a echoue."

        # 3) Dialogue avec le serveur :
        msgServeur = self.mySocket.recv(1024)
        self.mySocket.send("shutdown")
        msgServeur = self.mySocket.recv(1024)

        # 4) Fermeture de la connexion :
        print "Connexion interrompue."
        self.mySocket.close()
        self.say(u"Le pc s'eteint")
        self.complete_request()

    @register("fr-FR",u"(Ping pc)")
    def Ping_Pc(self, speech, language):
        Retour_Ping = ping.verbose_ping("192.168.0.29",2,1)
        self.say(Retour_Ping)
        self.complete_request()
