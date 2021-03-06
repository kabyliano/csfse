#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import*
from subprocess import call

def generate(event):
	matr=matricule.get().upper()
	head=open(r'head.tex' , 'r')
	foot=open(r'foot.tex' , 'r')
	s=head.read()+"Le Doyen de la Faculté des \\textbf{Sciences Exactes}\\\\\
\n\\\\%\n\
certifie que l'étudiant(e):\\\\\
\n\\\\%\n\
Nom: \\textbf{"+nom.get().upper()+"}\\\\\
\n\\\\%\n\
Prénom : \\textbf{"+prenom.get().capitalize()+"}\\\\\
\n\\\\%\n\
Né(e) le : \\textbf{"+date_nais.get()+"}   à : \\textbf{"+ville_nais.get().capitalize()+"}\\\\\
\n\\\\%\n\
est inscrit(e)  en \\textbf{Deuxième année.}\\\\\
\n\\\\%\n\
Matricule : \\textbf{"+matr+"}\\\\\
\n\\\\%\n\
Domaine : \\textbf{Mathématiques et Informatique}\\\\\
\n\\\\%\n\
Filière : \\textbf{Informatique}\\\\\
\n\\\\%\n\
Spécialité : \\textbf{Génie Logiciel}\\\\\
\n\\\\%\n\
Diplôme préparé : \\textbf{Master}\\\\\
\n\\\\%\n\
\\textbf{Année universitaire : 2015/2016}\
\n\\\\%\n\
\\begin{flushright}\
\\begin{pspicture}(4,0in)\
\\psbarcode{"+matr+"}{includecheck height=0.4}{code128}\
\\end{pspicture}\\\
\n\\\\%\n\
Béjaia, le 25/11/2015\\\\P/Le Doyen\
\\end{flushright}"+foot.read()
	head.close()
	foot.close()
	certificat = open(r''+matr+'.tex' , 'w')
	certificat.write(s)
	certificat.close()
	call(["xelatex", matr+".tex"])
	call(["evince", matr+".pdf"])

window=Tk()
window.pack_propagate(0)
nom=Entry(window, background='white')
prenom=Entry(window, background='white')
date_nais=Entry(window, background='white')
ville_nais=Entry(window, background='white')
matricule=Entry(window, background='white')
matricule.bind("<Return>",generate)

certificat = Label(text = 'Certificats de Scolarité')
certificat.grid(row=0)

labelNom = Label(text = 'Nom :')
labelPrenom = Label(text = 'Prenom :')
labelDate_nais = Label(text = 'Date de naissance :')
labelVille_nais = Label(text = 'ville de naissance :')
labelMatricule = Label(text = 'Matricule :')

labelNom.grid(row=1)
labelPrenom.grid(row=2)
labelDate_nais.grid(row=3)
labelVille_nais.grid(row=4)
labelMatricule.grid(row=5)

nom.grid(row=1,column=1)
prenom.grid(row=2,column=1)
date_nais.grid(row=3,column=1)
ville_nais.grid(row=4,column=1)
matricule.grid(row=5,column=1)

generer=Button(window, text="Générer", fg="black")
generer.bind("<Button-1>",generate)
quit=Button(window, text="Quitter", fg="red",command=window.destroy)
generer.grid(row=6,column=0)
quit.grid(row=6,column=1)

window.mainloop()
