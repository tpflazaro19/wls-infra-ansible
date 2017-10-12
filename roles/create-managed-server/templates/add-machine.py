ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to Admin Server
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Create a Machine
# ================
edit();
startEdit();

cd('/')
cmo.createMachine('{{ server_hostname }}')
cd('/Machines/{{ server_hostname }}/NodeManager/{{ server_hostname }}')
cmo.setListenAddress('{{ node_manager_listen_address }}')

save()
activate()

# Exit
exit()
