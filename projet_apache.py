import paramiko
ssh = paramiko.SSHClient()

#Pour éviter l'erreur "d'hôtes non reconnu"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#pour se connecter à la machine en ssh par une clé rsa
ssh.connect('192.168.0.26', username='tapha', key_filename="C:\\Users\\Pot2Fleur\\.ssh\\id_rsa")

# sftp = ssh.open_sftp()
# # Upload
# filepath = "/home/tapha"
# localpath = "C:\\Users\\Pot2Fleur\\Desktop\\courspython.txt"
# sftp.put(localpath,filepath)

#on lance la commande uptime et ce retour sera coupé en trois parties et stockés dans ces var
stdin, stdout, stderr = ssh.exec_command('apt update && apt install -y apache2')
#on affiche les lignes du retour
print(stdout.readlines())

#on ferme la connexion ssh
ssh.close()