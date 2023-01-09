import paramiko
ssh = paramiko.SSHClient()

#Pour éviter l'erreur "d'hôtes non reconnu"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#pour se connecter à la machine en ssh par une clé rsa
ssh.connect('192.168.0.26', username='root', password="password")#key_filename="C:\\Users\\Pot2Fleur\\.ssh\\id_rsa")

# sftp = ssh.open_sftp()
# # Upload
# filepath = "/home/tapha"
# localpath = "C:\\Users\\Pot2Fleur\\Desktop\\courspython.txt"
# sftp.put(localpath,filepath)

#on lance la commande uptime et ce retour sera coupé en trois parties et stockés dans ces var
stdin, stdout, stderr = ssh.exec_command('echo "<VirtualHost *:80>\n\tServerAdmin gregoire@localhost\n\tDocumentRoot /home/tapha/sites/\n\tErrorLog /home/tapha/sites/logs/error.log\n\tCustomLog /home/tapha/sites/logs/access.log combined\n</VirtualHost>" > /etc/apache2/sites-available/extranet.conf')
commands = ['mkdir -p /home/tapha/sites/logs', 'ls /etc/apache2/sites-available/', 'echo test > /home/tapha/sites/index.html', 'a2ensite extranet.conf', 'systemctl restart apache2', 'a2dissite 000-default.conf', 'chown -R www-data:www-data /home/tapha/sites/'] 

#stdin, stdout, stderr = ssh.exec_command('sudo apt install -y apache2')

for command in commands: 
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.readlines())



#on affiche les lignes du retour


#on ferme la connexion ssh
ssh.close()