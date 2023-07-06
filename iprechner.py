import subprocess

s_all_ips = subprocess.check_output(['ipconfig'], text=True) # String all IP-Addresses from Terminal comman ipconfig
i_pos_def_sw = s_all_ips.index('Default Switch') # locate position of Default Switch...
i_pos_ip = (i_pos_def_sw + s_all_ips[i_pos_def_sw:].index('IPv4-Adresse  . . . . . . . . . . :')
          +len('IPv4-Adresse  . . . . . . . . . . :')) #... 1st IP Adresse
i_pos_subm = (i_pos_def_sw + s_all_ips[i_pos_def_sw:].index('Subnetzmaske  . . . . . . . . . . :') 
            + len('Subnetzmaske  . . . . . . . . . . :'))# ... 1st Subnetz Maske
s_hit_ip = s_all_ips[i_pos_ip:i_pos_ip+15].strip() # String IP Addresse strip spaces
s_hit_subm = s_all_ips[i_pos_subm:i_pos_subm+15].strip() #String Subnetz Mask stropped spaces
l_s_hit_ip = s_hit_ip.split('.') # IP String to List
l_s_hit_subm = s_hit_subm.split('.') # Maske String to List

del i_pos_def_sw
del i_pos_ip
del i_pos_subm

# Prefix calculation from Subnet Mask , by counting binäry 1s
i_ip_prefix = (str(bin(int(l_s_hit_subm[0]))) + str(bin(int(l_s_hit_subm[1]))) 
             + str(bin(int(l_s_hit_subm[2]))) + str(bin(int(l_s_hit_subm[3])))).count('1') 

i_net_locate = 4 - ((32 - i_ip_prefix) // 8) # calculate wich IP octett the Prefix ends = (0.1.2.3)
i_blocksize = ((i_net_locate * 8) - i_ip_prefix) ** 2

if int(l_s_hit_ip[i_net_locate-1]) % i_blocksize != 0:
       print('Error 1 Network not correct')
       quit()

print('Network: '+ '.'.join(l_s_hit_ip[:i_net_locate]) + (( 4 - i_net_locate ) * '.0'))
print('Broadcast: '+ '.'.join(l_s_hit_ip[:i_net_locate - 1]) + '.' + str(int(l_s_hit_ip[i_net_locate-1]) + i_blocksize - 1) + '.255')
print('Last available IP: '+ '.'.join(l_s_hit_ip[:i_net_locate - 1]) + '.' + str(int(l_s_hit_ip[i_net_locate-1]) + i_blocksize - 1) + '.254')
print('Host IP-Adresse: ' + str(s_hit_ip) + '/' + str(i_ip_prefix))
print('Subnet Mask: ', s_hit_subm)
print("Blocksize: ", i_blocksize)