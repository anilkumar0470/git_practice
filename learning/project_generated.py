
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
    project_info_json = {
        '0-stamp': '1',
        'recipe_repo_list': [
            {
                'disable_flag.ci-release-project': False,
                'disable_flag.ci-release-recipe-repo': False,
                'disable_flag.ci-review': False,
                'disable_flag.ci-review-recipe-repo': False,
                'disable_flag.ci-update-manifest': False,
                'disable_flag.ci-update-manifest-recipe-repo': False,
                'office_365_connector': {
                    'disable_flag.ci-release-project': False,
                    'disable_flag.ci-release-recipe-repo': False,
                    'disable_flag.ci-review': False,
                    'disable_flag.ci-review-recipe-repo': False,
                    'disable_flag.ci-update-manifest': False,
                    'disable_flag.ci-update-manifest-recipe-repo': False,
                    'teams_channel_incoming_webhook_url': 'https://fujitsu.webhook.office.com/webhookb2/e3ad18e8-e04e-417a-bb6c-9b9cd5c02fad@a19f121d-81e1-4858-a9d8-736e267fd4c7/IncomingWebhook/1eece96f11074b819c2394ed1e2c614e/16431a81-bb3c-48fc-9684-0ae4b87f18f3',
                },
                'recipe_repo_branch': 'fss3',
                'recipe_repo_commit_updated_manifest_flag': True,
                'recipe_repo_handling_pipeline': 'recipe-repo-pipeline',
                'recipe_repo_jenkins': {
                    'debug_echo_recipe_repo_json_contents_flag': False,
                },
                'recipe_repo_manifest_fname': 'recipes/recipe-meta-fss-layer1.xml',
                'recipe_repo_name': 'meta-fss-layer1',
                'recipe_repo_path': 'poky/meta-fss-layer1',
                'recipe_repo_pipeline_disable_flag.ci-release-recipe-repo': False,
                'recipe_repo_pipeline_disable_flag.ci-review-recipe-repo': False,
                'recipe_repo_pipeline_disable_flag.ci-update-manifest-recipe-repo': False,
                'recipe_repo_project': 'apps',
            },
        ],
    }
    log.info('')
    log.info('----- handling recipe_repo -----')
    recipe_repo_build_job_dict = {}
    recipe_repo_sanity_job_dict = {}
    recipe_repo_build_job_list = [
        # ----- ----- ----- ----- -----
        # build: ci-project-build: build-fss-image-full-layer1
        #
        project_common.create_build_job(
            disable_flag={
                'ci-release-project': 'disabled',
                'ci-review': 'disabled',
                'ci-update-manifest-recipe-repo': 'disabled',
            },
            job_command_dict={
                '--enable-devtoolset-flag': True,
                '-cache': True,
                '-machine': 'qemux86-64',
                'image_dict': {
                    'fss-image-full-layer1': {
                        'archive_flag': True,
                    },
                    'meta-ide-support': {
                    },
                },
            },
            job_name='build-fss-image-full-layer1',
            job_timeout_amount=3,
        ),
    ]
    project_common.store_jobs_for_category(
        category_name='recipe_repo:build',
        category_value='meta-fss-layer1',
        category_job_dict=recipe_repo_build_job_dict,
        category_job_list=recipe_repo_build_job_list,
    )
    recipe_repo_sanity_job_list = [
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-eth-mapper-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-ETH',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_eth.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-eth-mapper-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-oduk-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OCHOD',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_ochodu_oduk.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-oduk-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-otsi-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OTSI',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_otsi.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-otsi-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-otuk-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OCHOD',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_ochodu_ochotu.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-otuk-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-odui-j-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OCHOD',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_ochodu_oduj_i.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-odui-j-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-tcm-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-ETH',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_tcm.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-tcm-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-otsi2-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': True,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': True,
            'disable_flag.ci-update-manifest': True,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OTSI2',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_otsi2.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-otsi2-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-otsg2-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': False,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': False,
            'disable_flag.ci-update-manifest': False,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-OTSG2',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_otsg2.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-failure',
            'job_name': 'layer1-otsg2-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 3,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
        # ----- ----- ----- ----- -----
        # sanity: ci-project-sanity-ntp: layer1-otsg2-blade-sanity
        #
        {
            'disable_flag.ci-release-project': True,
            'disable_flag.ci-release-recipe-repo': True,
            'disable_flag.ci-review': True,
            'disable_flag.ci-review-recipe-repo': True,
            'disable_flag.ci-update-manifest': True,
            'disable_flag.ci-update-manifest-recipe-repo': True,
            'job_agent': 'sanity-docker',
            'job_command_list': [
                'ci-project-sanity-ntp',
                '-test-framework-command',
                'Warrior/Warrior',
                '-device-wait-time',
                '600',
                '--ntp-topology-tag',
                '1-NE-1-Blade',
                '--ntp-instance-context-machine-name',
                'network-element:NE1/device:main',
                'qemux86-64',
                '--ntp-instance-context-image-name',
                'network-element:NE1/device:main',
                'fss-image-full-layer1',
                '--ntp-instance-context-image-info-config-name',
                'network-element:NE1/device:main',
                'main-L1-ETH',
                '--ntp-instance-context-add',
                'network-element:NE1/device:main',
                '--warrior-testcase',
                '../L1TC/Projects/project_sanity_blade_tcm.xml',
                '--enable-devtoolset-flag',
            ],
            'job_docker_container_flag': True,
            'job_failure_handling': 'pipeline-success',
            'job_name': 'layer1-otsg2-blade-sanity',
            'job_propagate_flag': True,
            'job_quiet_period': 0,
            'job_stash_flag': True,
            'job_template': 'ci-pipeline-job.xml',
            'job_timeout_amount': 1,
            'job_timeout_unit': 'HOURS',
            'job_type': 'explicit',
            'job_unstash_flag': True,
            'job_wait_flag': True,
            'previous_job_method': 'previous-job',
        },
    ]
    project_common.store_jobs_for_category(
        category_name='recipe_repo:sanity',
        category_value='meta-fss-layer1',
        category_job_dict=recipe_repo_sanity_job_dict,
        category_job_list=recipe_repo_sanity_job_list,
    )

    #
    # add image group sanities into project_info_json
    #
    project_common.add_recipe_repo_jobs(
        project_info_json=project_info_json,
        job_build_dict=recipe_repo_build_job_dict,
        job_sanity_dict=recipe_repo_sanity_job_dict,
    )
    log.info(f'get_json: end')
    return project_info_json

#    log.info(f'get_json: end')
#    return
