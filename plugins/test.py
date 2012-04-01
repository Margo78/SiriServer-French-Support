while Reponse_Supplementaire <> None :
            if language == 'fr-FR':
                answer = self.ask("Le resultat de votre calcul est " + str(Result_calcul) + " mais encore ?")
                print answer
                if (answer == "Stop") or (answer == "") :
                    Reponse_Supplementaire = None
