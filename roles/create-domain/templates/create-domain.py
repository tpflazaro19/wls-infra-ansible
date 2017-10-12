# db properties
db_server_name = '{{ dbserver_name }}'
db_server_port = '{{ dbserver_port }}'
db_service = '{{ dbserver_service }}'
data_source_url='jdbc:oracle:thin:@//' + db_server_name + ':' + db_server_port + '/' + db_service;
data_source_user_prefix= '{{ repository_prefix }}'

# weblogic properties
domain_application_home = '{{ applications_home }}/{{ domain_name }}'
domain_home = '{{ domains_home }}/{{ domain_name }}'
domain_name = '{{ domain_name }}'
java_home = '{{ jdk_folder }}'
middleware_home = '{{ middleware_home }}'
weblogic_home = '{{ weblogic_home }}'

weblogic_template=weblogic_home + '/common/templates/wls/wls.jar'
jrf_template=middleware_home + '/oracle_common/common/templates/wls/oracle.jrf_base_template.jar'
em_template=middleware_home + '/em/common/templates/wls/oracle.em_wls_template.jar'

# Update weblogic template
# ------------------------
print "Updating wls.jar template"
readTemplate(weblogic_template)

# Change domain properties
setOption('DomainName', domain_name)
setOption('OverwriteDomain', 'true')
setOption('JavaHome', java_home)
setOption('ServerStartMode', 'prod')

# Change Admin Server properties
cd('/Security/base_domain/User/weblogic')
cmo.setName('{{ weblogic_admin }}')
cmo.setUserPassword('{{ weblogic_admin_pass }}')
cd('/Server/AdminServer')
cmo.setName('{{ admin_server_name }}')
cmo.setListenPort(int('{{ admin_server_port }}'))
cmo.setListenAddress('')

print "Save domain"
writeDomain(domain_home)
closeTemplate()

# Add ADF
# -------
print 'Read domain'
readDomain(domain_home)

print 'Add templates'
addTemplate(jrf_template)
addTemplate(em_template)
setOption('AppDir', domain_application_home)

# Add DB information
cd('/JDBCSystemResource/LocalSvcTblDataSource/JdbcResource/LocalSvcTblDataSource')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','oracle.jdbc.OracleDriver')
set('URL',data_source_url)
set('PasswordEncrypted', '{{ datasource_password }}' )
cd('Properties/NO_NAME_0')
cd('Property/user')
cmo.setValue(data_source_user_prefix + '_STB')
getDatabaseDefaults()

cd("/SecurityConfiguration/" + domain_name);
cmo.setNodeManagerUsername('{{ nodemanager_username }}');
cmo.setNodeManagerPasswordEncrypted('{{ nodemanager_password }}');

cd('/Server/' + '{{ admin_server_name }}');
create('{{ admin_server_name }}','SSL');
cd('SSL/' + '{{ admin_server_name }}');
cmo.setHostnameVerificationIgnored(true);
cmo.setHostnameVerifier(None);
cmo.setTwoWaySSLEnabled(false);
cmo.setClientCertificateEnforced(false);

updateDomain()
closeDomain()

