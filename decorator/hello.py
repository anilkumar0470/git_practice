# from decoratos import new_decorator
#
# @new_decorator
# def display():
#     print("displaying ..")
# #display()
#
# @new_decorator
# def display_name(name):
#     print("name is {}".format(name))
# display_name(name="anil")


d = [
         {'sonar_line_coverage_alert': 'no', 'component_index_today': 100.0, 'quality_gate_alert': 'no',
          'sonar_issues_today': 0, 'sonar_issues_alert': 'no', 'component_index_alert': 'yes', 'cpplint_today': 'yes',
          'component': 'cia_led', 'quality_gate_prev': 'Gate Level-7', 'pylint_prev': 'NA',
          'manager': 'Clint.Bauer@fujitsu.com', 'cppcheck_prev': 'yes', 'quality_gate_today': u'Gate Level-7',
          'owner': 'Daniel.Cao@fujitsu.com', 'sonar_issues_prev': 0, 'valgrind_enable_alert': 'no',
          'sonar_line_coverage_today': 79.4, 'component_type': '', 'lead': 'Clint.Bauer@fujitsu.com',
          'component_index_prev': 100.0, 'cppcheck_today': 'yes', 'pylint_today': 'NA', 'valgrind_enable_prev': 'yes',
          'cpplint_prev': 'yes', 'sonar_line_coverage_prev': 79.4, 'valgrind_enable_today': 'yes', 'project': u'fss3',
          'static_analysis_alert': 'no'},
         {'sonar_line_coverage_alert': 'no', 'component_index_today': 100.0, 'quality_gate_alert': 'no',
          'sonar_issues_today': 0, 'sonar_issues_alert': 'no', 'component_index_alert': 'yes', 'cpplint_today': 'yes',
          'component': 'cia_control_layer', 'quality_gate_prev': 'Gate Level-7', 'pylint_prev': 'NA',
          'manager': 'Clint.Bauer@fujitsu.com', 'cppcheck_prev': 'yes', 'quality_gate_today': u'Gate Level-7',
          'owner': 'Clint.Bauer@fujitsu.com', 'sonar_issues_prev': 0, 'valgrind_enable_alert': 'no',
          'sonar_line_coverage_today': 97.6, 'component_type': '', 'lead': 'Clint.Bauer@fujitsu.com',
          'component_index_prev': 100.0, 'cppcheck_today': 'yes', 'pylint_today': 'NA', 'valgrind_enable_prev': 'yes',
          'cpplint_prev': 'yes', 'sonar_line_coverage_prev': 97.6, 'valgrind_enable_today': 'yes', 'project': u'fss3',
          'static_analysis_alert': 'no'},
         {'sonar_line_coverage_alert': 'no', 'component_index_today': 80.0, 'quality_gate_alert': 'no',
          'sonar_issues_today': 0, 'sonar_issues_alert': 'no', 'component_index_alert': 'yes', 'cpplint_today': 'yes',
          'component': 'rack_manager', 'quality_gate_prev': 'Fujitsu Way', 'pylint_prev': 'NA',
          'manager': 'Clint.Bauer@fujitsu.com', 'cppcheck_prev': 'yes', 'quality_gate_today': u'Fujitsu Way',
          'owner': 'Daniel.Cao@fujitsu.com', 'sonar_issues_prev': 0, 'valgrind_enable_alert': 'no',
          'sonar_line_coverage_today': 98.5, 'component_type': '', 'lead': 'Clint.Bauer@fujitsu.com',
          'component_index_prev': 80.0, 'cppcheck_today': 'yes', 'pylint_today': 'NA', 'valgrind_enable_prev': 'yes',
          'cpplint_prev': 'yes', 'sonar_line_coverage_prev': 98.5, 'valgrind_enable_today': 'yes', 'project': u'fss3',
          'static_analysis_alert': 'no'},
         {'sonar_line_coverage_alert': 'no', 'component_index_today': 80.0, 'quality_gate_alert': 'no',
          'sonar_issues_today': 0, 'sonar_issues_alert': 'no', 'component_index_alert': 'yes', 'cpplint_today': 'yes',
          'component': 'cia_red_app', 'quality_gate_prev': 'Gate Level-7', 'pylint_prev': 'NA',
          'manager': 'Clint.Bauer@fujitsu.com', 'cppcheck_prev': 'yes', 'quality_gate_today': u'Gate Level-7',
          'owner': 'John.Li@fujitsu.com', 'sonar_issues_prev': 0, 'valgrind_enable_alert': 'no',
          'sonar_line_coverage_today': 71.8, 'component_type': '', 'lead': 'Clint.Bauer@fujitsu.com',
          'component_index_prev': 80.0, 'cppcheck_today': 'yes', 'pylint_today': 'NA', 'valgrind_enable_prev': None,
          'cpplint_prev': 'yes', 'sonar_line_coverage_prev': 71.8, 'valgrind_enable_today': None, 'project': u'fss3',
          'static_analysis_alert': 'no'}]


import  pdb
# pdb.set_trace()
all_email_id_list = []
for row in d:
    if row["manager"]:
        if row["manager"] not in all_email_id_list:
            all_email_id_list.append(row["manager"])
    if row["owner"]:
        if row["owner"] not in all_email_id_list:
            all_email_id_list.append(row["owner"])
    if row["lead"]:
        if row["lead"] not in all_email_id_list:
            all_email_id_list.append(row["lead"])
print(all_email_id_list)
list2 = ['test@gmail.com', "hello@gmail.com"]
all_email_id_list.extend(list2)
print(all_email_id_list)