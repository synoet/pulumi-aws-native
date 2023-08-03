# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'FirewallPolicyOverrideAction',
    'FirewallPolicyRuleOrder',
    'FirewallPolicyStreamExceptionPolicy',
    'LoggingConfigurationLogDestinationConfigLogDestinationType',
    'LoggingConfigurationLogDestinationConfigLogType',
    'RuleGroupGeneratedRulesType',
    'RuleGroupHeaderDirection',
    'RuleGroupHeaderProtocol',
    'RuleGroupRuleOrder',
    'RuleGroupStatefulRuleAction',
    'RuleGroupTargetType',
    'RuleGroupTcpFlag',
    'RuleGroupTypeEnum',
]


class FirewallPolicyOverrideAction(str, Enum):
    DROP_TO_ALERT = "DROP_TO_ALERT"


class FirewallPolicyRuleOrder(str, Enum):
    DEFAULT_ACTION_ORDER = "DEFAULT_ACTION_ORDER"
    STRICT_ORDER = "STRICT_ORDER"


class FirewallPolicyStreamExceptionPolicy(str, Enum):
    DROP = "DROP"
    CONTINUE_ = "CONTINUE"
    REJECT = "REJECT"


class LoggingConfigurationLogDestinationConfigLogDestinationType(str, Enum):
    S3 = "S3"
    CLOUD_WATCH_LOGS = "CloudWatchLogs"
    KINESIS_DATA_FIREHOSE = "KinesisDataFirehose"


class LoggingConfigurationLogDestinationConfigLogType(str, Enum):
    ALERT = "ALERT"
    FLOW = "FLOW"


class RuleGroupGeneratedRulesType(str, Enum):
    ALLOWLIST = "ALLOWLIST"
    DENYLIST = "DENYLIST"


class RuleGroupHeaderDirection(str, Enum):
    FORWARD = "FORWARD"
    ANY = "ANY"


class RuleGroupHeaderProtocol(str, Enum):
    IP = "IP"
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"
    HTTP = "HTTP"
    FTP = "FTP"
    TLS = "TLS"
    SMB = "SMB"
    DNS = "DNS"
    DCERPC = "DCERPC"
    SSH = "SSH"
    SMTP = "SMTP"
    IMAP = "IMAP"
    MSN = "MSN"
    KRB5 = "KRB5"
    IKEV2 = "IKEV2"
    TFTP = "TFTP"
    NTP = "NTP"
    DHCP = "DHCP"


class RuleGroupRuleOrder(str, Enum):
    DEFAULT_ACTION_ORDER = "DEFAULT_ACTION_ORDER"
    STRICT_ORDER = "STRICT_ORDER"


class RuleGroupStatefulRuleAction(str, Enum):
    PASS_ = "PASS"
    DROP = "DROP"
    ALERT = "ALERT"
    REJECT = "REJECT"


class RuleGroupTargetType(str, Enum):
    TLS_SNI = "TLS_SNI"
    HTTP_HOST = "HTTP_HOST"


class RuleGroupTcpFlag(str, Enum):
    FIN = "FIN"
    SYN = "SYN"
    RST = "RST"
    PSH = "PSH"
    ACK = "ACK"
    URG = "URG"
    ECE = "ECE"
    CWR = "CWR"


class RuleGroupTypeEnum(str, Enum):
    STATELESS = "STATELESS"
    STATEFUL = "STATEFUL"
