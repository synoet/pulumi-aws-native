// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ContactFlowModuleState = {
    Active: "ACTIVE",
    Archived: "ARCHIVED",
} as const;

/**
 * The state of the contact flow module.
 */
export type ContactFlowModuleState = (typeof ContactFlowModuleState)[keyof typeof ContactFlowModuleState];

export const ContactFlowModuleStatus = {
    Published: "PUBLISHED",
    Saved: "SAVED",
} as const;

/**
 * The status of the contact flow module.
 */
export type ContactFlowModuleStatus = (typeof ContactFlowModuleStatus)[keyof typeof ContactFlowModuleStatus];

export const ContactFlowState = {
    Active: "ACTIVE",
    Archived: "ARCHIVED",
} as const;

/**
 * The state of the contact flow.
 */
export type ContactFlowState = (typeof ContactFlowState)[keyof typeof ContactFlowState];

export const ContactFlowType = {
    ContactFlow: "CONTACT_FLOW",
    CustomerQueue: "CUSTOMER_QUEUE",
    CustomerHold: "CUSTOMER_HOLD",
    CustomerWhisper: "CUSTOMER_WHISPER",
    AgentHold: "AGENT_HOLD",
    AgentWhisper: "AGENT_WHISPER",
    OutboundWhisper: "OUTBOUND_WHISPER",
    AgentTransfer: "AGENT_TRANSFER",
    QueueTransfer: "QUEUE_TRANSFER",
} as const;

/**
 * The type of the contact flow.
 */
export type ContactFlowType = (typeof ContactFlowType)[keyof typeof ContactFlowType];

export const HoursOfOperationConfigDay = {
    Sunday: "SUNDAY",
    Monday: "MONDAY",
    Tuesday: "TUESDAY",
    Wednesday: "WEDNESDAY",
    Thursday: "THURSDAY",
    Friday: "FRIDAY",
    Saturday: "SATURDAY",
} as const;

/**
 * The day that the hours of operation applies to.
 */
export type HoursOfOperationConfigDay = (typeof HoursOfOperationConfigDay)[keyof typeof HoursOfOperationConfigDay];

export const InstanceIdentityManagementType = {
    Saml: "SAML",
    ConnectManaged: "CONNECT_MANAGED",
    ExistingDirectory: "EXISTING_DIRECTORY",
} as const;

/**
 * Specifies the type of directory integration for new instance.
 */
export type InstanceIdentityManagementType = (typeof InstanceIdentityManagementType)[keyof typeof InstanceIdentityManagementType];

export const InstanceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationFailed: "CREATION_FAILED",
    Active: "ACTIVE",
} as const;

/**
 * Specifies the creation status of new instance.
 */
export type InstanceStatus = (typeof InstanceStatus)[keyof typeof InstanceStatus];

export const QuickConnectType = {
    PhoneNumber: "PHONE_NUMBER",
    Queue: "QUEUE",
    User: "USER",
} as const;

/**
 * The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
 */
export type QuickConnectType = (typeof QuickConnectType)[keyof typeof QuickConnectType];

export const TaskTemplateFieldType = {
    Name: "NAME",
    Description: "DESCRIPTION",
    ScheduledTime: "SCHEDULED_TIME",
    QuickConnect: "QUICK_CONNECT",
    Url: "URL",
    Number: "NUMBER",
    Text: "TEXT",
    TextArea: "TEXT_AREA",
    DateTime: "DATE_TIME",
    Boolean: "BOOLEAN",
    SingleSelect: "SINGLE_SELECT",
    Email: "EMAIL",
} as const;

/**
 * The type of the task template's field
 */
export type TaskTemplateFieldType = (typeof TaskTemplateFieldType)[keyof typeof TaskTemplateFieldType];

export const TaskTemplateStatus = {
    Active: "ACTIVE",
    Inactive: "INACTIVE",
} as const;

/**
 * The status of the task template
 */
export type TaskTemplateStatus = (typeof TaskTemplateStatus)[keyof typeof TaskTemplateStatus];

export const UserPhoneType = {
    SoftPhone: "SOFT_PHONE",
    DeskPhone: "DESK_PHONE",
} as const;

/**
 * The phone type.
 */
export type UserPhoneType = (typeof UserPhoneType)[keyof typeof UserPhoneType];
