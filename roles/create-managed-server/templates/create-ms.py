ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to Admin Server
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Create a ManagedServer
# ======================
edit();
startEdit();

cd('/')
cmo.createServer('{{ managed_server_name }}')
cd('/Servers/' + '{{ managed_server_name }}')
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))

# Default Channel for ManagedServer
# ---------------------------------
cmo.setListenAddress('')
cmo.setListenPort({{ managed_server_port }})
# Custom Startup Parameters because NodeManager writes wrong AdminURL in startup.properties
# -----------------------------------------------------------------------------------------
cd('/Servers/' + '{{ managed_server_name }}' + '/ServerStart/' + '{{ managed_server_name }}')
arguments = '-Djava.security.egd=file:/dev/./urandom {{ min_java_heap_size }} {{ max_java_heap_size }}'
cmo.setArguments(arguments)

applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');
# applyJRF wil call save and activate
exit()
