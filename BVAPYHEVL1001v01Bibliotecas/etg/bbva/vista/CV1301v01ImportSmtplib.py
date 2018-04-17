#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	17Abr2018
# Periódo           :   17Abr/2018
# Objetivo			:	Import Smtplib
# Fecha Edición		:
# Descripción		:   Mandar correos, se requiere un servidor de correo
#==============================================================================
import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)
print("Successfully sent email")
smtpObj.quit()
