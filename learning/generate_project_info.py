#!/usr/bin/env python3

import os
import sys
import argparse
import json
import project_common
import logging
import subprocess

log = logging.getLogger(__name__)

g_project = 'xxx'


class tree_item_cl:
    def __init__(
            self,
            name=None,
    ):
        self.child_dict = {}
        self.child_list = []
        self.name = name
        self.value = None


    def get_name(
            self,
    ):
        return self.name


    def get_value(
            self,
    ):
        return self.value


    def set_value(
            self,
            value,
    ):
        self.value = value


    def __contains__(
            self,
            key,
    ):
        """ implement the 'in' operator """
        value = False
        if key in self.child_dict:
            value = True
        return value


    def __getitem__(
            self,
            key,
    ):
        """ implement the dictionary read operation """
        value = None
        if key in self.child_dict:
            value = self.child_dict[key]
        return value


    def get_num_children(
            self,
    ):
        return len(self.child_list)


    def get_child_list(
            self,
    ):
        child_list = []
        for name in self.child_list:
            child_list.append(self.child_dict[name])
        return child_list


    def get_child_sequence(
            self,
    ):
        for name in self.child_list:
            yield self.child_dict[name]


    def add_child(self,name,):
        if name in self.child_dict:
            tree_item_obj = self.child_dict[name]
        else:
            tree_item_obj = tree_item_cl(name=name)
            self.child_dict[name] = tree_item_obj
            self.child_list.append(name)
        return tree_item_obj


    def get_obj(
            self,
            name_list,
    ):
        current_tree_item_obj = self
        for name in name_list:
            if name not in current_tree_item_obj.child_dict:
                current_tree_item_obj = None
                break
            current_tree_item_obj = current_tree_item_obj.child_dict[name]
        return current_tree_item_obj


    def create_obj(
            self,
            name_list,
    ):
        current_tree_item_obj = self
        for name in name_list:
            child_tree_item_obj = current_tree_item_obj.add_child(
                name=name,
            )
            current_tree_item_obj = child_tree_item_obj
        return current_tree_item_obj


    def add_value(
            self,
            name_list,
            value,
    ):
        #log.info(f'ntp-amend-for-docker-containers.tree_item_cl.add_value: begin')
        current_tree_item_obj = self
        for name in name_list:
            #log.info(f'ntp-amend-for-docker-containers.tree_item_cl.add_value:   name {name}')
            child_tree_item_obj = current_tree_item_obj.add_child(
                name=name,
            )
            current_tree_item_obj = child_tree_item_obj
        child_tree_item_obj.set_value(
            value=value,
        )
        return child_tree_item_obj


def get_item_text(
        data_item,
        type,
        current_indent='',
):
    item_text = ''
    indent_amount = '    '
    if isinstance(data_item, dict):
        if type != 'param':
            item_text += '{\n'
        for name in sorted(data_item):
            if type != 'param':
                item_text += current_indent + indent_amount + f'{repr(name)}: '
            else:
                item_text += current_indent + indent_amount + name + '='
            item_text += get_item_text(
                data_item=data_item[name],
                type='data',
                #current_indent=current_indent+'{'+f'{repr(name)}'+'}',
                current_indent=current_indent+indent_amount,
            )
            item_text += ',\n'
        if type != 'param':
            item_text += current_indent + '}'
    elif isinstance(data_item, list):
        item_text += '[\n'
        index = 0
        for child_item in data_item:
            item_text += current_indent + indent_amount + get_item_text(
                data_item=child_item,
                type='data',
                #current_indent=current_indent+'['+f'{repr(index)}'+']',
                current_indent=current_indent+indent_amount,
            )
            item_text += ',\n'
            index += 1
        item_text += current_indent + ']'
    else:
        #log.info(current_indent + f' = {repr(data_item)}')
        item_text += f'{repr(data_item)}'
    return item_text


def create_job_info_dict(
        job_json_dict,
        expected_job_category=None,
):
    job_info_dict = {
        'job_json_dict': job_json_dict,
    }
    job_name = job_json_dict['job_name']
    job_command_list = job_json_dict['job_command_list']
    job_command_name = job_command_list[0]
    topology_tag_name = None

    job_dict = None
    job_category = None
    get_create_job_text_func = None

    if job_command_name == 'ci-project-build':
        job_category = 'build'
        get_create_job_text_func = get_create_build_job_text
        job_dict = process_build_params(
            job_command_list=job_command_list,
        )
        #log.info('  job_json_dict: ' + json.dumps(job_json_dict, indent = 4, sort_keys=True))
        #log.info('  job_command_list: ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
        #log.info('  job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))
        #log.info(f'  bld:  job_command_list {repr(job_command_list)}')
        get_create_build_job_text(
            job_json_dict=job_json_dict,
            job_dict=job_dict,
        )
    elif job_command_name == 'ci-project-sanity':
        job_category = 'sanity'
        #log.info(f'  job_command_list {repr(job_command_list)}')
    elif job_command_name == 'ci-native':
        job_category = 'sanity'
        #log.info(f'  job_command_list {repr(job_command_list)}')
    elif job_command_name == 'ci-project-qa-build':
        job_category = 'build'
        #log.info(f'  job_command_list {repr(job_command_list)}')
    elif job_command_name == 'ci-project-qa-test':
        job_category = 'sanity'
        #log.info(f'  job_command_list {repr(job_command_list)}')
    elif job_command_name == 'ci-regression-get-image':
        job_category = 'build'
        #log.info(f'  job_command_list {repr(job_command_list)}')
    elif job_command_name == 'ci-project-sanity-tfwk':
        job_category = 'sanity'
        get_create_job_text_func = get_create_tfwk_job_text
        job_dict = process_tfwk_params(
            job_command_list=job_command_list,
        )
        #log.info(f'  job_command_list {repr(job_command_list)}')
        #log.info(f'  job_dict: {repr(job_dict)}')
        #log.info('  job_command_list: ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
        #log.info('  job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))
        #log.info(f'  ntp:  tptag {repr(job_dict["--topology-tag-name"])}, images {repr(job_dict["image_list"])}')
        get_create_tfwk_job_text(
            job_json_dict=job_json_dict,
            job_dict=job_dict,
        )
    elif job_command_name == 'ci-project-sanity-ntp':
        job_category = 'sanity'
        get_create_job_text_func = None
        job_dict = process_ntp_params(
            job_command_list=job_command_list,
        )
        job_info_dict['job_dict'] = job_dict
        #log.info('  job_command_list: ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
        #log.info('  job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))
        #log.info(f'  {repr(job_command_name)}: topology_tag_name {repr(job_dict["--topology-tag-name"])}, image_list {repr(job_dict["image_list"])}')
        #log.info(f'  tfwk: tptag {repr(job_dict["--ntp-topology-tag"])}, images {repr(job_dict["image_list"])}')
        #add_topology(
        #    topology_dict=topology_dict,
        #    job_json_dict=job_json_dict,
        #    job_dict=job_dict,
        #)
    else:
        raise ValueError(f'unknown job command {repr(job_command_name)} in job_command_list {repr(job_command_list)}')

    if expected_job_category is not None:
        if expected_job_category != job_category:
            raise ValueError(f'create_job_info_dict: job_category {repr(job_category)} != expected_job_category {repr(expected_job_category)}')
    job_info_dict['job_dict'] = job_dict
    job_info_dict['job_category'] = job_category
    job_info_dict['get_create_job_text_func'] = get_create_job_text_func

    #log.info(f'  {repr(job_command_name)}: topology_tag_name {repr(job_dict["--topology-tag-name"])}, image_list {repr(job_dict["image_list"])}, job_name {repr(job_name)}')
    #log.info(f'  job_command_list {repr(job_command_list)}')
    return job_info_dict


def add_job_info_to_context(
        job_dict,
        context_name_list,
        job_json_dict,
        expected_job_category,
):
    job_index_dict = job_dict['job_index_dict']
    tree_item_obj = job_dict['tree_item_obj']

    job_info_dict = create_job_info_dict(
        job_json_dict=job_json_dict,
        expected_job_category=expected_job_category,
    )
    job_category = job_info_dict['job_category']

    context_index = ':'.join(context_name_list)

    if context_index in job_index_dict:
        context_info_dict = job_index_dict[context_index]
    else:
        context_info_dict = {
            'context_name_list': context_name_list,
            'context_name': context_name_list[0],
            'context_index': context_index,
            'job_info_list': [],
        }
        job_index_dict[context_index] = context_info_dict
        #log.info(f'add_job_info_to_context: new context_index {repr(context_index)}')
    job_info_list = context_info_dict['job_info_list']
    job_info_list.append(job_info_dict)

    #log.info(f'add_job_info_to_context: context_name_list ' + json.dumps(context_name_list, indent = 4, sort_keys=True))
    category_context_list = context_name_list + [ job_category ]
    index = 0
    max = len(category_context_list)
    while index <= max:
        tmp_list = category_context_list[:index]
        #log.info(f'add_job_info_to_context: tmp_list ' + json.dumps(tmp_list, indent = 4, sort_keys=True))
        new_obj = tree_item_obj.create_obj(
            name_list=tmp_list,
        )
        context_info_dict = new_obj.get_value()
        if context_info_dict is None:
            context_info_dict = {
                'context_name_list': tmp_list,
                'context_index': ':'.join(tmp_list),
                'job_info_list': [],
            }
            if index > 0:
                context_info_dict['context_name'] = tmp_list[0]
            new_obj.set_value(
                value=context_info_dict,
            )
        job_info_list = context_info_dict['job_info_list']
        job_info_list.append(job_info_dict)
        index += 1
    return


def process_item(
        job_dict,
        data_item,
        indent='',
        context_list=[],
):
    if isinstance(data_item, dict):
        for name in sorted(data_item):
            if name == 'job_command_list':
                #log.info(indent + f' = {repr(data_item[name])}')
                #log.info(f'{repr(context_list)}' + f' = {repr(data_item[name])}')
                context_name = context_list[0]['name']
                context_index = context_name
                context_info_dict = {
                    'context_name': context_name,
                    'job_info_list': [],
                }
                context_name_list = [
                    context_index,
                ]
                expected_job_category = None
                if context_name == 'image_group_list':
                    expected_job_category = 'sanity'
                    image_group_name = context_list[2]['parent']['image_group_name']
                    context_name_list.append(image_group_name)
                    context_info_dict['image_group_name'] = image_group_name
                    context_index += ':' + image_group_name
                elif context_name == 'qa_jobs':
                    pass
                elif context_name == 'recipe_repo_list':
                    recipe_repo_name = context_list[2]['parent']['recipe_repo_name']
                    context_name_list.append(recipe_repo_name)
                    context_info_dict['recipe_repo_name'] = recipe_repo_name
                    context_index += ':' + recipe_repo_name
                elif context_name == 'regression_defs':
                    # regression_image_group_list
                    # regression_test_list
                    regression_section = context_list[1]['name']
                    context_name_list.append(regression_section)
                    context_info_dict['regression_section'] = regression_section
                    context_index += ':' + regression_section
                    parent_dict = context_list[3]['parent']
                    image_group_name = parent_dict['image_group_name']
                    context_info_dict['image_group_name'] = image_group_name
                    context_name_list.append(image_group_name)
                    context_index += ':' + image_group_name
                    if regression_section == 'regression_image_group_list':
                        expected_job_category = 'build'
                    elif regression_section == 'regression_test_list':
                        expected_job_category = 'sanity'
                        test_group_name = parent_dict.get('test_group_name', image_group_name)
                        context_info_dict['test_group_name'] = test_group_name
                    else:
                        raise ValueError(f'process_item: invalid regression_section {repr(regression_section)}')
                else:
                    for item_dict in context_list:
                        name = item_dict['name']
                        log.error(f'process_item: context name {repr(name)}')
                    raise ValueError(f'process_item: invalid root context name {repr(context_name)}')

                add_job_info_to_context(
                    job_dict=job_dict,
                    context_name_list=context_name_list,
                    job_json_dict=data_item,
                    expected_job_category=expected_job_category,
                )
            else:
                context_dict = {
                    'name': name,
                    'parent': data_item,
                }
                import pdb
                # pdb.set_trace()
                process_item(
                    job_dict=job_dict,
                    data_item=data_item[name],
                    indent=indent+'{'+f'{repr(name)}'+'}',
                    context_list=context_list + [ context_dict ]
                )
    elif isinstance(data_item, list):
        index = 0
        for child_item in data_item:
            context_dict = {
                'name': index,
                'parent': data_item,
            }
            process_item(
                job_dict=job_dict,
                data_item=child_item,
                indent=indent+'['+f'{repr(index)}'+']',
                    context_list=context_list + [ context_dict ]
            )
            index += 1
    else:
        #log.info(indent + f' = {repr(data_item)}')
        pass
    return


def build_param_store(
        job_dict,
        job_command_list,
        index,
):
    job_dict[job_command_list[index]] = job_command_list[index+1]
    return 1


def build_param_image(
        job_dict,
        job_command_list,
        index,
):
    param_name = job_command_list[index]
    image_name = job_command_list[index+1]
    #if param_name in job_dict:
    #    image_dict = job_dict[param_name]
    #else:
    #    image_dict = {}
    #    job_dict[param_name] = image_dict
    #image_dict[image_name] = True

    if 'image_dict' in job_dict:
        image_dict = job_dict['image_dict']
    else:
        image_dict = {}
        job_dict['image_dict'] = image_dict

    if image_name in image_dict:
        image_info_dict = image_dict[image_name]
    else:
        image_info_dict = {}
        image_dict[image_name] = image_info_dict

    field_dict = {
        '-image': None,
        '-archive': 'archive_flag',
    }
    if param_name not in field_dict:
        raise ValueError(f'build_param_image: un-implemented image option {repr(param_name)} in job_command_list {repr(job_command_list)}')
    field_name = field_dict[param_name]
    if field_name is not None:
        image_info_dict[field_name] = True
    return 1


def build_param_bool(
        job_dict,
        job_command_list,
        index,
):
    job_dict[job_command_list[index]] = True
    return 0


def process_build_params(
        job_command_list,
):
    job_dict = {}
    index = 0
    defs_dict = {
        'ci-project-build': { },
        '-machine': { 'func': build_param_store },
        '-image': { 'func': build_param_image },
        '-archive': { 'func': build_param_image },
        '-cache': { 'func': build_param_bool },
        '--enable-devtoolset-flag': { 'func': build_param_bool },
    }
    skip_count = 0
    for param in job_command_list:
        if skip_count > 0:
            #log.info(f'process_build_params: skip {repr(param)}')
            skip_count -= 1
        else:
            if param not in defs_dict:
                log.error(f'process_build_params: invalid param {repr(param)} in job_command_list ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
                raise ValueError(f'process_build_params: invalid param {repr(param)} in job_command_list {repr(job_command_list)}')

            param_dict = defs_dict[param]
            if 'func' in param_dict:
                #log.info(f'process_build_params: handle {repr(param)}')
                func = param_dict['func']
                skip_count = func(
                    job_dict=job_dict,
                    job_command_list=job_command_list,
                    index=index,
                )
        index += 1
    if '-image' in job_dict:
        image_dict = job_dict['-image']
        image_name = 'meta-ide-support'
        if image_name not in image_dict:
            raise ValueError(f'process_build_params: strange, did not find image_name {repr(image_name)} in job_command_list {repr(job_command_list)}')
    return job_dict

def get_create_build_job_text(
        job_json_dict,
        job_dict,
        indent='',
):
    #log.info('get_create_build_job_text: job_json_dict: ' + json.dumps(job_json_dict, indent = 4, sort_keys=True))
    #log.info('get_create_build_job_text: job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))

    # # INFO:   job_json_dict: {
    #     "disable_flag.ci-release-project": true,
    #     "disable_flag.ci-release-recipe-repo": false,
    #     "disable_flag.ci-review": true,
    #     "disable_flag.ci-review-recipe-repo": false,
    #     "disable_flag.ci-update-manifest": false,
    #     "disable_flag.ci-update-manifest-recipe-repo": true,
    #     "job_agent": "build-oia",
    #     "job_command_list": [
    #         "ci-project-build",
    #         "-machine",
    #         "qemux86-64",
    #         "-image",
    #         "fss-image-full-layer1",
    #         "-archive",
    #         "fss-image-full-layer1",
    #         "-image",
    #         "meta-ide-support",
    #         "-cache",
    #         "--enable-devtoolset-flag"
    #     ],
    #     "job_docker_container_flag": false,
    #     "job_failure_handling": "pipeline-failure",
    #     "job_name": "build-fss-image-full-layer1",
    #     "job_propagate_flag": true,
    #     "job_quiet_period": 0,
    #     "job_stash_flag": true,
    #     "job_timeout_amount": 3,
    #     "job_timeout_unit": "HOURS",
    #     "job_type": "inline",
    #     "job_unstash_flag": true,
    #     "job_wait_flag": true,
    #     "previous_job_method": "previous-job"
    # }
    # # INFO:   job_dict: {
    #     "--enable-devtoolset-flag": true,
    #     "-archive": {
    #         "fss-image-full-layer1": true
    #     },
    #     "-cache": true,
    #     "-image": {
    #         "fss-image-full-layer1": true,
    #         "meta-ide-support": true
    #     },
    #     "-machine": "qemux86-64"
    # }



    # job_dict = create_build_job(
    #     disable_flag={
    #         'ci-release-project': 'disabled',
    #         'ci-release-recipe-repo': 'enabled',
    #         'ci-review': 'disabled',
    #         'ci-review-recipe-repo': 'enabled',
    #         'ci-update-manifest': 'enabled',
    #         'ci-update-manifest-recipe-repo': 'disabled',
    #     },
    #     job_name='ci-webui-sanity',
    #     job_command_dict={
    #         '--testcases-project-name': 'fss3testcases',
    #         '--test-engine': 'Robot',
    #         '--device-wait-startup-timeout': 1800,
    #         '--topology-tag-name': 'NE1-main',
    #         '--topology-type': None,
    #         '--define-instance-attr': {
    #             'NE1/main': {
    #                 'image-name': 'fws-image-validation',
    #             },
    #         },
    #         '--test-engine-begin': [
    #             "--variable", "REMOTE_URL:http://rtxoialp10:4444/wd/hub",
    #             "--variable", "BROWSER:chrome",
    #             "--variable", "product:FSSPD2",
    #         ],
    #         '--run-init-begin': None,
    #         'testcase_list': [
    #             'robot-testcases/webui_automation/Projects/WebUI_sanity_project/webui_sanity.robot',
    #         ],
    #     },
    # )
    job_command_dict = {}

    bool_keyword_list = [
        {
            'src_name': '--enable-devtoolset-flag',
        },
        {
            'src_name': '-cache',
        },
    ]
    for key_info_dict in bool_keyword_list:
        src_name = key_info_dict['src_name']
        dst_name = key_info_dict.get('dst_name', src_name)
        if src_name in job_dict:
            job_command_dict[dst_name] = job_dict[src_name]

    simple_keyword_list = [
        {
            'src_name': '-machine',
        },
        {
            'src_name': 'image_dict',
        },
    ]
    for key_info_dict in simple_keyword_list:
        src_name = key_info_dict['src_name']
        dst_name = key_info_dict.get('dst_name', src_name)
        if src_name in job_dict:
            job_command_dict[dst_name] = job_dict[src_name]

    if '-image' in job_dict:
        for image_name in sorted(job_dict['-image']):
            pass

    job_keyword_list = [
        {
            'src_name': 'job_name',
        },
        {
            'src_name': 'job_agent',
            'default_value': 'sanity-docker',
        },
        {
            'src_name': 'job_docker_container_flag',
            'default_value': False,
        },
        {
            'src_name': 'job_failure_handling',
        },
        {
            'src_name': 'job_timeout_amount',
        },
        {
            'src_name': 'job_timeout_unit',
        },
        {
            'src_name': 'job_quiet_period',
        },
        {
            'src_name': 'job_template',
        },
        {
            'src_name': 'job_type',
        },
    ]
    build_job_defaults_dict = project_common.get_build_job_defaults_dict()
    job_keyword_dict = {}
    for key_info_dict in job_keyword_list:
        src_name = key_info_dict['src_name']
        dst_name = key_info_dict.get('dst_name', src_name)
        if src_name in job_json_dict:
            default_value = build_job_defaults_dict.get(dst_name, None)
            json_value = job_json_dict[src_name]
            save_flag = False
            if json_value is None:
                save_flag = False
            elif default_value is None:
                save_flag = True
            elif json_value != default_value:
                save_flag = True
            if save_flag:
                job_keyword_dict[dst_name] = json_value

    if 'disable_flag' in job_json_dict:
        disable_flag = job_json_dict['disable_flag']
    else:
        have_changes_flag = False
        disable_flag = {}
        valid_job_disable_names_dict = project_common.get_valid_job_disable_names_dict()
        for name in sorted(valid_job_disable_names_dict):
            disable_name = 'disable_flag.' + name
            disable_value = job_json_dict.get(disable_name, False)
            if disable_value:
                have_changes_flag = True
                #disable_flag[disable_name] = disable_value
                #disable_flag[disable_name] = 'disabled'
                disable_flag[name] = 'disabled'
        if not have_changes_flag:
            disable_flag = None
    if disable_flag is not None:
        job_keyword_dict['disable_flag'] = disable_flag
    job_keyword_dict['job_command_dict'] = job_command_dict
    #log.info(f'get_create_build_job_text: job_keyword_dict: ' + json.dumps(job_keyword_dict, indent = 4, sort_keys=True))
    #log.info(f'get_create_build_job_text: job_command_dict: ' + json.dumps(job_command_dict, indent = 4, sort_keys=True))
    item_text = get_item_text(
        data_item=job_keyword_dict,
        type='param',
        current_indent=indent,
    )
    #log.info(f'item_text:\n' + item_text)
    job_text = 'create_build_job(\n' + item_text + indent + ')'

    #log.info(f'get_create_build_job_text: job_text:\n' + job_text)
    return job_text

def process_attr_dict(
        attr_dict,
        attributes,
):
    field_list = attributes.split(',')
    #log.info(f'process_attr_dict: - field_list {repr(field_list)}')
    for field_text in field_list:
        name, value = field_text.split('=')
        #log.info(f'process_attr_dict:   {repr(name)} = {repr(value)}')
        name = name.lstrip()
        add_flag = True
        if name == 'project':
            if value != g_project:
                raise ValueError(f'referencing a different project than {repr(g_project)} in attributes {repr(attributes)}')
            add_flag = False
        elif name == 'machine-name':
            if value == 'qemux86-64':
                add_flag = False
        if add_flag:
            attr_dict[name] = value
    return attr_dict


def tfwk_param_section(
        job_dict,
        job_command_list,
        index,
):
    job_dict['section_count'] += 1
    return 0


def tfwk_param_store(
        job_dict,
        job_command_list,
        index,
):
    job_dict[job_command_list[index]] = job_command_list[index+1]
    return 1


def tfwk_param_add_instance(
        job_dict,
        job_command_list,
        index,
):
    inst_list = job_command_list[index+1].split(',')
    for instance in inst_list:
        job_dict['instance_list'].append(instance)
    return 1


def tfwk_param_attr_defaults(
        job_dict,
        job_command_list,
        index,
):
    process_attr_dict(
        attr_dict=job_dict['attr_defaults_dict'],
        attributes=job_command_list[index+1],
    )
    return 1


def tfwk_param_instance_attr(
        job_dict,
        job_command_list,
        index,
):
    instance_attr_dict = job_dict['instance_attr_dict']
    attr_dict = {}
    process_attr_dict(
        attr_dict=attr_dict,
        attributes=job_command_list[index+2],
    )
    inst_list = job_command_list[index+1].split(',')
    for name in attr_dict:
        for instance in inst_list:
            if instance in instance_attr_dict:
                inst_dict = instance_attr_dict[instance]
            else:
                inst_dict = {}
                instance_attr_dict[instance] = inst_dict
            inst_dict[name] = attr_dict[name]
    return 2


def param_block_begin(
        job_dict,
        job_command_list,
        index,
        block_end_param,
        block_list,
):
    counter = 1
    max = len(job_command_list)
    while index < max:
        index += 1
        param = job_command_list[index]
        #log.info(f'param_block_begin: param[{repr(index)}] = {repr(param)}')
        if param == block_end_param:
            break
        block_list.append(param)
        counter += 1
    return counter


def tfwk_param_test_engine_begin(
        job_dict,
        job_command_list,
        index,
):
    counter = param_block_begin(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        block_end_param='--test-engine-end',
        block_list=job_dict['test_engine_block'],
    )
    return counter


def tfwk_param_run_init_begin(
        job_dict,
        job_command_list,
        index,
):
    counter = param_block_begin(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        block_end_param='--run-init-end',
        block_list=job_dict['run_init_block'],
    )
    return counter


def process_tfwk_params(
        job_command_list,
):
    job_dict = {}
    index = 0
    defs_dict = {
        'ci-project-sanity-tfwk': { },
        '--': { 'func': tfwk_param_section },
        '--test-engine': { 'func': tfwk_param_store },
        '--device-wait-startup-timeout': { 'func': tfwk_param_store },
        '--testcases-project-name': { 'func': tfwk_param_store },
        '--topology-tag-name': { 'func': tfwk_param_store },
        '--topology-type': { 'func': tfwk_param_store },
        '--add-instance': { 'func': tfwk_param_add_instance },
        '--define-attr-defaults': { 'func': tfwk_param_attr_defaults },
        '--define-instance-attr': { 'func': tfwk_param_instance_attr },
        '--test-engine-begin': { 'func': tfwk_param_test_engine_begin },
        '--run-init-begin': { 'func': tfwk_param_run_init_begin },
    }
    job_dict['attr_defaults_dict'] = {}
    job_dict['instance_attr_dict'] = {}
    job_dict['instance_list'] = []
    job_dict['testcase_list'] = []
    job_dict['test_engine_block'] = []
    job_dict['run_init_block'] = []
    job_dict['section_count'] = 0
    skip_count = 0
    for param in job_command_list:
        if skip_count > 0:
            #log.info(f'process_tfwk_params: skip {repr(param)}')
            skip_count -= 1
        elif job_dict['section_count'] == 3:
            #log.info(f'process_tfwk_params: testcase {repr(param)}')
            job_dict['testcase_list'].append(param)
        else:
            if param not in defs_dict:
                log.error(f'process_tfwk_params: invalid param {repr(param)} in job_command_list ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
                raise ValueError(f'process_tfwk_params: invalid param {repr(param)} in job_command_list {repr(job_command_list)}')

            param_dict = defs_dict[param]
            if 'func' in param_dict:
                #log.info(f'process_tfwk_params: handle {repr(param)}')
                func = param_dict['func']
                skip_count = func(
                    job_dict=job_dict,
                    job_command_list=job_command_list,
                    index=index,
                )
        index += 1
    image_name_by_instance_dict = {}
    image_list = []
    image_dict = {}
    attr_defaults_dict = job_dict['attr_defaults_dict']
    instance_attr_dict = job_dict['instance_attr_dict']
    instance_all_attr_dict = {}
    for instance in job_dict['instance_list']:
        image_name = None

        if instance in instance_attr_dict:
            inst_dict = instance_attr_dict[instance]
        else:
            inst_dict = {}
            instance_attr_dict[instance] = inst_dict

        if instance in instance_all_attr_dict:
            inst_all_dict = instance_all_attr_dict[instance]
        else:
            inst_all_dict = {}
            instance_all_attr_dict[instance] = inst_all_dict

        for name in attr_defaults_dict:
            inst_all_dict[name] = attr_defaults_dict[name]
        for name in inst_dict:
            inst_all_dict[name] = inst_dict[name]

        if 'image-name' in inst_dict:
            image_name = inst_dict['image-name']
        elif 'image-name' in job_dict['attr_defaults_dict']:
            image_name = job_dict['attr_defaults_dict']['image-name']
        if image_name is None:
            raise ValueError(f'missing image name for instance {repr(instance)} in ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
        image_name_by_instance_dict[instance] = image_name
        image_list.append(image_name)
        image_dict[image_name] = True
    job_dict['image_name_by_instance_dict'] = image_name_by_instance_dict
    job_dict['image_list'] = image_list
    job_dict['image_dict'] = image_dict
    job_dict['instance_all_attr_dict'] = instance_all_attr_dict

    if len(job_dict['testcase_list']) <= 0:
        del job_dict['testcase_list']
    if len(job_dict['test_engine_block']) <= 0:
        del job_dict['test_engine_block']
    if len(job_dict['run_init_block']) <= 0:
        del job_dict['run_init_block']

    return job_dict


def get_create_tfwk_job_text(
        job_json_dict,
        job_dict,
        indent='',
):
    #log.info('get_create_tfwk_job_text: job_json_dict: ' + json.dumps(job_json_dict, indent = 4, sort_keys=True))
    #log.info('get_create_tfwk_job_text: job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))

    # job_dict = create_tfwk_sanity(
    #     disable_flag={
    #         'ci-release-project': 'disabled',
    #         'ci-release-recipe-repo': 'enabled',
    #         'ci-review': 'disabled',
    #         'ci-review-recipe-repo': 'enabled',
    #         'ci-update-manifest': 'enabled',
    #         'ci-update-manifest-recipe-repo': 'disabled',
    #     },
    #     job_name='ci-webui-sanity',
    #     job_command_dict={
    #         '--testcases-project-name': 'fss3testcases',
    #         '--test-engine': 'Robot',
    #         '--device-wait-startup-timeout': 1800,
    #         '--topology-tag-name': 'NE1-main',
    #         '--topology-type': None,
    #         '--define-instance-attr': {
    #             'NE1/main': {
    #                 'image-name': 'fws-image-validation',
    #             },
    #         },
    #         '--test-engine-begin': [
    #             "--variable", "REMOTE_URL:http://rtxoialp10:4444/wd/hub",
    #             "--variable", "BROWSER:chrome",
    #             "--variable", "product:FSSPD2",
    #         ],
    #         '--run-init-begin': None,
    #         'testcase_list': [
    #             'robot-testcases/webui_automation/Projects/WebUI_sanity_project/webui_sanity.robot',
    #         ],
    #     },
    # )
    job_command_dict = {}
    simple_keyword_list = [
        {
            'src_name': '--test-engine',
        },
        {
            'src_name': '--device-wait-startup-timeout',
        },
        {
            'src_name': '--testcases-project-name',
        },
        {
            'src_name': '--topology-tag-name',
        },
        {
            'src_name': '--topology-type',
        },
        {
            'src_name': 'testcase_list',
        },
        {
            'src_name': 'instance_all_attr_dict',
            'dst_name': '--define-instance-attr',
        },
        {
            'src_name': 'test_engine_block',
            'dst_name': '--test-engine-begin',
        },
        {
            'src_name': 'run_init_block',
            'dst_name': '--run-init-begin',
        },
    ]
    for key_info_dict in simple_keyword_list:
        src_name = key_info_dict['src_name']
        dst_name = key_info_dict.get('dst_name', src_name)
        if src_name in job_dict:
            job_command_dict[dst_name] = job_dict[src_name]

    job_keyword_list = [
        {
            'src_name': 'job_name',
        },
        {
            'src_name': 'job_agent',
            'default_value': 'sanity-docker',
        },
        {
            'src_name': 'job_docker_container_flag',
            'default_value': True,
        },
        {
            'src_name': 'job_failure_handling',
        },
        {
            'src_name': 'job_timeout_amount',
        },
        {
            'src_name': 'job_timeout_unit',
        },
        {
            'src_name': 'job_quiet_period',
        },
        {
            'src_name': 'job_template',
        },
        {
            'src_name': 'job_type',
        },
        #{
        #    'src_name': 'job_wait_flag',
        #},
        #{
        #    'src_name': 'job_propagate_flag',
        #},
    ]
    sanity_job_defaults_dict = project_common.get_sanity_job_defaults_dict()
    job_keyword_dict = {}
    for key_info_dict in job_keyword_list:
        src_name = key_info_dict['src_name']
        dst_name = key_info_dict.get('dst_name', src_name)
        if src_name in job_json_dict:
            default_value = sanity_job_defaults_dict.get(dst_name, None)
            json_value = job_json_dict[src_name]
            save_flag = False
            if json_value is None:
                save_flag = False
            elif default_value is None:
                save_flag = True
            elif json_value != default_value:
                save_flag = True
            if save_flag:
                job_keyword_dict[dst_name] = json_value

    if 'disable_flag' in job_json_dict:
        disable_flag = job_json_dict['disable_flag']
    else:
        have_changes_flag = False
        disable_flag = {}
        valid_job_disable_names_dict = project_common.get_valid_job_disable_names_dict()
        for name in sorted(valid_job_disable_names_dict):
            disable_name = 'disable_flag.' + name
            disable_value = job_json_dict.get(disable_name, False)
            if disable_value:
                have_changes_flag = True
                #disable_flag[disable_name] = disable_value
                #disable_flag[disable_name] = 'disabled'
                disable_flag[name] = 'disabled'
        if not have_changes_flag:
            disable_flag = None
    if disable_flag is not None:
        job_keyword_dict['disable_flag'] = disable_flag
    job_keyword_dict['job_command_dict'] = job_command_dict
    #log.info(f'get_create_tfwk_job_text: job_keyword_dict: ' + json.dumps(job_keyword_dict, indent = 4, sort_keys=True))
    #log.info(f'get_create_tfwk_job_text: job_command_dict: ' + json.dumps(job_command_dict, indent = 4, sort_keys=True))
    item_text = get_item_text(
        data_item=job_keyword_dict,
        type='param',
        current_indent=indent,
    )
    #log.info(f'get_create_tfwk_job_text: item_text:\n' + item_text)
    job_text = 'create_tfwk_sanity(\n' + item_text + indent + ')'

    #log.info(f'get_create_tfwk_job_text: job_text:\n' + job_text)
    return job_text


def ntp_param_store(
        job_dict,
        job_command_list,
        index,
):
    job_dict[job_command_list[index]] = job_command_list[index+1]
    return 1


def ntp_param_enable_devtoolset_flag(
        job_dict,
        job_command_list,
        index,
):
    job_dict[job_command_list[index]] = True
    return 0


def ntp_param_store_instance_attr(
        job_dict,
        job_command_list,
        index,
        attr_name,
):
    instance_attr_dict = job_dict['instance_attr_dict']
    instance = job_command_list[index+1]
    if instance in instance_attr_dict:
        inst_dict = instance_attr_dict[instance]
    else:
        inst_dict = {}
        instance_attr_dict[instance] = inst_dict
    inst_dict[attr_name] = job_command_list[index+2]
    return 2


def ntp_param_instance_context_machine_name(
        job_dict,
        job_command_list,
        index,
):
    ntp_param_store_instance_attr(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        attr_name='machine-name',
    )
    return 2


def ntp_param_instance_context_image_name(
        job_dict,
        job_command_list,
        index,
):
    ntp_param_store_instance_attr(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        attr_name='image-name',
    )
    return 2


def ntp_param_instance_context_image_info_config_name(
        job_dict,
        job_command_list,
        index,
):
    ntp_param_store_instance_attr(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        attr_name='image-info-config-name',
    )
    return 2


def ntp_param_ntp_instance_context_regression_group(
        job_dict,
        job_command_list,
        index,
):
    ntp_param_store_instance_attr(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        attr_name='regression-group',
    )
    return 2


def ntp_param_instance_context_add(
        job_dict,
        job_command_list,
        index,
):
    inst_list = job_command_list[index+1].split(',')
    for instance in inst_list:
        job_dict['instance_list'].append(instance)
    return 1


def ntp_param_instance_configure_options_begin(
        job_dict,
        job_command_list,
        index,
):
    counter = param_block_begin(
        job_dict=job_dict,
        job_command_list=job_command_list,
        index=index,
        block_end_param='--instance-configure-options-end',
        block_list=job_dict['instance_configure_options'],
    )
    return counter




def ntp_param_warrior_testcase(
        job_dict,
        job_command_list,
        index,
):
    job_dict['testcase_list'].append(job_command_list[index+1])
    return 1


def process_ntp_params(
        job_command_list,
):
    job_dict = {}
    index = 0
    defs_dict = {
        'ci-project-sanity-ntp': { },
        '-test-framework-command': { 'func': ntp_param_store },
        '-device-wait-time': { 'func': ntp_param_store },
        '--ntp-topology-tag': { 'func': ntp_param_store },
        '--ntp-instance-context-machine-name': { 'func': ntp_param_instance_context_machine_name },
        '--ntp-instance-context-image-name': { 'func': ntp_param_instance_context_image_name },
        '--ntp-instance-context-image-info-config-name': { 'func': ntp_param_instance_context_image_info_config_name },
        '--ntp-instance-context-regression-group': { 'func': ntp_param_ntp_instance_context_regression_group },
        '--ntp-instance-context-add': { 'func': ntp_param_instance_context_add },
        '--instance-configure-options-begin': { 'func': ntp_param_instance_configure_options_begin },
        '--warrior-testcase': { 'func': ntp_param_warrior_testcase },
        '--enable-devtoolset-flag': { 'func': ntp_param_enable_devtoolset_flag },
    }
    #job_dict['attr_defaults_dict'] = {}
    job_dict['instance_attr_dict'] = {}
    job_dict['instance_list'] = []
    job_dict['testcase_list'] = []
    job_dict['instance_configure_options'] = []
    skip_count = 0
    for param in job_command_list:
        if skip_count > 0:
            #log.info(f'process_ntp_params: skip {repr(param)}')
            skip_count -= 1
        else:
            if param not in defs_dict:
                log.error(f'process_ntp_params: invalid param {repr(param)} in job_command_list ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
                raise ValueError(f'invalid param {repr(param)} in job_command_list {repr(job_command_list)}')

            param_dict = defs_dict[param]
            if 'func' in param_dict:
                #log.info(f'process_ntp_params: handle {repr(param)}')
                func = param_dict['func']
                skip_count = func(
                    job_dict=job_dict,
                    job_command_list=job_command_list,
                    index=index,
                )
        index += 1
    if '--ntp-topology-tag' in job_dict:
        if job_dict['--ntp-topology-tag'] == "1-NE-1-Blade":
            job_dict['--ntp-topology-tag'] = "NE1-main"
    image_name_by_instance_dict = {}
    image_list = []
    image_dict = {}
    for instance in job_dict['instance_list']:
        image_name = None
        instance_attr_dict = job_dict['instance_attr_dict']
        if instance in instance_attr_dict:
            inst_dict = instance_attr_dict[instance]
        else:
            inst_dict = {}
            instance_attr_dict[instance] = inst_dict
        if 'image-name' in inst_dict:
            image_name = inst_dict['image-name']
        elif 'image-name' in job_dict['attr_defaults_dict']:
            image_name = job_dict['attr_defaults_dict']['image-name']
        if image_name is None:
            raise ValueError(f'missing image name for instance {repr(instance)} in ' + json.dumps(job_command_list, indent = 4, sort_keys=True))
        image_name_by_instance_dict[instance] = image_name
        image_list.append(image_name)
        image_dict[image_name] = True
    job_dict['image_name_by_instance_dict'] = image_name_by_instance_dict
    job_dict['image_list'] = image_list
    job_dict['image_dict'] = image_dict
    return job_dict


def get_tp_dict(
        job_command_name,
        job_dict,
):
    tp_dict = {}
    compare_dict = None
    if job_command_name == 'ci-project-sanity-tfwk':
        #log.info(f'get_tp_dict: job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))
        compare_dict = {
            #'--device-wait-startup-timeout': True,
            #'--test-engine': True,
            #'--testcases-project-name': True,
            '--topology-tag-name': True,
            'instance_all_attr_dict': True,
            #'instance_attr_dict': True,
            #'attr_defaults_dict': True,
            'image_dict': True,
            #'image_list': True,
            #'image_name_by_instance_dict': True,
            #'instance_list': True,
            #'run_init_block': True,
            #'section_count': True,
            #'test_engine_block': True,
            #'testcase_list': True,
        }
    elif job_command_name == 'ci-project-sanity-ntp':
        #log.info(f'get_tp_dict: job_dict: ' + json.dumps(job_dict, indent = 4, sort_keys=True))
        compare_dict = {
            #'--enable-devtoolset-flag': True,
            '--ntp-topology-tag': True,
            #'-device-wait-time': True,
            #'-test-framework-command': True,
            #'instance_attr_dict': True,
            'image_dict': True,
            #'image_list': True,
            #'image_name_by_instance_dict': True,
            #'instance_configure_options': True,
            #'instance_list': True,
            #'testcase_list': True,
        }
    if compare_dict is not None:
        for name in compare_dict:
            if name in job_dict:
                tp_dict[name] = job_dict[name]
    return tp_dict


def add_topology(
        topology_dict,
        job_json_dict,
        job_dict,
):
    job_command_list = job_json_dict['job_command_list']
    job_command_name = job_command_list[0]
    if job_command_name in topology_dict['command_type_dict']:
        command_type_dict = topology_dict['command_type_dict'][job_command_name]
    else:
        command_type_dict = {}
        topology_dict['command_type_dict'][job_command_name] = command_type_dict

    #if 'image_dict' in job_dict:
    #    if len(job_dict['image_dict']) != 1:
    #        raise ValueError(f'add_topology: more than one different image for job_dict {repr(job_dict)}')

    tp_new_dict = get_tp_dict(
        job_command_name=job_command_name,
        job_dict=job_dict,
    )
    tp_new_text = f'{repr(tp_new_dict)}'

    topology_tag_name = ''
    if job_command_name == 'ci-project-sanity-tfwk':
        topology_tag_name = job_dict['--topology-tag-name']
    elif job_command_name == 'ci-project-sanity-ntp':
        topology_tag_name = job_dict['--ntp-topology-tag']

    matching_index = None
    for topology_index in sorted(command_type_dict):
        job_info_dict = command_type_dict[topology_index]
        tp_dict = job_info_dict['tp_dict']
        tp_text = f'{repr(tp_dict)}'
        if tp_new_text == tp_text:
            matching_index = topology_index
            break
    if matching_index is not None:
        job_info_dict = command_type_dict[matching_index]
        job_info_dict['job_counter'] += 1
        job_info_dict['job_json_list'].append(job_json_dict)
    else:
        topology_dict['topology_counter'] += 1
        topology_counter = topology_dict['topology_counter']
        topology_index = f'{topology_tag_name}:{topology_counter:04d}'
        job_info_dict = {
            'job_counter': 1,
            'job_json_list': [ job_json_dict ],
            'tp_dict': tp_new_dict,
        }
        command_type_dict[topology_index] = job_info_dict
    return


def generate_job_list_code(
        job_info_list,
        prefix_text,
        project_common_module_name,
):
    indent_amount = '    '
    generated_text = ''

    generated_text += f"[\n"

    current_indent = prefix_text + indent_amount

    for job_info_dict in job_info_list:
        job_json_dict = job_info_dict['job_json_dict']
        job_name = job_json_dict['job_name']
        job_command_list = job_json_dict['job_command_list']
        job_command_name = job_command_list[0]
        job_category = job_info_dict.get('job_category', None)
        if job_category is None:
            raise ValueError(f'main: missing job_category for job_command_list {repr(job_command_list)}')
        get_create_job_text_func = job_info_dict.get('get_create_job_text_func', None)
        generated_text += current_indent + f"# ----- ----- ----- ----- -----\n"
        #generated_text += current_indent + f"#log.info('  {job_category}: {job_command_name}: {job_name}')\n"
        generated_text += current_indent + f"# {job_category}: {job_command_name}: {job_name}\n"
        generated_text += current_indent + f"#\n"
        if get_create_job_text_func is None:
            item_text = get_item_text(
                data_item=job_json_dict,
                type='data',
                current_indent=current_indent,
            )
            #generated_text += current_indent + "job_json = " + item_text + "\n"
            generated_text += current_indent + item_text + ",\n"
        else:
            job_dict = job_info_dict['job_dict']
            item_text = get_create_job_text_func(
                job_json_dict=job_json_dict,
                job_dict=job_dict,
                indent=current_indent,
            )
            #generated_text += current_indent + "job_json = project_common." + item_text + "\n"
            generated_text += current_indent + project_common_module_name + "." + item_text + ",\n"

            show_debug_info_flag = False
            if show_debug_info_flag:
                item_org_text = get_item_text(
                    data_item=job_json_dict,
                    type='data',
                    current_indent=current_indent,
                )
                generated_text += current_indent + f"log.info('  ----- ----- ----- ----- -----')\n"
                generated_text += current_indent + f"item_text = " + f'{repr(item_text)}' + "\n"
                generated_text += current_indent + f"item_dict = " + item_org_text + "\n"
                generated_text += current_indent + f"log.info('  org_job_json: ' + json.dumps(item_dict, indent = 4, sort_keys=True))\n"
                generated_text += current_indent + f"log.info('  item_text: ' + item_text)\n"
                generated_text += current_indent + f"log.info('  new_job_json: ' + json.dumps(job_json, indent = 4, sort_keys=True))\n"

    generated_text += prefix_text + f"]\n"
    #generated_text += prefix_text + f"crapper\n"

    return generated_text


def generate_store_category_jobs_code(
        tree_obj,
        category_name,
        category_value,
        job_dict_var_name,
        job_list_var_name,
        project_common_module_name,
):
    generated_text = ''
    if tree_obj is not None:
        context_info_dict = tree_obj.get_value()
        context_index = context_info_dict['context_index']
        job_info_list = context_info_dict['job_info_list']
        num_jobs = len(job_info_list)
        generated_text += f"    {job_list_var_name} = "
        generated_text += generate_job_list_code(
            job_info_list=job_info_list,
            prefix_text='    ',
            project_common_module_name=project_common_module_name,
        )
        generated_text += f"    {project_common_module_name}.store_jobs_for_category(\n"
        generated_text += f"        category_name={repr(category_name)},\n"
        generated_text += f"        category_value={repr(category_value)},\n"
        generated_text += f"        category_job_dict={job_dict_var_name},\n"
        generated_text += f"        category_job_list={job_list_var_name},\n"
        generated_text += f"    )\n"
    return generated_text


def generate_add_category_jobs_code(
        child_list,
        project_common_module_name,
        project_info_json_var_name,
        category_name,
        add_jobs_func,
):
    job_build_dict_var_name = f'{category_name}_build_job_dict'
    job_build_list_var_name = f'{category_name}_build_job_list'
    job_sanity_dict_var_name = f'{category_name}_sanity_job_dict'
    job_sanity_list_var_name = f'{category_name}_sanity_job_list'

    generated_text = ''
    generated_text += f"    log.info('')\n"
    generated_text += f"    log.info('----- handling {category_name} -----')\n"
    generated_text += f"    {job_build_dict_var_name} = " + "{}\n"
    generated_text += f"    {job_sanity_dict_var_name} = " + "{}\n"
    for child_obj in child_list:
        category_value = child_obj.name
        context_info_dict = child_obj.get_value()
        context_index = context_info_dict['context_index']
        num_jobs = len(context_info_dict['job_info_list'])
        log.info(f'generate_add_category_jobs_code:   {category_name} {repr(category_value)}: {repr(context_index)}, num_jobs {repr(num_jobs)}')
        #for category_obj in child_obj.get_child_sequence():
        #    context_info_dict = category_obj.get_value()
        #    num_jobs = len(context_info_dict['job_info_list'])
        #    log.info(f'generate_add_category_jobs_code:     category_name {repr(category_obj.name)}, num_jobs {repr(num_jobs)}')

        generated_text += generate_store_category_jobs_code(
            tree_obj=child_obj['build'],
            category_name=f'{category_name}:build',
            category_value=category_value,
            job_dict_var_name=job_build_dict_var_name,
            job_list_var_name=job_build_list_var_name,
            project_common_module_name=project_common_module_name,
        )
        generated_text += generate_store_category_jobs_code(
            tree_obj=child_obj['sanity'],
            category_name=f'{category_name}:sanity',
            category_value=category_value,
            job_dict_var_name=job_sanity_dict_var_name,
            job_list_var_name=job_sanity_list_var_name,
            project_common_module_name=project_common_module_name,
        )

    generated_text += f"\n"
    generated_text += f"    #\n"
    generated_text += f"    # add image group sanities into {project_info_json_var_name}\n"
    generated_text += f"    #\n"
    generated_text += f"    {project_common_module_name}.{add_jobs_func}(\n"
    generated_text += f"        project_info_json={project_info_json_var_name},\n"
    generated_text += f"        job_build_dict={job_build_dict_var_name},\n"
    generated_text += f"        job_sanity_dict={job_sanity_dict_var_name},\n"
    generated_text += f"    )\n"
    return generated_text


def get_regression_obj(
    job_obj,
    index,
):
    context_info_dict = job_obj.get_value()
    tracker_dict = {}
    job_info_list = context_info_dict['job_info_list']
    for job_info_dict in job_info_list:
        job_category = job_info_dict.get('job_category', None)
        if job_category in tracker_dict:
            new_info_list = tracker_dict[job_category]
        else:
            new_info_list = []
            tracker_dict[job_category] = new_info_list
        new_info_list.append(job_info_dict)
    base_context_list = [
        index,
    ]
    parent_obj = tree_item_cl(
        name=index,
    )
    context_info_dict = {
        'context_name_list': base_context_list,
        'context_index': ':'.join(base_context_list),
        'context_name': base_context_list[0],
        'job_info_list': job_info_list,
    }
    parent_obj.set_value(
        value=context_info_dict,
    )
    #log.info(f'xxxxx: - tracker')
    for name in sorted(tracker_dict):
        #log.info(f'xxxxx:   {repr(name)}')
        child_obj = parent_obj.add_child(
            name=name,
        )
        child_context_list = base_context_list + [ name ]
        context_info_dict = {
            'context_name_list': child_context_list,
            'context_index': ':'.join(child_context_list),
            'context_name': child_context_list[0],
            'job_info_list': tracker_dict[name],
        }
        child_obj.set_value(
            value=context_info_dict,
        )
    return parent_obj

g_preamble_text = """
import os
import sys
import argparse
import json
import logging
import project_common

log = logging.getLogger(__name__)

def get_json(
):
    log.info(f'get_json: begin')
"""

g_postamble_text = """
#    log.info(f'get_json: end')
#    return
"""


def create_python_module_from_json(
        json_fname,
        stamp=None,
):
    log.info(f'create_python_module_from_json: reading from {repr(json_fname)}')
    with open(json_fname, 'r') as fhandle:
        original_json_dict = json.load(fhandle)

    original_json_dict['0-stamp'] = stamp
    # original_json_dict
    job_index_dict = {}
    tree_item_obj = tree_item_cl()
    job_total_dict = {
        'job_index_dict': job_index_dict,
        'tree_item_obj': tree_item_obj,
    }
    topology_dict = {
        'topology_counter': 0,
        'command_type_dict': {},
    }
    process_item(
        job_dict=job_total_dict,
        data_item=original_json_dict,
    )
    #log.info(f'create_python_module_from_json: xxx: ' + json.dumps(job_total_dict, indent = 4, sort_keys=True))

    generated_text = ''

    #
    # Go through various items that contain job trees to remove their job trees.
    # Later, we'll go through the collected jobs and re-insert
    # the job trees with json obtained through function calls instead of plain json.
    #

    # ['image_group_list'][]['sanity_jobs']
    # all sanity jobs in parallel
    if 'image_group_list' in original_json_dict:
        image_group_list = original_json_dict['image_group_list']
        for image_group_dict in image_group_list:
            if 'sanity_jobs' in image_group_dict:
                del image_group_dict['sanity_jobs']

    # ['qa_jobs']
    # all builds in parallel followed by all sanities in parallel
    if 'qa_jobs' in original_json_dict:
        del original_json_dict['qa_jobs']

    # ['recipe_repo_list'][]['recipe_repo_jobs']
    # all builds in parallel followed by all sanities in parallel
    if 'recipe_repo_list' in original_json_dict:
        recipe_repo_list = original_json_dict['recipe_repo_list']
        for recipe_repo_dict in recipe_repo_list:
            if 'recipe_repo_jobs' in recipe_repo_dict:
                del recipe_repo_dict['recipe_repo_jobs']


    # ['regression_defs']['regression_image_group_list'][]['build_jobs']
    # ['regression_defs']['regression_test_list'][]['regression_jobs']
    # need to discuss if can all builds in parallel followed by all sanities in parallel
    if 'regression_defs' in original_json_dict:
        regression_defs = original_json_dict['regression_defs']
        if 'regression_image_group_list' in regression_defs:
            del regression_defs['regression_image_group_list']
        if 'regression_test_list' in regression_defs:
            del regression_defs['regression_test_list']



    #
    # add code for the original JSON with job tree sections taken out
    #
    project_info_json_var_name = 'project_info_json'
    item_text = get_item_text(
        data_item=original_json_dict,
        type='data',
        current_indent='    ',
    )
    generated_text += f"    {project_info_json_var_name} = " + item_text + "\n"




    for category_obj in tree_item_obj.get_child_sequence():
        context_name = category_obj.name
        log.info(f'create_python_module_from_json: + context_name {repr(context_name)}')


    project_common_module_name = 'project_common'

    image_group_list_obj = tree_item_obj.get_obj(
        name_list=['image_group_list'],
    )
    if image_group_list_obj is not None:
        context_info_dict = image_group_list_obj.get_value()
        num_jobs = len(context_info_dict['job_info_list'])
        log.info(f'create_python_module_from_json: - image_group_list, num_jobs {repr(num_jobs)}')
        generated_text += generate_add_category_jobs_code(
            child_list=image_group_list_obj.get_child_list(),
            project_common_module_name=project_common_module_name,
            project_info_json_var_name=project_info_json_var_name,
            category_name='image_group',
            add_jobs_func='add_image_group_sanity_jobs',
        )



    qa_jobs_obj = tree_item_obj.get_obj(
        name_list=['qa_jobs'],
    )
    if qa_jobs_obj is not None:
        context_info_dict = qa_jobs_obj.get_value()
        num_jobs = len(context_info_dict['job_info_list'])
        log.info(f'create_python_module_from_json: - qa_jobs, num_jobs {repr(num_jobs)}')

        generated_text += generate_add_category_jobs_code(
            child_list=[qa_jobs_obj],
            project_common_module_name=project_common_module_name,
            project_info_json_var_name=project_info_json_var_name,
            category_name='qa',
            add_jobs_func='add_qa_jobs',
        )


    recipe_repo_list_obj = tree_item_obj.get_obj(
        name_list=['recipe_repo_list'],
    )
    if recipe_repo_list_obj is not None:
        # context_info_dict = image_group_list_obj.get_value()
        # num_jobs = len(context_info_dict['job_info_list'])
        # log.info(f'create_python_module_from_json: - image_group_list, num_jobs {repr(num_jobs)}')
        generated_text += generate_add_category_jobs_code(
            child_list=recipe_repo_list_obj.get_child_list(),
            project_common_module_name=project_common_module_name,
            project_info_json_var_name=project_info_json_var_name,
            category_name='recipe_repo',
            add_jobs_func='add_recipe_repo_jobs',
        )


    #regression_defs_obj = tree_item_obj.get_obj(
    #    name_list=['regression_defs'],
    #)
    #if regression_defs_obj is not None:
    #    log.info(f'create_python_module_from_json: - regression_defs')
    #    for recipe_repo_obj in regression_defs_obj.get_child_sequence():
    #        log.info(f'create_python_module_from_json:   section {repr(recipe_repo_obj.name)}')

    regression_image_group_list_obj = tree_item_obj.get_obj(
        name_list=['regression_defs', 'regression_image_group_list'],
    )
    if regression_image_group_list_obj is not None:
        context_info_dict = regression_image_group_list_obj.get_value()
        num_jobs = len(context_info_dict['job_info_list'])
        log.info(f'create_python_module_from_json: - regression_image_group_list, num_jobs {repr(num_jobs)}')

        parent_obj = get_regression_obj(
            job_obj=regression_image_group_list_obj,
            index='regression_image_group_list',
        )

        generated_text += generate_add_category_jobs_code(
            child_list=[parent_obj],
            project_common_module_name=project_common_module_name,
            project_info_json_var_name=project_info_json_var_name,
            category_name='reg_build',
            add_jobs_func='add_reg_build_jobs',
        )

    regression_test_list_obj = tree_item_obj.get_obj(
        name_list=['regression_defs', 'regression_test_list'],
    )
    if regression_test_list_obj is not None:
        context_info_dict = regression_test_list_obj.get_value()
        num_jobs = len(context_info_dict['job_info_list'])
        log.info(f'create_python_module_from_json: - regression_test_list, num_jobs {repr(num_jobs)}')

        parent_obj = get_regression_obj(
            job_obj=regression_test_list_obj,
            index='regression_test_list',
        )

        generated_text += generate_add_category_jobs_code(
            child_list=[parent_obj],
            project_common_module_name=project_common_module_name,
            project_info_json_var_name=project_info_json_var_name,
            category_name='reg_sanity',
            add_jobs_func='add_reg_sanity_jobs',
        )

    generated_text += f"    log.info(f'get_json: end')\n"
    generated_text += f"    return {project_info_json_var_name}\n"

    generated_fname = 'project_generated.py'
    log.info(f'create_python_module_from_json: ----- saving into {repr(generated_fname)} -----')
    with open(generated_fname, 'w') as fhandle:
        fhandle.write(g_preamble_text)
        fhandle.write(generated_text)
        fhandle.write(g_postamble_text)

    #import project_generated
    #new_json_dict = project_generated.get_json()
    #return new_json_dict

    return


def main(
        args,
):
    global g_project
    g_project = args.project
    json_fname = args.json_fname

    create_python_module_from_json(
        json_fname=json_fname,
        stamp='1',
    )

    # new1_json_fname = 'new-1.json'
    # command = [
    #     './project-info.py',
    #     '--out-json-fname', new1_json_fname,
    # ]
    # subprocess.run(command)
    #
    # create_python_module_from_json(
    #     json_fname=new1_json_fname,
    #     stamp='2',
    # )
    #
    # new2_json_fname = 'new-2.json'
    # command = [
    #     './project-info.py',
    #     '--out-json-fname', new2_json_fname,
    # ]
    # subprocess.run(command)

    return


def parse_arguments():
    """!
    Parse the input arguments for the product and origin
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--json-fname', action='store', default='project_info.json', help='xxx')
    parser.add_argument('--project', action='store', default='fss3', help='xxx')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()

    datefmt = '%Y-%m-%d %H:%M:%S'
    datefmt = '%H:%M:%S'

    logging_format = '#'
    #logging_format += ' %(asctime)s'
    #logging_format += ' ' + str(os.path.basename(__file__))
    logging_format += ' %(levelname)s: %(message)s'

    #log_level = logging.INFO
    #if args.verbosity >= 2:
    #    log_level = logging.DEBUG
    #elif args.verbosity == 1:
    #    log_level = logging.INFO
    #elif args.verbosity == 0:
    #    log_level = logging.WARNING
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format=logging_format, datefmt=datefmt)

    #log.info('args: %s', json.dumps(vars(args), indent = 4, sort_keys=True))
    main(args=args)
    log.info(f'done')
    sys.exit(0)
