# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Utilities for the unit tests."""

PROJECT = {
    "custom_keys": [],
    "description": "Fedora-messaging schemas for fedocal",
    "full_url": "http://localhost.localdomain/fedora-infra/fedocal-messages",
    "parent": None,
    "date_modified": "1602658714",
    "access_users": {
        "admin": [],
        "collaborator": [],
        "ticket": [],
        "owner": ["pingou"],
        "commit": [],
    },
    "namespace": "fedora-infra",
    "priorities": {},
    "id": 8820,
    "access_groups": {"admin": [], "collaborator": [], "ticket": [], "commit": []},
    "milestones": {},
    "user": {
        "fullname": "Pierre-YvesChibon",
        "url_path": "user/pingou",
        "full_url": "http://localhost.localdomain/user/pingou",
        "name": "pingou",
    },
    "date_created": "1602658714",
    "fullname": "fedora-infra/fedocal-messages",
    "url_path": "fedora-infra/fedocal-messages",
    "close_status": [],
    "tags": [],
    "name": "fedocal-messages",
}

FORK = {
    "custom_keys": [],
    "description": "A git centered forge",
    "full_url": "http://localhost.localdomain/fork/jjames/pagure",
    "parent": {
        "custom_keys": [],
        "description": "A git centered forge",
        "full_url": "http://localhost.localdomain/pagure",
        "parent": None,
        "date_modified": "1590422384",
        "access_users": {
            "admin": ["ryanlerch"],
            "collaborator": [],
            "ticket": [
                "farhaan",
                "jcline",
                "jlanda",
                "karsten",
                "lenkaseg",
                "lslebodn",
                "mprahl",
                "ngompa",
                "vivekanand1101",
            ],
            "owner": ["pingou"],
            "commit": ["bkabrda", "cverna", "puiterwijk"],
        },
        "namespace": None,
        "priorities": {"": "", "1": "High", "3": "Low", "2": "Normal"},
        "id": 10,
        "access_groups": {
            "admin": [],
            "collaborator": [],
            "ticket": [],
            "commit": [],
        },
        "milestones": {
            "5.0": {"active": False, "date": None},
            "5.1": {"active": False, "date": None},
            "5.2": {"active": False, "date": "January 7th 2019"},
            "5.3": {"active": False, "date": "February 7th 2019"},
            "5.4": {"active": False, "date": "March 7th 2019"},
            "5.5": {"active": False, "date": "April 7th 2019"},
            "5.6": {"active": False, "date": "May 7th 2019"},
            "5.7": {"active": False, "date": "July 7th 2019"},
            "5.8": {"active": False, "date": "August 7th"},
            "5.9": {"active": False, "date": None},
            "Coming 3 months": {"active": True, "date": None},
            "5.12": {"active": True, "date": None},
            "5.13": {"active": True, "date": None},
            "5.10": {"active": False, "date": None},
            "5.11": {"active": False, "date": None},
            "6.0": {"active": True, "date": None},
            "Coming 6 months": {"active": True, "date": None},
        },
        "user": {
            "fullname": "Pierre-YvesChibon",
            "url_path": "user/pingou",
            "full_url": "http://localhost.localdomain/user/pingou",
            "name": "pingou",
        },
        "date_created": "1431549490",
        "fullname": "pagure",
        "url_path": "pagure",
        "close_status": [
            "Invalid",
            "Insufficient data",
            "Fixed",
            "Duplicate",
            "Won't Fix",
        ],
        "tags": ["pagure", "fedmsg"],
        "name": "pagure",
    },
    "date_modified": "1602543006",
    "access_users": {
        "admin": [],
        "collaborator": [],
        "ticket": [],
        "owner": ["jjames"],
        "commit": [],
    },
    "namespace": None,
    "priorities": {},
    "id": 8813,
    "access_groups": {
        "admin": [],
        "collaborator": [],
        "ticket": [],
        "commit": [],
    },
    "milestones": {},
    "user": {
        "fullname": "Jerry James",
        "url_path": "user/jjames",
        "full_url": "http://localhost.localdomain/user/jjames",
        "name": "jjames",
    },
    "date_created": "1602543006",
    "fullname": "forks/jjames/pagure",
    "url_path": "fork/jjames/pagure",
    "close_status": [],
    "tags": [],
    "name": "pagure",
}


ISSUE = {
    "status": "Open",
    "priority": 3,
    "last_updated": "1602574891",
    "blocks": [],
    "boards": [
        {
            "status": {
                "default": False,
                "bg_color": "#15d415",
                "close_status": "Fixed",
                "name": "Done",
                "close": True,
            },
            "board": {
                "active": True,
                "status": [
                    {
                        "default": True,
                        "bg_color": "#ffb300",
                        "close_status": None,
                        "name": "Backlog",
                        "close": False,
                    },
                    {
                        "default": False,
                        "bg_color": "#f4ff64",
                        "close_status": None,
                        "name": "Triaged",
                        "close": False,
                    },
                    {
                        "default": False,
                        "bg_color": "#99d200",
                        "close_status": None,
                        "name": "In Progress",
                        "close": False,
                    },
                    {
                        "default": False,
                        "bg_color": "#3c7bff",
                        "close_status": None,
                        "name": "In Review",
                        "close": False,
                    },
                    {
                        "default": False,
                        "bg_color": "#15d415",
                        "close_status": "Fixed",
                        "name": "Done",
                        "close": True,
                    },
                    {
                        "default": False,
                        "bg_color": "#e80909",
                        "close_status": None,
                        "name": "Blocked",
                        "close": False,
                    },
                ],
                "tag": {
                    "tag_color": "#3efa0e",
                    "tag": "ops",
                    "tag_description": "ops problem now...",
                },
                "name": "ops",
                "full_url": "http://localhost.localdomain/test/boards/ops",
            },
            "rank": 8,
        }
    ],
    "tags": ["medium-gain", "medium-trouble", "ops"],
    "title": "aws: fedora-ci access to s3 bucket request",
    "related_prs": [],
    "milestone": None,
    "comments": [
        {
            "comment": "This is related to the previous ticket and comment: "
            "https://pagure.io/fedora-infrastructure/issue/8958#comment-656531",
            "reactions": {},
            "parent": None,
            "notification": False,
            "edited_on": None,
            "editor": None,
            "date_created": "1599751495",
            "id": 677658,
            "user": {
                "fullname": "Andrei Stepanov",
                "url_path": "user/astepano",
                "full_url": "http://localhost.localdomain/user/astepano",
                "name": "astepano",
            },
        },
        {
            "comment": "**Metadata Update from @kevin**:\n- Issue priority "
            "set to: Waiting on Assignee (was: Needs Review)\n- "
            "Issue tagged with: medium-gain, medium-trouble, ops",
            "reactions": {},
            "parent": None,
            "notification": True,
            "edited_on": None,
            "editor": None,
            "date_created": "1599760908",
            "id": 677717,
            "user": {
                "fullname": "Kevin Fenzi",
                "url_path": "user/kevin",
                "full_url": "http://localhost.localdomain/user/kevin",
                "name": "kevin",
            },
        },
    ],
    "close_status": None,
    "content": "Good day.\r\n\r\nIn context of fedora-ci initiative may we ask "
    "to have an access to s3 bucket please?\r\nCurrently we are deploying "
    "pipelines on AWS EKS: https://osci-jenkins-1.ci.fedoraproject.org/\r\n"
    "We need to store artifacts and logs with easy way of maintenance. \r\n"
    "\r\nI see there are two ways:\r\n\r\n1. Allow to `user/fedora-ci-osci` "
    "token create s3 buckets on demand. This would be preferable solution. "
    "From our side I promise to follow resource-tagging conventions... ",
    "assignee": None,
    "depends": [],
    "private": False,
    "date_created": "1599751343",
    "full_url": "http://localhost.localdomain/test/issue/9311",
    "id": 9311,
    "closed_at": "1602535496",
    "closed_by": {
        "fullname": "Kevin Fenzi",
        "url_path": "user/kevin",
        "full_url": "http://localhost.localdomain/user/kevin",
        "name": "kevin",
    },
    "custom_fields": [],
    "user": {
        "fullname": "Andrei Stepanov",
        "full_url": "http://localhost.localdomain/user/astepano",
        "url_path": "user/astepano",
        "name": "astepano",
    },
}


PULL_REQUEST = {
    "last_updated": "1602575128",
    "uid": "f763d8f1254440c782a7cde84ae5f422",
    "initial_comment": "I just created a new project on pagure.io.  "
    "Two of the instructions I was given on setting up my new repo were out of order.",
    "commit_stop": "2e8db9ce332cae0747f6b38e414bb99634f9b662",
    "remote_git": None,
    "closed_at": "1602575128",
    "full_url": "http://localhost.localdomain/pagure/pull-request/5014",
    "id": 5014,
    "title": "Reverse out of order instructions for new repos",
    "comments": [
        {
            "comment": "Good catch, thanks!",
            "reactions": {},
            "parent": None,
            "notification": False,
            "tree": None,
            "filename": None,
            "edited_on": None,
            "editor": None,
            "date_created": "1602575085",
            "commit": None,
            "line": None,
            "id": 133903,
            "user": {
                "fullname": "Pierre-YvesChibon",
                "url_path": "user/pingou",
                "full_url": "http://localhost.localdomain/user/pingou",
                "name": "pingou",
            },
        },
        {
            "comment": "Pull-Request has been merged by pingou",
            "reactions": {},
            "parent": None,
            "notification": True,
            "tree": None,
            "filename": None,
            "edited_on": None,
            "editor": None,
            "date_created": "1602575128",
            "commit": None,
            "line": None,
            "id": 133905,
            "user": {
                "fullname": "Pierre-YvesChibon",
                "url_path": "user/pingou",
                "full_url": "http://localhost.localdomain/user/pingou",
                "name": "pingou",
            },
        },
    ],
    "branch": "master",
    "status": "Merged",
    "tags": [],
    "user": {
        "fullname": "Jerry James",
        "url_path": "user/jjames",
        "full_url": "http://localhost.localdomain/user/jjames",
        "name": "jjames",
    },
    "date_created": "1602543367",
    "closed_by": {
        "fullname": "Pierre-YvesChibon",
        "url_path": "user/pingou",
        "full_url": "http://localhost.localdomain/user/pingou",
        "name": "pingou",
    },
    "branch_from": "master",
    "assignee": None,
    "commit_start": "2e8db9ce332cae0747f6b38e414bb99634f9b662",
    "project": {
        "custom_keys": [],
        "description": "A git centered forge",
        "full_url": "http://localhost.localdomain/pagure",
        "parent": None,
        "date_modified": "1590422384",
        "access_users": {
            "admin": ["ryanlerch"],
            "collaborator": [],
            "ticket": [
                "farhaan",
                "jcline",
                "jlanda",
                "karsten",
                "lenkaseg",
                "lslebodn",
                "mprahl",
                "ngompa",
                "vivekanand1101",
            ],
            "owner": ["pingou"],
            "commit": ["bkabrda", "cverna", "puiterwijk"],
        },
        "namespace": None,
        "priorities": {"": "", "1": "High", "3": "Low", "2": "Normal"},
        "id": 10,
        "access_groups": {
            "admin": [],
            "collaborator": [],
            "ticket": [],
            "commit": [],
        },
        "milestones": {
            "5.0": {"active": False, "date": None},
            "5.1": {"active": False, "date": None},
            "5.2": {"active": False, "date": "January 7th 2019"},
            "5.3": {"active": False, "date": "February 7th 2019"},
            "5.4": {"active": False, "date": "March 7th 2019"},
            "5.5": {"active": False, "date": "April 7th 2019"},
            "5.6": {"active": False, "date": "May 7th 2019"},
            "5.7": {"active": False, "date": "July 7th 2019"},
            "5.8": {"active": False, "date": "August 7th"},
            "5.9": {"active": False, "date": None},
            "Coming 3 months": {"active": True, "date": None},
            "5.12": {"active": True, "date": None},
            "5.13": {"active": True, "date": None},
            "5.10": {"active": False, "date": None},
            "5.11": {"active": False, "date": None},
            "6.0": {"active": True, "date": None},
            "Coming 6 months": {"active": True, "date": None},
        },
        "user": {
            "fullname": "Pierre-YvesChibon",
            "url_path": "user/pingou",
            "full_url": "http://localhost.localdomain/user/pingou",
            "name": "pingou",
        },
        "date_created": "1431549490",
        "fullname": "pagure",
        "url_path": "pagure",
        "close_status": [
            "Invalid",
            "Insufficient data",
            "Fixed",
            "Duplicate",
            "Won't Fix",
        ],
        "tags": ["pagure", "fedmsg"],
        "name": "pagure",
    },
    "repo_from": {
        "custom_keys": [],
        "description": "A git centered forge",
        "parent": {
            "custom_keys": [],
            "description": "A git centered forge",
            "full_url": "http://localhost.localdomain/pagure",
            "parent": None,
            "date_modified": "1590422384",
            "access_users": {
                "admin": ["ryanlerch"],
                "collaborator": [],
                "ticket": [
                    "farhaan",
                    "jcline",
                    "jlanda",
                    "karsten",
                    "lenkaseg",
                    "lslebodn",
                    "mprahl",
                    "ngompa",
                    "vivekanand1101",
                ],
                "owner": ["pingou"],
                "commit": ["bkabrda", "cverna", "puiterwijk"],
            },
            "namespace": None,
            "priorities": {"": "", "1": "High", "3": "Low", "2": "Normal"},
            "id": 10,
            "access_groups": {
                "admin": [],
                "collaborator": [],
                "ticket": [],
                "commit": [],
            },
            "milestones": {
                "5.0": {"active": False, "date": None},
                "5.1": {"active": False, "date": None},
                "5.2": {"active": False, "date": "January 7th 2019"},
                "5.3": {"active": False, "date": "February 7th 2019"},
                "5.4": {"active": False, "date": "March 7th 2019"},
                "5.5": {"active": False, "date": "April 7th 2019"},
                "5.6": {"active": False, "date": "May 7th 2019"},
                "5.7": {"active": False, "date": "July 7th 2019"},
                "5.8": {"active": False, "date": "August 7th"},
                "5.9": {"active": False, "date": None},
                "Coming 3 months": {"active": True, "date": None},
                "5.12": {"active": True, "date": None},
                "5.13": {"active": True, "date": None},
                "5.10": {"active": False, "date": None},
                "5.11": {"active": False, "date": None},
                "6.0": {"active": True, "date": None},
                "Coming 6 months": {"active": True, "date": None},
            },
            "user": {
                "fullname": "Pierre-YvesChibon",
                "url_path": "user/pingou",
                "full_url": "http://localhost.localdomain/user/pingou",
                "name": "pingou",
            },
            "date_created": "1431549490",
            "fullname": "pagure",
            "url_path": "pagure",
            "close_status": [
                "Invalid",
                "Insufficient data",
                "Fixed",
                "Duplicate",
                "Won't Fix",
            ],
            "tags": ["pagure", "fedmsg"],
            "name": "pagure",
        },
        "date_modified": "1602543006",
        "access_users": {
            "admin": [],
            "collaborator": [],
            "ticket": [],
            "owner": ["jjames"],
            "commit": [],
        },
        "namespace": None,
        "priorities": {},
        "id": 8813,
        "access_groups": {
            "admin": [],
            "collaborator": [],
            "ticket": [],
            "commit": [],
        },
        "milestones": {},
        "user": {
            "fullname": "Jerry James",
            "url_path": "user/jjames",
            "name": "jjames",
        },
        "date_created": "1602543006",
        "fullname": "forks/jjames/pagure",
        "url_path": "fork/jjames/pagure",
        "close_status": [],
        "tags": [],
        "name": "pagure",
    },
    "cached_merge_status": "unknown",
    "updated_on": "1602575128",
    "threshold_reached": None,
}


COMMIT_FLAG = {
    "comment": "Build failed.",
    "status": "failure",
    "date_updated": "1602688864",
    "percent": "0",
    "username": "jenkins",
    "url": "https://jenkins.example.org/job/project/job/project-postmerge/264/",
    "commit_hash": "36ca6c643221858eda70e2b52a6aee666dc6e576",
    "date_created": "1602687207",
    "user": {
        "fullname": "foobar",
        "url_path": "user/foobar",
        "name": "foobar",
        "full_url": "http://localhost.localdomain/user/foobar",
    },
}


GROUP = {
    "display_name": "fedora infra folks",
    "description": "Fedora infrastructure team",
    "creator": {
        "fullname": "pingou",
        "url_path": "user/pingou",
        "name": "pingou",
        "full_url": "http://localhost.localdomain/user/pingou",
    },
    "members": [
        "pingou",
        "kevin",
        "smooge",
        "ralph",
    ],
    "date_created": "1598094647",
    "group_type": "user",
    "name": "fedora-infra",
    "full_url": "http://localhost.localdomain/group/fedora-infra",
}
