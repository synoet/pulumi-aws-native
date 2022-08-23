# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ContactFlowModuleState',
    'ContactFlowModuleStatus',
    'ContactFlowState',
    'ContactFlowType',
    'HoursOfOperationConfigDay',
    'InstanceIdentityManagementType',
    'InstanceStatus',
    'QuickConnectType',
    'TaskTemplateFieldType',
    'TaskTemplateStatus',
    'UserPhoneType',
]


class ContactFlowModuleState(str, Enum):
    """
    The state of the contact flow module.
    """
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class ContactFlowModuleStatus(str, Enum):
    """
    The status of the contact flow module.
    """
    PUBLISHED = "PUBLISHED"
    SAVED = "SAVED"


class ContactFlowState(str, Enum):
    """
    The state of the contact flow.
    """
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class ContactFlowType(str, Enum):
    """
    The type of the contact flow.
    """
    CONTACT_FLOW = "CONTACT_FLOW"
    CUSTOMER_QUEUE = "CUSTOMER_QUEUE"
    CUSTOMER_HOLD = "CUSTOMER_HOLD"
    CUSTOMER_WHISPER = "CUSTOMER_WHISPER"
    AGENT_HOLD = "AGENT_HOLD"
    AGENT_WHISPER = "AGENT_WHISPER"
    OUTBOUND_WHISPER = "OUTBOUND_WHISPER"
    AGENT_TRANSFER = "AGENT_TRANSFER"
    QUEUE_TRANSFER = "QUEUE_TRANSFER"


class HoursOfOperationConfigDay(str, Enum):
    """
    The day that the hours of operation applies to.
    """
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"


class InstanceIdentityManagementType(str, Enum):
    """
    Specifies the type of directory integration for new instance.
    """
    SAML = "SAML"
    CONNECT_MANAGED = "CONNECT_MANAGED"
    EXISTING_DIRECTORY = "EXISTING_DIRECTORY"


class InstanceStatus(str, Enum):
    """
    Specifies the creation status of new instance.
    """
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_FAILED = "CREATION_FAILED"
    ACTIVE = "ACTIVE"


class QuickConnectType(str, Enum):
    """
    The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
    """
    PHONE_NUMBER = "PHONE_NUMBER"
    QUEUE = "QUEUE"
    USER = "USER"


class TaskTemplateFieldType(str, Enum):
    """
    The type of the task template's field
    """
    NAME = "NAME"
    DESCRIPTION = "DESCRIPTION"
    SCHEDULED_TIME = "SCHEDULED_TIME"
    QUICK_CONNECT = "QUICK_CONNECT"
    URL = "URL"
    NUMBER = "NUMBER"
    TEXT = "TEXT"
    TEXT_AREA = "TEXT_AREA"
    DATE_TIME = "DATE_TIME"
    BOOLEAN = "BOOLEAN"
    SINGLE_SELECT = "SINGLE_SELECT"
    EMAIL = "EMAIL"


class TaskTemplateStatus(str, Enum):
    """
    The status of the task template
    """
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class UserPhoneType(str, Enum):
    """
    The phone type.
    """
    SOFT_PHONE = "SOFT_PHONE"
    DESK_PHONE = "DESK_PHONE"
