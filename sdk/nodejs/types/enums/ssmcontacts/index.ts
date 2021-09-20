// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ContactChannelChannelType = {
    Sms: "SMS",
    Voice: "VOICE",
    Email: "EMAIL",
} as const;

/**
 * Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.
 */
export type ContactChannelChannelType = (typeof ContactChannelChannelType)[keyof typeof ContactChannelChannelType];

export const ContactType = {
    Personal: "PERSONAL",
    Custom: "CUSTOM",
    Service: "SERVICE",
    Escalation: "ESCALATION",
} as const;

/**
 * Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.
 */
export type ContactType = (typeof ContactType)[keyof typeof ContactType];
