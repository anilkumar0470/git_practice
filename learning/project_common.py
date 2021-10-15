
import os
import sys
import argparse
import json
import logging

log = logging.getLogger(__name__)

def get_valid_job_disable_names_dict(
):
    valid_job_disable_names_dict = {
        'ci-release-project': True,
        'ci-release-recipe-repo': True,
        'ci-review': True,
        'ci-review-recipe-repo': True,
        'ci-update-manifest': True,
        'ci-update-manifest-recipe-repo': True,
        'junk':True
    }
    return valid_job_disable_names_dict

def get_valid_job_disable_values_dict(
):
    valid_job_disable_values_dict = {
        None: False,
        True: True,
        False: False,
        'enabled': False,
        'disabled': True,
    }
    return valid_job_disable_values_dict


def get_sanity_job_defaults_dict(
):
    sanity_job_defaults_dict = {
        'job_agent': 'sanity-docker',
        'job_docker_container_flag': True,
        'job_failure_handling': 'pipeline-failure',
        'job_timeout_amount': 5,
        'job_timeout_unit': 'HOURS',
        'job_quiet_period': 0,
        'job_template': 'ci-pipeline-job.xml',
        'job_type': 'explicit',
        "junk":True
        #'job_wait_flag': None,
        #'job_propagate_flag': None,
    }
    return sanity_job_defaults_dict


def get_build_job_defaults_dict(
):
    build_job_defaults_dict = {
        'job_agent': 'build-oia',
        'job_docker_container_flag': False,
        'job_failure_handling': 'pipeline-failure',
        'job_timeout_amount': 5,
        'job_timeout_unit': 'HOURS',
        'job_quiet_period': 0,
        'job_template': 'ci-pipeline-job.xml',
        'job_type': 'inline',
    }
    return build_job_defaults_dict


def create_sanity(
):
    return


def create_tfwk_sanity(
        **keywords
):
    #
    # for some of the defaults below need to check with groovy (or documentation) against its default to simply leave it out from here
    #
    sanity_job_defaults_dict = get_sanity_job_defaults_dict()
    job_keyword_defs_list = [
        {
            'job_field_name': 'job_name',
            'mandatory_keyword_flag': True,
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_agent',
        },
        {
            'job_field_name': 'job_docker_container_flag',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_failure_handling',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_timeout_amount',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_timeout_unit',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_quiet_period',
        },
        {
            'job_field_name': 'job_template',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_type',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'disable_flag',
            'job_field_save': 'save-never',
        },
        {
            'job_field_name': 'job_command_dict',
            'job_field_save': 'save-never',
        },
    ]
    job_keyword_defs_dict = {}
    for field_defs_dict in job_keyword_defs_list:
        job_field_name = field_defs_dict['job_field_name']
        job_keyword_defs_dict[job_field_name] = field_defs_dict
    job_dict = {}
    for keyword_name in sorted(keywords):
        if keyword_name not in job_keyword_defs_dict:
            raise ValueError(f'create_tfwk_sanity: unsupported keyword {repr(keyword_name)} in keywords {repr(keywords)}')
        field_defs_dict = job_keyword_defs_dict[keyword_name]
        job_field_name = field_defs_dict['job_field_name']
        job_field_save = field_defs_dict.get('job_field_save', 'save-if-not-None')
        if job_field_save != 'save-never':
            mandatory_keyword_flag = field_defs_dict.get('mandatory_keyword_flag', False)
            default_value = sanity_job_defaults_dict.get(job_field_name, None)
            keyword_value = keywords.get(job_field_name, default_value)
            save_field_flag = False
            if job_field_save == 'save-always':
                save_field_flag = True
            elif job_field_save == 'save-if-not-None':
                if keyword_value is not None:
                    save_field_flag = True
            elif job_field_save == 'save-if-not-default':
                if keyword_value is not None:
                    if default_value is None:
                        save_field_flag = True
                    elif keyword_value != default_value:
                        save_field_flag = True
            if save_field_flag:
                job_dict[job_field_name] = keyword_value

    # disable_flag
    disable_flag = keywords.get('disable_flag', None)
    if disable_flag is not None:
        valid_job_disable_values_dict = get_valid_job_disable_values_dict()
        if isinstance(disable_flag, dict):
            valid_job_disable_names_dict = get_valid_job_disable_names_dict()
            for name in sorted(disable_flag):
                if name not in valid_job_disable_names_dict:
                    raise ValueError(f'invalid disable_flag dict field {repr(name)}, valid ones are {repr(sorted(valid_job_disable_names_dict))}')
                value = disable_flag[name]
                if value not in valid_job_disable_values_dict:
                    raise ValueError(f'invalid disable_flag dict field {repr(name)} value of {repr(value)}, valid values are {repr(list(valid_job_disable_values_dict.keys()))}')
                # "disable_flag.ci-release-project": True,
                job_dict['disable_flag.' + name] = valid_job_disable_values_dict[value]
        else:
            if disable_flag not in valid_job_disable_values_dict:
                raise ValueError(f'invalid disable_flag dict field "disable_flag" value of {repr(disable_flag)}, valid values are {repr(list(valid_job_disable_values_dict.keys()))}')
            job_dict['disable_flag'] = valid_job_disable_values_dict[disable_flag]

    job_command_dict = keywords.get('job_command_dict', None)

    mandatory_keywords_list = [
        'job_name',
        'job_command_dict',
    ]
    mandatory_job_keywords_list = [
        # '--test-engine',
        # '--device-wait-startup-timeout',
        '--testcases-project-name',
        '--topology-tag-name',
        # '--topology-type',
        '--define-instance-attr',
        # '--test-engine-begin',
        # '--run-init-begin',
        'testcase_list',
    ]

    for name in mandatory_keywords_list:
        value = keywords.get(name, None)
        if value is None:
            raise ValueError(f'create_tfwk_sanity: did not specify {repr(name)} in keywords {repr(keywords)}')

    for name in mandatory_job_keywords_list:
        value = job_command_dict.get(name, None)
        if value is None:
            raise ValueError(f'create_tfwk_sanity: did not specify {repr(name)} in job_command_dict {repr(job_command_dict)}')

    testcases_project_name = job_command_dict.get('--testcases-project-name', None)
    test_engine = job_command_dict.get('--test-engine', 'Warrior')
    device_wait_startup_timeout = str(job_command_dict.get('--device-wait-startup-timeout', 1800))
    topology_tag_name = job_command_dict.get('--topology-tag-name', None)
    topology_type = job_command_dict.get('--topology-type', None)
    define_instance_attr = job_command_dict.get('--define-instance-attr', None)
    test_engine_begin = job_command_dict.get('--test-engine-begin', None)
    run_init_begin = job_command_dict.get('--run-init-begin', None)
    testcase_list = job_command_dict.get('testcase_list', None)

    job_command_list = [
        'ci-project-sanity-tfwk',
        '--',
    ]
    if testcases_project_name is not None:
        job_command_list += [
            '--testcases-project-name', testcases_project_name,
        ]
    job_command_list += [
        '--',
    ]
    if test_engine is not None:
        job_command_list += [
            '--test-engine', test_engine,
        ]
    if device_wait_startup_timeout is not None:
        job_command_list += [
            '--device-wait-startup-timeout', str(device_wait_startup_timeout),
        ]
    if topology_tag_name is not None:
        job_command_list += [
            '--topology-tag-name', topology_tag_name,
        ]
    if topology_type is not None:
        job_command_list += [
            '--topology-type', topology_type,
        ]
    if define_instance_attr is not None:
        for device_name in sorted(define_instance_attr):
            # "--define-instance-attr", "NE1/main", "image-info-config-name=main-FSS2-PD01",
            device_dict = define_instance_attr[device_name]
            for name in sorted(device_dict):
                value = device_dict[name]
                job_command_list += [
                    '--define-instance-attr', device_name, name + '=' + value,
                ]
            job_command_list += [
                '--add-instance', device_name,
            ]
    if test_engine_begin is not None:
        job_command_list += [
            '--test-engine-begin',
        ]
        job_command_list += test_engine_begin
        job_command_list += [
            '--test-engine-end',
        ]
    if run_init_begin is not None:
        job_command_list += [
            '--run-init-begin',
        ]
        job_command_list += run_init_begin
        job_command_list += [
            '--run-init-end',
        ]
    job_command_list += [
        '--',
    ]
    if testcase_list is not None:
        job_command_list += testcase_list

    job_dict['job_command_list'] = job_command_list

    return job_dict


def create_build_job(
        **keywords
):
    #
    # for some of the defaults below need to check with groovy (or documentation) against its default to simply leave it out from here
    #
    sanity_job_defaults_dict = get_sanity_job_defaults_dict()
    job_keyword_defs_list = [
        {
            'job_field_name': 'job_name',
            'mandatory_keyword_flag': True,
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_agent',
        },
        {
            'job_field_name': 'job_docker_container_flag',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_failure_handling',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_timeout_amount',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_timeout_unit',
            'job_field_save': 'save-if-not-default',
        },
        {
            'job_field_name': 'job_quiet_period',
        },
        {
            'job_field_name': 'job_template',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'job_type',
            'job_field_save': 'save-always',
        },
        {
            'job_field_name': 'disable_flag',
            'job_field_save': 'save-never',
        },
        {
            'job_field_name': 'job_command_dict',
            'job_field_save': 'save-never',
        },
    ]
    job_keyword_defs_dict = {}
    for field_defs_dict in job_keyword_defs_list:
        job_field_name = field_defs_dict['job_field_name']
        job_keyword_defs_dict[job_field_name] = field_defs_dict
    job_dict = {}
    for keyword_name in sorted(keywords):
        if keyword_name not in job_keyword_defs_dict:
            raise ValueError(f'create_tfwk_sanity: unsupported keyword {repr(keyword_name)} in keywords {repr(keywords)}')
        field_defs_dict = job_keyword_defs_dict[keyword_name]
        job_field_name = field_defs_dict['job_field_name']
        job_field_save = field_defs_dict.get('job_field_save', 'save-if-not-None')
        if job_field_save != 'save-never':
            mandatory_keyword_flag = field_defs_dict.get('mandatory_keyword_flag', False)
            default_value = sanity_job_defaults_dict.get(job_field_name, None)
            keyword_value = keywords.get(job_field_name, default_value)
            save_field_flag = False
            if job_field_save == 'save-always':
                save_field_flag = True
            elif job_field_save == 'save-if-not-None':
                if keyword_value is not None:
                    save_field_flag = True
            elif job_field_save == 'save-if-not-default':
                if keyword_value is not None:
                    if default_value is None:
                        save_field_flag = True
                    elif keyword_value != default_value:
                        save_field_flag = True
            if save_field_flag:
                job_dict[job_field_name] = keyword_value

    disable_flag = keywords.get('disable_flag', None)
    if disable_flag is not None:
        valid_job_disable_values_dict = get_valid_job_disable_values_dict()
        if isinstance(disable_flag, dict):
            valid_job_disable_names_dict = get_valid_job_disable_names_dict()
            for name in sorted(disable_flag):
                if name not in valid_job_disable_names_dict:
                    raise ValueError(f'invalid disable_flag dict field {repr(name)}, valid ones are {repr(sorted(valid_job_disable_names_dict))}')
                value = disable_flag[name]
                if value not in valid_job_disable_values_dict:
                    raise ValueError(f'invalid disable_flag dict field {repr(name)} value of {repr(value)}, valid values are {repr(list(valid_job_disable_values_dict.keys()))}')
                # "disable_flag.ci-release-project": True,
                job_dict['disable_flag.' + name] = valid_job_disable_values_dict[value]
        else:
            if disable_flag not in valid_job_disable_values_dict:
                raise ValueError(f'invalid disable_flag dict field "disable_flag" value of {repr(disable_flag)}, valid values are {repr(list(valid_job_disable_values_dict.keys()))}')
            job_dict['disable_flag'] = valid_job_disable_values_dict[disable_flag]

    job_command_dict = keywords.get('job_command_dict', None)

    mandatory_keywords_list = [
        'job_name',
        'job_command_dict',
    ]

    for name in mandatory_keywords_list:
        value = keywords.get(name, None)
        if value is None:
            raise ValueError(f'create_tfwk_sanity: did not specify {repr(name)} in keywords {repr(keywords)}')

    job_command_list = [
        'ci-project-build',
    ]
    if 'image_dict' in job_command_dict:
        flag_mapper_dict = {
            'archive_flag': '-archive',
        }
        image_dict = job_command_dict['image_dict']
        for image_name in sorted(image_dict):
            job_command_list += [
                '-image', image_name,
            ]
            image_info_dict = image_dict[image_name]
            if image_info_dict is not None:
                for flag_name in sorted(image_info_dict):
                    if flag_name not in flag_mapper_dict:
                        raise ValueError(f'create_build_job: unsupported flag_name {repr(flag_name)} in image_info_dict {repr(image_info_dict)}')
                    flag_value = flag_mapper_dict[flag_name]
                    job_command_list += [
                        flag_value, image_name,
                    ]


    job_param_list = [
        {
            'field_name': '-machine',
            'field_type': 'double',
        },
        {
            'field_name': '--enable-devtoolset-flag',
        },
        {
            'field_name': '-cache',
        },
    ]
    for job_param_dict in job_param_list:
        field_name = job_param_dict['field_name']
        if field_name in job_command_dict:
            job_command_list += [
                field_name,
            ]
            field_type = job_param_dict.get('field_type', 'single')
            if field_type != 'single':
                field_value = job_command_dict[field_name]
                if field_value is not None:
                    job_command_list += [
                        field_value,
                    ]


    job_dict['job_command_list'] = job_command_list

    return job_dict


def get_job_tree(
        build_job_list,
        sanity_job_list,
        job_name_prefix,
        info_text,
):
    num_build_jobs = len(build_job_list)
    num_sanity_jobs = len(sanity_job_list)

    build_parallel_job = build_job_list
    if num_build_jobs > 1:
        build_parallel_job = {
            'job_type': 'parallel',
            'job_name': job_name_prefix + '-build-p',
            'job_list': build_job_list,
        }

    sanity_parallel_job = sanity_job_list
    if num_sanity_jobs > 1:
        sanity_parallel_job = {
            'job_type': 'parallel',
            'job_name': job_name_prefix + '-sanity-p',
            'job_list': sanity_job_list,
        }

    job_tree = None
    if num_build_jobs <= 0:
        if num_sanity_jobs <= 0:
            log.info(f'get_job_tree: {info_text}there are no jobs to add')
        else:
            log.info(f'get_job_tree: {info_text}adding {repr(num_sanity_jobs)} sanity jobs')
            job_tree = sanity_parallel_job
    elif num_sanity_jobs <= 0:
        log.info(f'get_job_tree: {info_text}adding {repr(num_build_jobs)} build jobs')
        job_tree = build_parallel_job
    else:
        log.info(f'get_job_tree: {info_text}adding {repr(num_build_jobs)} build jobs and {repr(num_sanity_jobs)} sanity jobs')
        job_tree = {
            'job_type': 'serial',
            'job_name': job_name_prefix + '-s',
            'job_list': [
                build_parallel_job,
                sanity_parallel_job,
            ],
        }
    return job_tree





def store_jobs_for_category(
        category_name,
        category_value,
        category_job_dict,
        category_job_list,
):
    if category_value in category_job_dict:
        raise ValueError(f'store_sanity_jobs_for_image_group: cannot store multiple sanity jobs into same category {repr(category_name)} value {repr(category_value)}')
    log.info(f'store_jobs_for_category: {len(category_job_list):3d} jobs into category {repr(category_name)} value {repr(category_value)}')
    category_job_dict[category_value] = category_job_list
    return


def add_image_group_sanity_jobs(
        project_info_json,
        job_build_dict,
        job_sanity_dict,
):
    # ['image_group_list'][]['sanity_jobs']
    if 'image_group_list' in project_info_json:
        image_group_list = project_info_json['image_group_list']
        for image_group_dict in image_group_list:
            image_group_name = image_group_dict['image_group_name']
            image_group_build_job_list = job_build_dict.get(image_group_name, [])
            image_group_sanity_job_list = job_sanity_dict.get(image_group_name, [])
            job_tree = get_job_tree(
                build_job_list=image_group_build_job_list,
                sanity_job_list=image_group_sanity_job_list,
                job_name_prefix='ig',
                info_text=f'image group {repr(image_group_name)}: ',
            )
            if job_tree is not None:
                image_group_dict['sanity_jobs'] = job_tree
    return


def add_qa_jobs(
        project_info_json,
        job_build_dict,
        job_sanity_dict,
):
    log.info(f'add_qa_jobs: - build')
    for name in sorted(job_build_dict):
        log.info(f'add_qa_jobs:   {repr(name)}')
    log.info(f'add_qa_jobs: - sanity')
    for name in sorted(job_sanity_dict):
        log.info(f'add_qa_jobs:   {repr(name)}')
    qa_build_job_list = job_build_dict['qa_jobs']
    qa_sanity_job_list = job_sanity_dict['qa_jobs']
    qa_jobs = get_job_tree(
        build_job_list=qa_build_job_list,
        sanity_job_list=qa_sanity_job_list,
        job_name_prefix='qa',
        info_text='qa: ',
    )
    if qa_jobs is not None:
        project_info_json['qa_jobs'] = qa_jobs
    return


def add_recipe_repo_jobs(
        project_info_json,
        job_build_dict,
        job_sanity_dict,
):
    # ['recipe_repo_list'][]['recipe_repo_jobs']
    if 'recipe_repo_list' in project_info_json:
        recipe_repo_list = project_info_json['recipe_repo_list']
        for recipe_repo_dict in recipe_repo_list:
            recipe_repo_name = recipe_repo_dict['recipe_repo_name']
            recipe_repo_build_job_list = job_build_dict.get(recipe_repo_name, [])
            recipe_repo_sanity_job_list = job_sanity_dict.get(recipe_repo_name, [])
            job_tree = get_job_tree(
                build_job_list=recipe_repo_build_job_list,
                sanity_job_list=recipe_repo_sanity_job_list,
                job_name_prefix='rr',
                info_text=f'recipe repo {repr(recipe_repo_name)}: ',
            )
            if job_tree is not None:
                recipe_repo_dict['recipe_repo_jobs'] = job_tree
    return


def add_reg_build_jobs(
        project_info_json,
        job_build_dict,
        job_sanity_dict,
):
    # ['regression_defs']['regression_image_group_list'][]['build_jobs']
    # log.info(f'add_reg_build_jobs: - build')
    # for name in sorted(job_build_dict):
    #     log.info(f'add_reg_build_jobs:   {repr(name)}')
    # log.info(f'add_reg_build_jobs: - sanity')
    # for name in sorted(job_sanity_dict):
    #     log.info(f'add_reg_build_jobs:   {repr(name)}')
    reg_jobs = get_job_tree(
        build_job_list=job_build_dict.get('regression_image_group_list', []),
        sanity_job_list=job_sanity_dict.get('regression_image_group_list', []),
        job_name_prefix='reg-build',
        info_text='reg-build: ',
    )
    #if reg_jobs is not None:
    #    project_info_json['reg_jobs'] = reg_jobs
    return


def add_reg_sanity_jobs(
        project_info_json,
        job_build_dict,
        job_sanity_dict,
):
    # ['regression_defs']['regression_test_list'][]['regression_jobs']
    reg_jobs = get_job_tree(
        build_job_list=job_build_dict.get('regression_test_list', []),
        sanity_job_list=job_sanity_dict.get('regression_test_list', []),
        job_name_prefix='reg-sanity',
        info_text='reg-sanity: ',
    )
    #if reg_jobs is not None:
    #    project_info_json['reg_jobs'] = reg_jobs
    return

